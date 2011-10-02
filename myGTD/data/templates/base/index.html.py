# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1313002026.5471549
_template_filename=u'/home/lubson/Plocha/myGTD/myGTD/mygtd/templates/base/index.html'
_template_uri=u'/base/index.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['head', 'footer', 'menu', 'title', 'header', 'heading']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 57
    ns = runtime.Namespace(u'projectFields', context._clean_inheritance_tokens(), templateuri=u'/derived/page/project_fields.html', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, u'projectFields')] = ns

    # SOURCE LINE 50
    ns = runtime.Namespace(u'taskFields', context._clean_inheritance_tokens(), templateuri=u'/derived/page/task_fields.html', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, u'taskFields')] = ns

    # SOURCE LINE 64
    ns = runtime.Namespace(u'fields', context._clean_inheritance_tokens(), templateuri=u'/derived/page/inbox_fields.html', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, u'fields')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'projectFields')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'taskFields')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'fields')._populate(_import_ns, [u'*'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        next = _import_ns.get('next', context.get('next', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'<?xml version="1.0" encoding="utf-8" ?>\n<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="cs" lang="cs">\n\n    <head>\n        <title>')
        # SOURCE LINE 7
        __M_writer(escape(self.title()))
        __M_writer(u'</title>\n        ')
        # SOURCE LINE 8
        __M_writer(escape(self.head()))
        __M_writer(u"\n    </head>\n    <body class='yui-skin-sam'>\n        <div>\n            ")
        # SOURCE LINE 12
        __M_writer(escape(self.header()))
        __M_writer(u'\n            ')
        # SOURCE LINE 13
        __M_writer(escape(self.menu()))
        __M_writer(u'\n            ')
        # SOURCE LINE 14
        __M_writer(escape(next.body()))
        __M_writer(u'\n            ')
        # SOURCE LINE 15
        __M_writer(escape(self.footer()))
        __M_writer(u'\n        </div>\n    </body>\n</html>\n\n')
        # SOURCE LINE 20
        __M_writer(u'\n\n')
        # SOURCE LINE 42
        __M_writer(u'\n\n')
        # SOURCE LINE 67
        __M_writer(u'\n\n')
        # SOURCE LINE 94
        __M_writer(u'\n\n<!--')
        # SOURCE LINE 96
        __M_writer(u'-->\n\n')
        # SOURCE LINE 102
        __M_writer(u'\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'projectFields')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'taskFields')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'fields')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n     <script src="/scripts/prototype.js" type="text/javascript"></script>\n     <script src="/scripts/editinplace.js" type="text/javascript"></script>\n     ')
        # SOURCE LINE 25
        __M_writer(escape(h.stylesheet_link(h.url_for('/css/editinplace.css'))))
        __M_writer(u'\n    <link rel="stylesheet" type="text/css" href="/yui/2.9.0/assets/skins/sam/skin.css"/>\n    <!--muj kalendar css\n    <link rel="stylesheet" type="text/css" href="/css/calendar.css" />-->\n    <script type="text/javascript" src="/yui/2.9.0/yahoo-dom-event/yahoo-dom-event.js"></script>\n    <script type="text/javascript" src="/yui/2.9.0/dragdrop/dragdrop-min.js"></script>\n    <script type="text/javascript" src="/yui/2.9.0/element/element-min.js"></script>\n    <script type="text/javascript" src="/yui/2.9.0/button/button-min.js"></script>\n    <script type="text/javascript" src="/yui/2.9.0/container/container-min.js"></script>\n    <script type="text/javascript" src="/yui/2.9.0/calendar/calendar-min.js"></script>\n    <!--muj kalendar script-->\n    <script type="text/javascript" src="/scripts/calendar.js"></script>\n    <script type="text/javascript" src="/scripts/popupforms.js"></script>\n    <script type="text/javascript" src="/yui/2.9.0/yahoo-dom-event/yahoo-dom-event.js"></script>\n    <script type="text/javascript" src = "/yui/2.9.0/connection/connection-min.js"></script>\n    <script type="text/javascript" src="/scripts/select.js"></script>\n    <script type="text/javascript" src="/scripts/editproject.js"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'projectFields')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'taskFields')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'fields')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        # SOURCE LINE 98
        __M_writer(u'\n    <div id="footer">\n        <p><a href="#top">Top ^</a></p>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'projectFields')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'taskFields')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'fields')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 69
        __M_writer(u'\n    <div id="menu">\n \n        <ul>\n            <li><a href="')
        # SOURCE LINE 73
        __M_writer(escape(h.url_for(controller='page', action='inbox', id=None)))
        __M_writer(u'">Inbox</a></li>\n            <li><a href="')
        # SOURCE LINE 74
        __M_writer(escape(h.url_for(controller='page', action='today')))
        __M_writer(u'">Today</a></li>\n            <li><a href="')
        # SOURCE LINE 75
        __M_writer(escape(h.url_for(controller='page', action='next')))
        __M_writer(u'">Next</a></li>\n            <li><a href="')
        # SOURCE LINE 76
        __M_writer(escape(h.url_for(controller='page', action='scheduled')))
        __M_writer(u'">Scheduled</a></li>\n            <li><a href="')
        # SOURCE LINE 77
        __M_writer(escape(h.url_for(controller='page', action='waiting')))
        __M_writer(u'">Waiting</a></li>\n            <li><a href="')
        # SOURCE LINE 78
        __M_writer(escape(h.url_for(controller='page', action='project', id=None)))
        __M_writer(u'">Projects</a> <a href="show"><img src="" alt=""/></a>\n                <ul>\n')
        # SOURCE LINE 80
        for project in c.projects:
            # SOURCE LINE 81
            __M_writer(u'                    <li>\n                     <a href="')
            # SOURCE LINE 82
            __M_writer(escape(h.url_for(controller='page', action='project', id=project.id)))
            __M_writer(u'">')
            __M_writer(escape(project.name))
            __M_writer(u'</a>\n                    </li>\n')
            pass
        # SOURCE LINE 85
        __M_writer(u'                </ul>\n            </li>\n            <li><a href="')
        # SOURCE LINE 87
        __M_writer(escape(h.url_for(controller='page', action='someday')))
        __M_writer(u'">Someday</a></li>\n            <li><a href="')
        # SOURCE LINE 88
        __M_writer(escape(h.url_for(controller='page', action='context')))
        __M_writer(u'">Context</a></li>\n            <li><a href="')
        # SOURCE LINE 89
        __M_writer(escape(h.url_for(controller='page', action='contact')))
        __M_writer(u'">Contact</a></li>\n            <li><a href="')
        # SOURCE LINE 90
        __M_writer(escape(h.url_for(controller='page', action='archive')))
        __M_writer(u'">Archive</a></li>\n            <li><a href="')
        # SOURCE LINE 91
        __M_writer(escape(h.url_for(controller='page', action='trash')))
        __M_writer(u'">Trash</a></li>\n        </ul>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'projectFields')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'taskFields')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'fields')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        # SOURCE LINE 20
        __M_writer(u'myGTD')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'projectFields')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'taskFields')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'fields')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        fields = _mako_get_namespace(context, 'fields')
        taskFields = _mako_get_namespace(context, 'taskFields')
        projectFields = _mako_get_namespace(context, 'projectFields')
        __M_writer = context.writer()
        # SOURCE LINE 44
        __M_writer(u'\n\n    <div id="header">\n        <div id="horMenu">\n            <button id="showTaskForm">New Task</button>\n            <div id="taskForm" style="visibility:hidden;">\n                ')
        # SOURCE LINE 50
        __M_writer(u'\n                ')
        # SOURCE LINE 51
        __M_writer(escape(taskFields.body()))
        __M_writer(u'\n            </div>\n            <!--<button id="showProjectForm" onclick="')
        # SOURCE LINE 53
        __M_writer(escape("fetchForm('%s', 'realm', 'projectForm'); return false;"%(
        h.url_for(controller="page", action="projectForm"))))
        # SOURCE LINE 54
        __M_writer(u'">New Project</button>-->\n            <button id="showProjectForm">New Project</button>\n            <div id="projectForm" style="visibility:hidden;">\n                ')
        # SOURCE LINE 57
        __M_writer(u'\n                ')
        # SOURCE LINE 58
        __M_writer(escape(projectFields.body()))
        __M_writer(u'\n            </div>\n\n            <a href="')
        # SOURCE LINE 61
        __M_writer(escape(h.url_for('signout')))
        __M_writer(u'">Log out</a>\n        </div>\n\n        ')
        # SOURCE LINE 64
        __M_writer(u'\n        ')
        # SOURCE LINE 65
        __M_writer(escape(fields.body()))
        __M_writer(u'\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'projectFields')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'taskFields')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'fields')._populate(_import_ns, [u'*'])
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 96
        __M_writer(u'<h1>')
        __M_writer(escape(c.heading or 'No Title'))
        __M_writer(u'</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()


