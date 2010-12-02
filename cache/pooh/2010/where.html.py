from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1291324640.095
_template_filename='D:/Work/Research/__FUN__/POOH/pooh/source/pooh/2010/where.html'
_template_uri='/pooh/2010/where.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
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
    return runtime._inherit_from(context, 'template.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        PATH = context.get('PATH', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n<div>\n    <h2>\u0412\u0440\u0435\u043c\u044f \u0438 \u043c\u0435\u0441\u0442\u043e \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f:</h2>\n    <p class="par">19 \u0434\u0435\u043a\u0430\u0431\u0440\u044f 2009 \u0433., 19:00-22:00</p>\n    \u0411\u043e\u043b\u044c\u0448\u043e\u0439 \u043a\u043e\u043d\u0444\u0435\u0440\u0435\u043d\u0446-\u0437\u0430\u043b \u0433\u043e\u0441\u0442\u0438\u043d\u0438\u0446\u044b \xab\u0422\u0443\u0440\u0438\u0441\u0442\xbb\n    <br>\n    (100 \u043c \u043e\u0442 \u043c. \xab\u041b\u0435\u0432\u043e\u0431\u0435\u0440\u0435\u0436\u043d\u0430\u044f\xbb, \u0443\u043b. \u0420. \u041e\u043a\u0438\u043f\u043d\u043e\u0439 2).\n    <br>\n    <img class="invite_way" src="')
        # SOURCE LINE 9
        __M_writer(unicode(PATH('/images/2010/invite_back.jpg')))
        __M_writer(u'">\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


