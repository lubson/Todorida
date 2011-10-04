"""The application's model objects"""
from operator import and_
import sqlalchemy as sa
from sqlalchemy import orm, schema, types

import datetime

from mygtd.model import meta

from pylons import request

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    ## Reflected tables must be defined and mapped here
    #global reflected_table
    #reflected_table = sa.Table("Reflected", meta.metadata, autoload=True,
    #                           autoload_with=engine)
    #orm.mapper(Reflected, reflected_table)

    # We are using SQLAlchemy 0.5 so transactional=True is replaced by
    # autocommit=False
    sm = orm.sessionmaker(autoflush=True, autocommit=False, bind=engine)

    meta.engine = engine
    meta.Session = orm.scoped_session(sm)

def now():
    return datetime.datetime.now()

def isInToday(date):
    if date is not None and ((date - now()).days + 1) <= 0:
        return True
    else:
        return False

user_data_table = schema.Table('user_data', meta.metadata,
    schema.Column('login', types.String, primary_key=True),
    schema.Column('name', types.Unicode(255), default=u''),
    schema.Column('email', types.Unicode(255), default=u''),
    schema.Column('info', types.Text(), default=u''),
)

inbox_table = schema.Table('inbox', meta.metadata,
    schema.Column('id', types.Integer,
                  schema.Sequence('inbox_seq_id', optional=True), primary_key=True),
    schema.Column('user_login', types.String,
                  schema.ForeignKey('user_data.login'), nullable=False),
    schema.Column('content', types.Text(), default=u''),
    schema.Column('created', types.DATETIME, default=now()),
)

realm_table = schema.Table('realm', meta.metadata,
    schema.Column('id', types.Integer,
                  schema.Sequence('realm_seq_id', optional=True), primary_key=True),
    schema.Column('user_login', types.String,
                  schema.ForeignKey('user_data.login'), nullable=False),
    schema.Column('name', types.Unicode(255), default=u''),
    schema.Column('show', types.Boolean, default=True),
    schema.Column('created', types.TIMESTAMP(), default=now()),
)

project_table = schema.Table('project', meta.metadata,
    schema.Column('id', types.Integer,
                  schema.Sequence('project_seq_id', optional=True), primary_key=True),
    schema.Column('realm_id', types.Integer,
                  schema.ForeignKey('realm.id'), nullable=False),
    schema.Column('name', types.Unicode(255), default=u''),
    schema.Column('note', types.Text(), default=u''),
    schema.Column('scheduled', types.DateTime),
    schema.Column('due', types.DateTime),
    schema.Column('state', types.String, default='active')
)

task_table = schema.Table('task', meta.metadata,
    schema.Column('id', types.Integer,
                  schema.Sequence('task_seq_id', optional=True), primary_key=True),
    schema.Column('project_id', types.Integer,
                  schema.ForeignKey('project.id'), nullable=False),
    schema.Column('name', types.Unicode(255), default=u''),
    schema.Column('note', types.Text(), default=u''),
    schema.Column('scheduled', types.DateTime),
    schema.Column('due', types.DateTime),
    schema.Column('state', types.String, default=u'active')
)



class UserManager():
    @staticmethod
    def addUser(userData, pwd):
        #pridat kontrolu na login
        meta.Session.add(userData)
        users = request.environ['authkit.users']
        users.user_create(userData.login, pwd)
        meta.Session.commit()


    @staticmethod
    def getUserData(login):
        query = meta.Session.query(UserData)
        userData = query.filter(
                UserData.login == login).first()
        return userData

    #TODO tohle jeste nefunguje, mozna kvuli mapperum
    @staticmethod
    def removeUser(login):
        query = meta.Session.query(UserData)
        userData = query.filter(
                UserData.login == login).first()
        meta.Session.delete(userData)
        meta.Session.commit()
        #users = request.environ['authkit.users']
        #users.user_delete(login)

class UserData(object):

    def __init__(self, login, name, email, info):
        self.login = login
        self.name = name
        self.email = email
        self.info = info

    def getAllSums(self):
        sums ={}
        sums['inbox']= self.getAllInboxes(tickler=False).count()
        sums['tickler']= self.getAllInboxes(tickler=True).count()
        return sums

    def getSpecificTasks(self, mode):
        specificTasks = {'inboxCouple':[],'otherProjectsCouple':[]}
        realms = self.getAllRealms(show=True)
        for realm in realms:
            if mode == 'waiting':
                for inboxTask in realm.getProject().tasks:
                    if inboxTask.state == 'waiting':
                        specificTasks['inboxCouple'].append((inboxTask,realm.id))
                for project in realm.getAllProjects(state='active', next=False):
                    tasks = project.getAllTasks(state='waiting')
                    if  tasks != []:
                        projectCouple = [Project,[]]
                        projectCouple[0] = project
                        for task in tasks:
                            projectCouple[1].append(task.id)
                        specificTasks['otherProjectsCouple'].append(projectCouple)

            elif mode == 'today':
                for inboxTask in realm.getProject().tasks:
                    if (inboxTask.state == 'active' or inboxTask.state=='waiting') and \
                        (isInToday(inboxTask.scheduled) or isInToday(inboxTask.due)):
                        specificTasks['inboxCouple'].append((inboxTask,realm.id))
                for project in realm.getAllProjects(state='active', next=False):
                    wasAdded = False
                    for task in project.tasks:
                        if (isInToday(task.scheduled) or isInToday(task.due)) and \
                           (task.state == 'active' or task.state == 'waiting'):
                            if not wasAdded:
                                projectCouple = [Project,[]]
                                projectCouple[0] = project
                                wasAdded = True
                            projectCouple[1].append(task.id)
                    if wasAdded:
                        specificTasks['otherProjectsCouple'].append(projectCouple)


            elif mode == 'scheduled':
                for inboxTask in realm.getProject().tasks:
                    if inboxTask.scheduled is not None and (inboxTask.state == 'active' or inboxTask.state == 'waiting'):
                        specificTasks['inboxCouple'].append((inboxTask,realm.id))
                for project in realm.getAllProjects(state='active', next=False):
                    wasAdded = False
                    for task in project.tasks:
                        if task.scheduled is not None and (task.state == 'active' or task.state == 'waiting'):
                            if not wasAdded:
                                projectCouple = [Project,[]]
                                projectCouple[0] = project
                                wasAdded = True
                            projectCouple[1].append(task.id)
                    if wasAdded:
                        specificTasks['otherProjectsCouple'].append(projectCouple)
            else:
                for inboxTask in realm.getProject().tasks:
                    if inboxTask.state == 'active' or inboxTask.state == 'waiting':
                        specificTasks['inboxCouple'].append((inboxTask,realm.id))
                for project in realm.getAllProjects(state='active', next=False):
                    wasAdded = False
                    for task in project.tasks:
                        if task.state == 'active' or task.state == 'waiting':
                            if not wasAdded:
                                projectCouple = [Project,[]]
                                projectCouple[0] = project
                                wasAdded = True
                            projectCouple[1].append(task.id)
                    if wasAdded:
                        specificTasks['otherProjectsCouple'].append(projectCouple)
        return specificTasks


    def addInbox(self, inbox):
        self.inboxes.append(inbox)
        meta.Session.commit()

    def getInbox(self, inbox_id):
        query = meta.Session.query(Inbox)
        inbox = query.filter(sa.and_(
                Inbox.id == inbox_id, Inbox.user_login == self.login)).first()
        return inbox

    def getAllInboxes(self, tickler=False):
        query = meta.Session.query(Inbox)
        if tickler:
            inboxes = query.filter(sa.and_(
                Inbox.user_login == self.login, Inbox.created > now()))
        else:
            inboxes = query.filter(sa.and_(
                Inbox.user_login == self.login, Inbox.created <= now()))

        return inboxes.order_by(sa.desc(Inbox.created)).all()

    def removeInbox(self, inbox):
        meta.Session.delete(inbox)
        meta.Session.commit()

    def addRealm(self, realm):
        self.realms.append(realm)
        project = Project(None, realm.id, 'next', None, None, None, 'active')
        realm.projects.append(project)
        meta.Session.commit()

    def getRealm(self, realm_id = None):
        query = meta.Session.query(Realm)
        if realm_id is None:
            realm = query.filter(
                    Realm.user_login == self.login).order_by(sa.desc(Realm.created)).first()
        else:
            realm = query.filter(sa.and_(
                    Realm.id == realm_id, Realm.user_login == self.login)).first()
        return realm

    def getAllRealms(self, show = True):
        query = meta.Session.query(Realm)
        realms = query.filter(sa.and_(
                    Realm.user_login == self.login, Realm.show == show)).order_by(
                    sa.desc(Realm.created)).all()
        return realms

    def setDefaultRealm(self, realm):
        realm.created = now()
        meta.Session.commit()

    def removeRealm(self, realm):
        meta.Session.delete(realm)
        meta.Session.commit()


class Inbox(object):

    def  __init__(self, id=None, user_login=None, content=None, created=None):
        self.id = id
        self.user_login = user_login
        self.content = content
        self.created = created


class Realm(object):

    def  __init__(self, id, user_login, name, show, created):
        self.id = id
        self.user_login = user_login
        self.name = name
        self.show = show
        self.created = created

    def addProject(self,project):
        if project.name != 'next':
            self.projects.append(project)
            meta.Session.commit()

    def getProject(self, project_id = None):
        query = meta.Session.query(Project)
        if project_id is None:
            project = query.filter(sa.and_(
                    Project.realm_id == self.id, Project.name == 'next')).first()
        else:
            project = query.filter(sa.and_(
                    Project.realm_id == self.id, project_id == Project.id)).first()
        return project

    def getAllProjects(self, state=None, next=False):
        query = meta.Session.query(Project)
        if next:
            projects = query.filter(and_(
                        self.id == Project.realm_id, state == Project.state )).order_by(
                        sa.desc(Project.due)).all()
        else:
            projects = query.filter(and_(
                        self.id == Project.realm_id, and_(state == Project.state, 'next' != Project.name))).order_by(
                        sa.desc(Project.due)).all()
        return projects


    def removeProject(self, project):
        meta.Session.delete(project)
        meta.Session.commit()


class Project(object):

    def  __init__(self, id=None, realm_id=None, name=None, note=None, scheduled=None, due=None, state=None):
        self.id = id
        self.realm_id = realm_id
        self.name = name
        self.note = note
        self.scheduled = scheduled
        self.due = due
        self.state = state

    def addTask(self, task):
        self.tasks.append(task)
        meta.Session.commit()

    
    def getTask(self, task_id = None):
        query = meta.Session.query(Task)
        task = query.filter(sa.and_(
                    Task.project_id == self.id, Task.id == task_id)).first()
        return task

    def getAllTasks(self, state='active'):
        query = meta.Session.query(Task)
        tasks = query.filter(sa.and_(
                Task.project_id == self.id, Task.state == state)).all()
        return tasks

    def removeTask(self, task):
        meta.Session.delete(task)
        meta.Session.commit()
    #docasne pro testovani
    def printMe(self):
        return "Project: %s; %s; %s; %s;" %(self.name, self.note, self.state, self.scheduled)

    
class Task(object):

    def  __init__(self, id=None, task_id=None, name=None, note=None, scheduled=None, due=None, state=None):
        self.id = id
        self.task_id = task_id
        self.name = name
        self.note = note
        self.scheduled = scheduled
        self.due = due
        self.state = state


orm.mapper(UserData, user_data_table, properties={
        'inboxes': orm.relation(Inbox, backref='user_data', cascade='all, delete, delete-orphan'),
        'realms': orm.relation(Realm, backref='user_data', cascade='all, delete, delete-orphan'),
    }
)
orm.mapper(Inbox, inbox_table)
orm.mapper(Realm, realm_table, properties={
        'projects': orm.relation(Project, backref='realm', cascade='all, delete, delete-orphan'),
    }
)
orm.mapper(Project, project_table, properties={
        'tasks': orm.relation(Task, backref='project', cascade='all, delete, delete-orphan')
    }
)
orm.mapper(Task,task_table)