# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1311254593.9802489
_template_filename=u'/home/lubson/Plocha/myGTD/myGTD/mygtd/templates/derived/page/task_view.html'
_template_uri=u'/derived/page/task_view.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


# SOURCE LINE 2
import mygtd.lib.gtdlib as l

def render_body(context,task,realm_id,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,task=task,realm_id=realm_id)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n<div>\n    <h4>')
        # SOURCE LINE 5
        __M_writer(escape(task.name))
        __M_writer(u'</h4>\n    <span>\n')
        # SOURCE LINE 7
        if (task.state == 'active' or task.state == 'waiting'):
            # SOURCE LINE 8
            __M_writer(u'            <em>')
            __M_writer(escape(l.duePhrase(task.due)))
            __M_writer(u' </em>\n')
            pass
        # SOURCE LINE 10
        __M_writer(u'\n')
        # SOURCE LINE 11
        if ((task.state == 'active' or task.state == 'waiting') and task.scheduled is not None):
            # SOURCE LINE 12
            __M_writer(u'            <em>')
            __M_writer(escape(task.scheduled))
            __M_writer(u'</em>\n')
            pass
        # SOURCE LINE 14
        __M_writer(u'\n        <form action="')
        # SOURCE LINE 15
        __M_writer(escape((h.url_for(controller='page', action='changeStateOfTask'))))
        __M_writer(u'" method="post">\n            <input type="hidden" name="realm_id" value="')
        # SOURCE LINE 16
        __M_writer(escape(realm_id))
        __M_writer(u'"/>\n            <input type="hidden" name="project_id" value="')
        # SOURCE LINE 17
        __M_writer(escape(task.project_id))
        __M_writer(u'"/>\n            <input type="hidden" name="task_id" value="')
        # SOURCE LINE 18
        __M_writer(escape(task.id))
        __M_writer(u'"/>\n            <input type="hidden" name="task_state" value="archived"/>\n            <button type="submit">Complete</button>\n        </form>\n        <form action="')
        # SOURCE LINE 22
        __M_writer(escape((h.url_for(controller='page', action='changeStateOfTask'))))
        __M_writer(u'" method="post">\n            <input type="hidden" name="realm_id" value="')
        # SOURCE LINE 23
        __M_writer(escape(realm_id))
        __M_writer(u'"/>\n            <input type="hidden" name="project_id" value="')
        # SOURCE LINE 24
        __M_writer(escape(task.project_id))
        __M_writer(u'"/>\n            <input type="hidden" name="task_id" value="')
        # SOURCE LINE 25
        __M_writer(escape(task.id))
        __M_writer(u'"/>\n            <input type="hidden" name="task_state" value="removed"/>\n            <button type="submit">Delete</button>\n        </form>\n    </span>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


