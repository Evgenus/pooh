from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1291324581.7349999
_template_filename='D:/Work/Research/__FUN__/POOH/pooh/source/pooh/2010/template.mako'
_template_uri='/pooh/2010/template.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = ['head']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml">\n<head>\n')
        # SOURCE LINE 5
        __M_writer(unicode(self.head()))
        __M_writer(u'\n')
        # SOURCE LINE 14
        __M_writer(u"\n</head>\n<body>\n<div class='header'>\n    <div class='holder'>\n        <div class='title'></div>\n    </div>\n</div>\n<div class='main'>\n    <div class='holder'>\n        <div class='content'>\n            <div class='menu'>\n                <div class='menu_body'>\n                    <div class='buttons'>\n                        <a href='index.html'><div class='button'></div></a>\n                        <a href='participants.html'><div class='button'></div></a>\n                        <a href='organizers.html'><div class='button'></div></a>\n                        <a href='programm.html'><div class='button'></div></a>\n                        <a href='video.html'><div class='button'></div></a>\n                        <a href='photo.html'><div class='button'></div></a>\n                        <a href='where.html'><div class='button'></div></a>\n                        <a href='contacts.html'><div class='button'></div></a>\n                        <a href='feedback.html'><div class='button'></div></a>\n                    </div>\n                <div class='menu_end'></div>\n                </div>\n            </div>\n        <div id='content'>")
        # SOURCE LINE 41
        __M_writer(unicode(self.body()))
        __M_writer(u"</div>\n        </div>\n    </div>\n</div>\n<div class='footer'>\n    <div class='holder'>\n        <div class='copyright'></div>\n    </div>\n</div>\n</body>\n</html>")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context):
    context.caller_stack._push_frame()
    try:
        PATH = context.get('PATH', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 6
        __M_writer(u'\n<title>\u041f\u0443\u0445 \u0438 \u0432\u0441\u0435-\u0432\u0441\u0435-\u0432\u0441\u0435</title>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n<title></title>\n<script type="text/javascript" src="')
        # SOURCE LINE 10
        __M_writer(unicode(PATH('/js/jquery.js')))
        __M_writer(u'"></script>\n<script type="text/javascript" src="')
        # SOURCE LINE 11
        __M_writer(unicode(PATH('/js/jquery.lightbox.js')))
        __M_writer(u'"></script>\n<link rel="stylesheet" type="text/css" href="')
        # SOURCE LINE 12
        __M_writer(unicode(PATH('/css/2010.css')))
        __M_writer(u'"/>\n<link rel="stylesheet" type="text/css" href="')
        # SOURCE LINE 13
        __M_writer(unicode(PATH('/css/jquery.lightbox.css')))
        __M_writer(u'"/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


