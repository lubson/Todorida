# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1313060635.056442
_template_filename=u'/home/lubson/Plocha/myGTD/myGTD/mygtd/templates/derived/page/task_fields.html'
_template_uri=u'/derived/page/task_fields.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<form action="/page/createTask" method="post">\n    <div>\n        <input name="name" type="text"/>\n    </div>\n\n\n    <div>\n        <textarea name="note" cols="30" rows="8"></textarea>\n\n        <select id="task_realm_id" name="task_realm_id" onchange="callAjax(\'/page/getRelevantProjects\', \'realm\', \'relevantProjects\'); return false;">\n            <option value="1">Work</option>\n            <option value="2">Home</option>\n        </select>\n\n       <select id="relevantProjects" name="relevantProjects">\n            <option value="1"></option>\n            <option value="21">Aloha</option>\n            <option value="20">Delay</option>\n            <option value="12">Due Today</option>\n            <option value="39">Jen tak</option>\n            <option value="11">Project s due</option>\n            <option value="4">Stat se is-technikem</option>\n        </select>\n\n        <select name="state">\n            <option value="active">Active</option>\n            <option value="waiting">Waiting</option>\n            <option value="someday">Someday</option>\n            <option value="archived">Archived</option>\n        </select>\n    </div>\n\n    <div>\n        <input name="tags" type="text"/>\n    </div>\n\n    <div class="datefield">\n        <input id="dateTaskScheduled" name="due" type="text" value=""/>\n        <button id="showDateTaskScheduled" title="Show Calendar" type="button">\n            <img alt="Calendar" height="18" width="18" src="/yui/2.9.0/assets/calbtn.gif"/>\n        </button>\n    </div>\n\n    <div class="datefield">\n        <input id="dateTaskDue" name="due" type="text" value=""/>\n        <button id="showDateTaskDue" title="Show Calendar" type="button">\n            <img alt="Calendar" height="18" width="18" src="/yui/2.9.0/assets/calbtn.gif"/>\n        </button>\n    </div>\n\n    \n    <div>\n        <button>Save</button>\n        <button id="hideTaskForm" title="Close form" type="reset">Cancel</button>\n    </div>\n</form>')
        return ''
    finally:
        context.caller_stack._pop_frame()


