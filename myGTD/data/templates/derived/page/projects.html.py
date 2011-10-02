# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1309197934.3538201
_template_filename='/home/lubson/Plocha/myGTD/myGTD/mygtd/templates/derived/page/projects.html'
_template_uri='/derived/page/projects.html'
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
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base/index.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n<div id="projects">\n\n\n')
        # SOURCE LINE 5
        for realm in c.realms:
            # SOURCE LINE 6
            __M_writer(u'    <h3>')
            __M_writer(escape(realm.name))
            __M_writer(u'</h3>\n')
            # SOURCE LINE 7

            activeProjects = realm.getAllProjects(state='active')
            somedayProjects = realm.getAllProjects(state='someday')
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['activeProjects','somedayProjects'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 10
            __M_writer(u'\n\n')
            # SOURCE LINE 12
            if len(activeProjects) > 0 :
                # SOURCE LINE 13
                __M_writer(u'        <h4>Active <span>')
                __M_writer(escape(len(activeProjects)))
                __M_writer(u'</span></h4>\n')
                pass
            # SOURCE LINE 15
            for project in activeProjects:
                # SOURCE LINE 16
                __M_writer(u'        <ul>\n            <li>\n                <a href="')
                # SOURCE LINE 18
                __M_writer(escape((h.url_for(controller='page', action='project', id=project.id))))
                __M_writer(u'">')
                __M_writer(escape(project.name))
                __M_writer(u'</a>\n            </li>\n        </ul>\n')
                pass
            # SOURCE LINE 22
            __M_writer(u'\n\n')
            # SOURCE LINE 24
            if len(somedayProjects) > 0:
                # SOURCE LINE 25
                __M_writer(u'        <h4>Someday <span>')
                __M_writer(escape(len(somedayProjects)))
                __M_writer(u'</span></h4>\n')
                pass
            # SOURCE LINE 27
            for project in somedayProjects:
                # SOURCE LINE 28
                __M_writer(u'        <ul>\n            <li>\n                <a href="')
                # SOURCE LINE 30
                __M_writer(escape((h.url_for(controller='page', action='project', id=project.id))))
                __M_writer(u'">')
                __M_writer(escape(project.name))
                __M_writer(u'</a>\n            </li>\n        </ul>\n')
                pass
            pass
        # SOURCE LINE 35
        __M_writer(u'</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


