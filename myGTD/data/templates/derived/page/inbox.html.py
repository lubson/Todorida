# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1312121617.4212461
_template_filename='/home/lubson/Plocha/myGTD/myGTD/mygtd/templates/derived/page/inbox.html'
_template_uri='/derived/page/inbox.html'
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
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n<ul id="editInPlace">\n')
        # SOURCE LINE 3
        for inbox in c.inboxes:
            # SOURCE LINE 4
            __M_writer(u'    <li>\n        <span>')
            # SOURCE LINE 5
            __M_writer(escape(inbox.created))
            __M_writer(u'</span>\n        <p id="inbox_')
            # SOURCE LINE 6
            __M_writer(escape(inbox.id))
            __M_writer(u'" class="edit">')
            __M_writer(escape(inbox.content))
            __M_writer(u'</p>\n        ')
            # SOURCE LINE 7
            __M_writer(escape(h.form_start(h.url_for(controller='page', action='deleteInbox', id=inbox.id), method="post")))
            __M_writer(u'\n        ')
            # SOURCE LINE 8
            __M_writer(escape(h.field(field=h.submit(value="Delete", name='submit', id=None))))
            __M_writer(u'\n        ')
            # SOURCE LINE 9
            __M_writer(escape(h.form_end()))
            __M_writer(u'\n    </li>\n')
            pass
        # SOURCE LINE 12
        __M_writer(u'</ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


