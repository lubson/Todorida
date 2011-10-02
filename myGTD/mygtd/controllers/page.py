import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from mygtd import model

import mygtd.lib.helpers as h

import formencode
from formencode import htmlfill

from pylons.decorators import validate

from pylons.decorators.rest import restrict

from mygtd.lib.base import BaseController, render

from authkit.permissions import ValidAuthKitUser
from authkit.authorize.pylons_adaptors import authorize

from mygtd.model import meta

from webhelpers.html.tags import HTML
import datetime

import mygtd.lib.gtdlib as l

log = logging.getLogger(__name__)

def sayHello():
    return 'hello'

class NewInboxForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    content = formencode.validators.String()
    created = formencode.validators.DateConverter(
            month_style='dd/mm/yyyy'
    )

class NewProjectForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    id = formencode.validators.Int()
    realm_id = formencode.validators.Int()
    name = formencode.validators.String()
    note = formencode.validators.String()
    tags = formencode.validators.String()
    due = formencode.validators.DateConverter(
            month_style='dd/mm/yyyy'
    )
    state = formencode.validators.String()

class NewTaskForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    task_realm_id = formencode.validators.Int()
    relevantProjects = formencode.validators.Int()
    name = formencode.validators.String()
    note = formencode.validators.String()
    tags = formencode.validators.String()
    scheduled = formencode.validators.DateConverter(
            month_style='dd/mm/yyyy'
    )
    due = formencode.validators.DateConverter(
            month_style='dd/mm/yyyy'
    )
    state = formencode.validators.String()



class PageController(BaseController):

    @authorize(ValidAuthKitUser())
    def __before__(self):
        ud = model.UserManager.getUserData(request.environ.get('REMOTE_USER'))
        if ud is not None:
            realms = ud.getAllRealms()
            allProjects = []
            realmNames=[]
            for realm in realms:
                projects = realm.getAllProjects('active')
                allProjects.extend(projects)
                realmNames.append([realm.id,realm.name])
            c.projects = sorted(allProjects, key = lambda x : x.name)
            c.realmNames = realmNames
            mainRealm = ud.getRealm()
            relevantProjects = []
            for project in mainRealm.getAllProjects(state='active',next=True):
                if project.name == 'next':
                    name = ''
                else:
                    name=project.name
                relevantProjects.append([project.id, name])
            c.relevantProjects = sorted(relevantProjects, key=lambda x: x[1])
            c.today = datetime.datetime.now()


    @restrict('GET')
    @authorize(ValidAuthKitUser())
    def getRelevantProjects(self):    
        ud = model.UserManager.getUserData(request.environ.get('REMOTE_USER'))
        relevantRealm = ud.getRealm(int(request.GET.get('realm_id','')))
        result=[]
        if relevantRealm is not None:
            for project in relevantRealm.getAllProjects(state='active', next=True):
                if project.name == 'next':
                    project.name = ''
                result.append([project.name, project.id])
            result = sorted(result, key=lambda x: x[0] )
            htmlResult = []
            for project in result:
                htmlResult.append(HTML.option(project[0], value=project[1]))
        return htmlResult
    
#    jen pro testovaci ucely
#    def adduser(self):
#        userData = model.UserData('lubson','Lubomir Hruban', 'l.hruban@gmail.com', None)
#        model.UserManager.addUser(userData,'alien')
#        realm1 = model.Realm(None,userData.login,'Work',True,None)
#        realm2 = model.Realm(None,userData.login,'Home',True,None)
#        userData.addRealm(realm1)
#        userData.addRealm(realm2)
#        project1 = model.Project(None,realm1.id, 'Udelat bakalarku',None,None,None,'active')
#        project2 = model.Project(None,realm1.id, 'Stat se is-technikem',None,None,None,'active')
#        project3 = model.Project(None,realm2.id, 'Nabrat svalovou hmotu',None,None,None,'active')
#        realm1.addProject(project1)
#        realm1.addProject(project2)
#        realm2.addProject(project3)
#        return 'Check db'

    @authorize(ValidAuthKitUser())
    def inbox(self):
        ud = model.UserManager.getUserData(request.environ.get('REMOTE_USER'))
        c.inboxes = ud.getAllInboxes()
        return render('/derived/page/inbox.html')

    @authorize(ValidAuthKitUser())
    def project(self,id=None):
        ud = model.UserManager.getUserData(request.environ.get('REMOTE_USER'))
        realms = ud.getAllRealms(show=True)
        if id is None:
            c.realms = realms
            return render('/derived/page/projects.html')
        for realm in realms:
            project = realm.getProject(id)
            if project is not None:
                break
        c.realmName = realm.name
        c.project = project
        return render('/derived/page/project.html')

    @authorize(ValidAuthKitUser())
    @restrict('POST')
    @validate(schema=NewInboxForm(), form='new')
    def createInbox(self):
        ud = model.UserManager.getUserData(request.environ.get('REMOTE_USER'))
        data = self.form_result.items()
        inbox = model.Inbox(content = data[0][1], created = data[1][1])
        ud.addInbox(inbox)
        # Issue an HTTP redirect
        response.status_int = 302
        response.headers['location'] = h.url_for(controller='page', action='inbox', id=None)
        return 'Moved temporarily'


    @authorize(ValidAuthKitUser())
    @restrict('POST')
    @validate(schema=NewProjectForm(), form='new')
    def saveProject(self):
        ud = model.UserManager.getUserData(request.environ.get('REMOTE_USER'))
        realm = ud.getRealm(int(request.POST.get('realm_id','')))
        if request.POST.get('id') == "":
            project = model.Project()
            for k, v in self.form_result.items():
                setattr(project, k, v)
            realm.addProject(project)
        else:
            for oldRealm in ud.getAllRealms(show=True):
                project = oldRealm.getProject(request.POST.get('id'))
                if project is not None:
                    break
            if oldRealm == realm:
                for k, v in self.form_result.items():
                    setattr(project, k, v)
                meta.Session.commit()
            else:
                oldRealm.removeProject(project)
                project = model.Project()
                for k, v in self.form_result.items():
                    setattr(project, k, v)
                realm.addProject(project)
        # Issue an HTTP redirect
        response.status_int = 302
        response.headers['location'] = h.url_for(controller='page',action='project', id=project.id)
        return 'Moved temporarily'

    @authorize(ValidAuthKitUser())
    @restrict('POST')
    @validate(schema=NewTaskForm(), form='new')
    def createTask(self):
        ud = model.UserManager.getUserData(request.environ.get('REMOTE_USER'))
        realm = ud.getRealm(int(request.POST.get('task_realm_id','')))
        project = realm.getProject(int(request.POST.get('relevantProjects')))
        data = self.form_result.items()
        task = model.Task()
        for k, v in self.form_result.items():
            if (k=='task_realm_id'):
                k='realm_id'
            if (k=='relevantProjects'):
                k='project_id'
            setattr(task, k, v)
        project.addTask(task)
        # Issue an HTTP redirect
        response.status_int = 302
        response.headers['location'] = h.url_for(controller='page',action='inbox')
        return 'Moved temporarily'

    @restrict('POST')
    @authorize(ValidAuthKitUser())
    def changeStateOfTask(self):
        ud = model.UserManager.getUserData(request.environ.get('REMOTE_USER'))
        realm = ud.getRealm(request.POST.get('realm_id',''))
        if realm is not None:
            project = realm.getProject(request.POST.get('project_id',''))
            if project is not None:
                task = project.getTask(request.POST.get('task_id',''))
                if task is not None:
                    task.state = request.POST.get('task_state','')
                    meta.Session.commit()
        response.status_int = 302
        response.headers['location'] = h.url_for(controller='page',action='project', id=request.POST.get('project_id',''))
        return 'Moved temporarily'

    @restrict('POST')
    @authorize(ValidAuthKitUser())
    def deleteInbox(self, id=None):
        if id is None:
            abort(404)
        ud = model.UserManager.getUserData(request.environ.get('REMOTE_USER'))
        inbox = ud.getInbox(id)
        ud.removeInbox(inbox)
        # Issue an HTTP redirect
        response.status_int = 302
        response.headers['location'] = h.url_for(controller='page',action='inbox', id=None )
        return 'Moved temporarily'

    @restrict('POST')
    @authorize(ValidAuthKitUser())
    def editInbox(self):
        ud = model.UserManager.getUserData(request.environ.get('REMOTE_USER'))
        inbox_id = request.POST.get('id','')
        new_content = request.POST.get('content','')
        inbox = ud.getInbox(int(inbox_id[6:]))
        inbox.content = new_content
        meta.Session.commit()
        return new_content

    @authorize(ValidAuthKitUser())
    def waiting(self):
        ud = model.UserManager.getUserData(request.environ.get('REMOTE_USER'))
        projects = []
        for realm in ud.getAllRealms(show=True):
            for project in realm.getAllProjects(state='active', next=True):
                for task in project.getAllTasks(state='waiting'):
                    projects.append(project)
                    break
        c.waiting = projects
        return render('/derived/page/waiting.html')

    @authorize(ValidAuthKitUser())
    def next(self):
        ud = model.UserManager.getUserData(request.environ.get('REMOTE_USER'))
        projects = []
        for realm in ud.getAllRealms(show=True):
            for project in realm.getAllProjects(state='active', next=True):
                for task in project.tasks:
                    if task.state == 'active' or task.state == 'waiting':
                        projects.append(project)
                        break
        c.next = projects
        return render('/derived/page/next.html')

    @authorize(ValidAuthKitUser())
    def scheduled(self):
        ud = model.UserManager.getUserData(request.environ.get('REMOTE_USER'))
        projects = []
        for realm in ud.getAllRealms(show=True):
            for project in realm.getAllProjects(state='active', next=True):
                for task in project.tasks:
                    if task.scheduled is not None and (task.state == 'active' or task.state == 'waiting'):
                        projects.append(project)
                        break
        c.scheduled = projects
        return render('/derived/page/scheduled.html')

    @authorize(ValidAuthKitUser())
    def today(self):
        ud = model.UserManager.getUserData(request.environ.get('REMOTE_USER'))
        projects = []
        for realm in ud.getAllRealms(show=True):
            for project in realm.getAllProjects(state='active', next=True):
                if l.isInToday(project.due) and project.state == 'active':
                    projects.append(project)
                else:
                    for task in project.tasks:
                        if (task.state == 'active' or task.state=='waiting') and (l.isInToday(task.due) or l.isInToday(task.scheduled)):
                            projects.append(project)
                            break
        c.today = projects
        return render('/derived/page/today.html')

    @restrict('GET')
    @authorize(ValidAuthKitUser())
    def show(self):
        ud = model.UserManager.getUserData(request.environ.get('REMOTE_USER'))
        c.specificTasks = ud.getSpecificTasks(request.GET.get('mode','inbox'))
        return render('/derived/page/show.html')
