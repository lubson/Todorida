# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1313002163.5353889
_template_filename=u'/home/lubson/Plocha/myGTD/myGTD/mygtd/templates/derived/page/inbox_fields.html'
_template_uri=u'/derived/page/inbox_fields.html'
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
        __M_writer(u'<form action="/page/createInbox" method="post">\n    <div>\n        <input id="content" name="content" type="text" />\n    </div>\n\n    <div class="datefield">\n        <input id="dateInbox" name="created" type="text" value="" />\n        <button id="showDateInbox" title="Show Calendar" type="button">\n            <img alt="Calendar" height="18" src="/yui/2.9.0/assets/calbtn.gif" width="18" />\n        </button>\n    </div>\n    <div>\n        <input id="submit" name="submit" type="submit" value="Add" />\n    </div>\n</form>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


