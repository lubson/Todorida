# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1311259503.8301129
_template_filename='/home/lubson/Plocha/myGTD/myGTD/mygtd/templates/derived/page/scheduled.html'
_template_uri='/derived/page/scheduled.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 25
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
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n<div id="scheduled">\n')
        # SOURCE LINE 3
        for project in c.scheduled:
            # SOURCE LINE 4
            if project.name == 'next':
                # SOURCE LINE 5
                __M_writer(u'        <ul>\n')
                # SOURCE LINE 6
                for task in project.tasks:
                    # SOURCE LINE 7
                    if task.scheduled is not None and (task.state == 'active' or task.state == 'waiting'):
                        # SOURCE LINE 8
                        __M_writer(u'                    <li>\n                        ')
                        # SOURCE LINE 9
                        __M_writer(u'\n                        ')
                        # SOURCE LINE 10
                        __M_writer(escape(taskView.body(task, project.realm_id)))
                        __M_writer(u'\n                    </li>\n')
                        pass
                    pass
                # SOURCE LINE 14
                __M_writer(u'        </ul>\n')
                pass
            pass
        # SOURCE LINE 17
        __M_writer(u'\n')
        # SOURCE LINE 18
        for project in c.scheduled:
            # SOURCE LINE 19
            if project.name != 'next':
                # SOURCE LINE 20
                __M_writer(u'        <a href="')
                __M_writer(escape((h.url_for(controller='page', action='project', id=project.id))))
                __M_writer(u'" ><h3>')
                __M_writer(escape(project.name))
                __M_writer(u'</h3></a>\n        <ul>\n')
                # SOURCE LINE 22
                for task in project.tasks:
                    # SOURCE LINE 23
                    if task.scheduled is not None and (task.state == 'active' or task.state == 'waiting'):
                        # SOURCE LINE 24
                        __M_writer(u'                    <li>\n                        ')
                        # SOURCE LINE 25
                        __M_writer(u'\n                        ')
                        # SOURCE LINE 26
                        __M_writer(escape(taskView.body(task, project.realm_id)))
                        __M_writer(u'\n                    </li>\n')
                        pass
                    pass
                # SOURCE LINE 30
                __M_writer(u'        </ul>\n')
                pass
            pass
        # SOURCE LINE 33
        __M_writer(u'</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


