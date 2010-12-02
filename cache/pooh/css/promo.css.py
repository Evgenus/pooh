from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1291324640.4230001
_template_filename='D:/Work/Research/__FUN__/POOH/pooh/source/pooh/css/promo.css'
_template_uri='/pooh/css/promo.css'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        PATH = context.get('PATH', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\nbody {\n    margin: 0px;\n    padding: 0px;\n}\n\n.header {\n    width:  100%;\n    height: 100%;\n    position: absolute;\n    top: 0px;\n    bottom: 0px;\n    left: 0px;\n    right: 0px;\n    background-color: black;\n}\n\n.holder {\n    top: 50%;\n    left: 50%;\n    width: 1px;\n    height: 1px;\n    position: relative;\n}\n\n.holder > div {\n    height: 600px;\n    width: 800px;\n    left: -400px;\n    top: -300px;\n    position: absolute;\n    background-repeat: no-repeat;\n}\n\n#back_null {\n    background-image: url(')
        # SOURCE LINE 36
        __M_writer(unicode(PATH('/images/back_null.png')))
        __M_writer(u');\n}\n\n#back_2010 {\n    background-image: url(')
        # SOURCE LINE 40
        __M_writer(unicode(PATH('/images/back_2010.png')))
        __M_writer(u');\n    display: none;\n}\n\n#back_2011 {\n    background-image: url(')
        # SOURCE LINE 45
        __M_writer(unicode(PATH('/images/back_2011.png')))
        __M_writer(u');\n    display: none;\n}\n\n.fore {\n    background-image: url(')
        # SOURCE LINE 50
        __M_writer(unicode(PATH('/images/back_mask.png')))
        __M_writer(u');\n}\n\n#a2010 {\n    width: 126px;\n    height: 33px;\n    left: 180px;\n    top: 500px;\n    position: absolute;\n    cursor: pointer;\n    background-image: url(')
        # SOURCE LINE 60
        __M_writer(unicode(PATH('/images/2010.png')))
        __M_writer(u');\n}\n\n#a2011 {\n    width: 126px;\n    height: 33px;\n    left: 500px;\n    top: 500px;\n    position: absolute;\n    background-image: url(')
        # SOURCE LINE 69
        __M_writer(unicode(PATH('/images/2011.png')))
        __M_writer(u');\n}\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


