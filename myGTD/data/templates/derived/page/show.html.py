# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1317549336.8246541
_template_filename='/home/lubson/Plocha/myGTD/myGTD/mygtd/templates/derived/page/show.html'
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
    # SOURCE LINE 7
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
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n<div>\n\n')
        # SOURCE LINE 5
        for inboxTask in c.specificTasks['inbox']:
            # SOURCE LINE 6
            __M_writer(u'<li>\n    ')
            # SOURCE LINE 7
            __M_writer(u'\n    ')
            # SOURCE LINE 8
            __M_writer(escape(taskView.body(inboxTask,1)))
            __M_writer(u'\n</li>\n')
            pass
        # SOURCE LINE 11
        __M_writer(u'<br/>\n')
        # SOURCE LINE 12
        for projectCouple in c.specificTasks['otherProjects']:
            # SOURCE LINE 13
            __M_writer(u'    ')
            __M_writer(escape(projectCouple[0].name))
            __M_writer(u'\n    ')
            # SOURCE LINE 14
            __M_writer(escape(projectCouple[1][0]))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 16
        __M_writer(u'\n\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


