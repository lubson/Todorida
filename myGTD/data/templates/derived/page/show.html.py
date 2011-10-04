# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1317740186.6316831
_template_filename='/home/lubson/Plocha/todorida/myGTD/mygtd/templates/derived/page/show.html'
_template_uri='/derived/page/show.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


# SOURCE LINE 2
import mygtd.lib.gtdlib as l

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
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n<div>\n\n')
        # SOURCE LINE 5
        for couple in c.specificTasks['inboxCouple']:
            # SOURCE LINE 6

            task = couple[0]
            realm_id = couple[1]
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['task','realm_id'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 9
            __M_writer(u'\n<li>\n    ')
            # SOURCE LINE 11
            __M_writer(u'\n    ')
            # SOURCE LINE 12
            __M_writer(escape(taskView.body(task,realm_id)))
            __M_writer(u'\n</li>\n')
            pass
        # SOURCE LINE 15
        __M_writer(u'<br/>\n')
        # SOURCE LINE 16
        for couple in c.specificTasks['otherProjectsCouple']:
            # SOURCE LINE 17

            project = couple[0]
            selectedIds = couple[1]
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['project','selectedIds'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 20
            __M_writer(u'\n    <a href="')
            # SOURCE LINE 21
            __M_writer(escape((h.url_for(controller='page', action='project', id=project.id))))
            __M_writer(u'" ><h3>')
            __M_writer(escape(project.name))
            __M_writer(u'</h3></a>\n        <ul>\n')
            # SOURCE LINE 23
            for task_id in selectedIds:
                # SOURCE LINE 24
                __M_writer(u'                  <li>\n                      ')
                # SOURCE LINE 25
                __M_writer(u'\n                      ')
                # SOURCE LINE 26
                __M_writer(escape(taskView.body(project.getTask(task_id), project.realm_id)))
                __M_writer(u'\n                  </li>\n')
                pass
            # SOURCE LINE 29
            __M_writer(u'        </ul>\n')
            pass
        # SOURCE LINE 31
        __M_writer(u'\n\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


