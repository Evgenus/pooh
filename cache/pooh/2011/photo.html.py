from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1291415360.5209999
_template_filename='D:/Work/Distributives/pooh/source/pooh/2011/photo.html'
_template_uri='/pooh/2011/photo.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = ['page_id']


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
    return runtime._inherit_from(context, 'template.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        PATH = context.get('PATH', UNDEFINED)
        range = context.get('range', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n<div style="padding:40px 0px 20px 25px">\n')
        # SOURCE LINE 4
        for num in range(1, 60):
            # SOURCE LINE 5
            __M_writer(u'<a class="gall" style="float:left" href="')
            __M_writer(unicode(PATH('/images/2011/photo/{0:02d}.jpg'.format(num))))
            __M_writer(u'"><img src="')
            __M_writer(unicode(PATH('/images/2011/photo/thumbnails/{0:02d}.jpg'.format(num))))
            __M_writer(u'"/></a>\n')
        # SOURCE LINE 7
        __M_writer(u'<p style="clear:left"></p>\n\n<script>\n$(\'a.gall\').lightBox();\n</script>\n\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_id(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'photo')
        return ''
    finally:
        context.caller_stack._pop_frame()


