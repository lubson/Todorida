# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1313001678.3606069
_template_filename=u'/home/lubson/Plocha/myGTD/myGTD/mygtd/templates/derived/page/project_fields.html'
_template_uri=u'/derived/page/project_fields.html'
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
        __M_writer(u'<form action="/page/saveProject" method="post">\n    <div>\n        <input name="id" type="hidden"/>\n    </div>\n\n    <div>\n        <input name="name" type="text"/>\n    </div>\n\n    <div>\n        <textarea cols="30" rows="8" name="note"></textarea>\n    </div>\n\n    <div>\n        <input name="tags" type="text"/>\n    </div>\n\n    <div class="datefield">\n        <input id="dateProjectDue" name="due" type="text" value=""/>\n        <button id="showDateProjectDue" title="Show Calendar" type="button">\n            <img alt="Calendar" height="18" src="/yui/2.9.0/assets/calbtn.gif" width="18"/>\n        </button>\n    </div>\n\n    <div>\n        <select id="realm_id" name="realm_id">\n            <option value="1">Work</option>\n            <option value="2">Home</option>\n        </select>\n    </div>\n\n    <div>\n        <select name="state">\n            <option value="active">Active</option>\n            <option value="someday">Someday</option>\n            <option value="archived">Archived</option>\n        </select>\n    </div>\n\n    <div><button>Save</button></div>\n\n    <div><button id="hideProjectForm" title="Close form" type="reset">Cancel</button></div>\n</form>')
        return ''
    finally:
        context.caller_stack._pop_frame()


