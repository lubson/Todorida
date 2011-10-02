# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1311256172.3364789
_template_filename='/home/lubson/Plocha/myGTD/myGTD/mygtd/templates/derived/page/project.html'
_template_uri='/derived/page/project.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['duePhrase']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 51
    ns = runtime.Namespace(u'taskView', context._clean_inheritance_tokens(), templateuri=u'/derived/page/task_view.html', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, u'taskView')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base/index.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'taskView')._populate(_import_ns, [u'*'])
        taskView = _mako_get_namespace(context, 'taskView')
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        def duePhrase(date):
            return render_duePhrase(context.locals_(__M_locals),date)
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n<div project="project_')
        # SOURCE LINE 2
        __M_writer(escape(c.project.id))
        __M_writer(u'">\n    <div class="project_header">\n        <a onclick="fillProjectForm(\'')
        # SOURCE LINE 4
        __M_writer(escape(c.project.id))
        __M_writer(u"', '")
        __M_writer(escape(c.project.name))
        __M_writer(u"', '")
        __M_writer(escape(c.project.note))
        __M_writer(u"','")
        __M_writer(escape(c.project.due))
        __M_writer(u"','")
        __M_writer(escape(c.project.realm_id))
        __M_writer(u"','")
        __M_writer(escape(c.project.state))
        __M_writer(u'\')"><h3>')
        __M_writer(escape(c.project.name))
        __M_writer(u'</h3><i>')
        __M_writer(escape(c.realmName))
        __M_writer(u"</i></a>\n    </div>\n<!--\nPSEUDOFORMAT DATETIME (dolar je nahrazen #)\n'#{c.project.scheduled.day}-#{c.project.scheduled.month}-#{c.project.scheduled.year}', '#{c.project.due.day}-#{c.project.due.month}-#{c.project.due.year}\n-->\n")
        # SOURCE LINE 25
        __M_writer(u'\n\n')
        # SOURCE LINE 27

        state = {}
        state['active'], state['waiting'], state['someday'], state['completed'] = [], [], [], []
        for task in c.project.tasks:
            if task.state == 'active':
                state['active'].append(task)
            elif task.state == 'waiting':
                state['waiting'].append(task)
            elif task.state == 'someday':
                state['someday'].append(task)
            elif task.state == 'archived':
                state['completed'].append(task)
        
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['state','task'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 40
        __M_writer(u'\n    <div class="project_content">\n')
        # SOURCE LINE 42
        if (c.project.due is not None):
            # SOURCE LINE 43
            __M_writer(u'        <p>')
            __M_writer(escape(duePhrase(c.project.due)))
            __M_writer(u'</p>\n')
            pass
        # SOURCE LINE 45
        for category in state:
            # SOURCE LINE 46
            if len(state[category])>0:
                # SOURCE LINE 47
                __M_writer(u'            <h4>')
                __M_writer(escape(category.capitalize()))
                __M_writer(u'</h4>\n            <ul>\n')
                # SOURCE LINE 49
                for task in state[category]:
                    # SOURCE LINE 50
                    __M_writer(u'                <li>\n                      ')
                    # SOURCE LINE 51
                    __M_writer(u'\n                      ')
                    # SOURCE LINE 52
                    __M_writer(escape(taskView.body(task, c.project.realm_id)))
                    __M_writer(u'\n                </li>\n')
                    pass
                # SOURCE LINE 55
                __M_writer(u'            </ul>\n')
                pass
            pass
        # SOURCE LINE 58
        __M_writer(u'    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_duePhrase(context,date):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'taskView')._populate(_import_ns, [u'*'])
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        str = _import_ns.get('str', context.get('str', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 10
        __M_writer(u'\n')
        # SOURCE LINE 11
        if date is not None:
            # SOURCE LINE 12
            __M_writer(u'        ')
            deltaDue = (date - c.today).days + 1
            
            __M_writer(u'\n')
            # SOURCE LINE 13
            if deltaDue > 1:
                # SOURCE LINE 14
                __M_writer(u'            ')
                __M_writer(escape('Due in ' + str(deltaDue) + ' days'))
                __M_writer(u'\n')
                # SOURCE LINE 15
            elif deltaDue == 1:
                # SOURCE LINE 16
                __M_writer(u'            ')
                __M_writer(escape('Tomorrow'))
                __M_writer(u'\n')
                # SOURCE LINE 17
            elif deltaDue == 0:
                # SOURCE LINE 18
                __M_writer(u'            ')
                __M_writer(escape('Today'))
                __M_writer(u'\n')
                # SOURCE LINE 19
            elif deltaDue == -1:
                # SOURCE LINE 20
                __M_writer(u'            ')
                __M_writer(escape('Yesterday'))
                __M_writer(u'\n')
                # SOURCE LINE 21
            else:
                # SOURCE LINE 22
                __M_writer(u'            ')
                __M_writer(escape(str((-1)*deltaDue) + ' days late'))
                __M_writer(u'\n')
                pass
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


