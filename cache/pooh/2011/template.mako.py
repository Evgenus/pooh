from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1292100780.73
_template_filename='D:/Work/Distributives/pooh/source/pooh/2011/template.mako'
_template_uri='/pooh/2011/template.mako'
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
        # SOURCE LINE 13
        __M_writer(u"\n</head>\n<body>\n<div class='main'>\n    <div class='holder'>\n        <div class='head'></div>\n        <div class='buttons at_")
        # SOURCE LINE 19
        __M_writer(unicode(self.page_id()))
        __M_writer(u"'>\n                   <span class='btn_main_head'>\n            </span><span class='btn_main'>\n            </span><span class='btn_prog'>\n            </span><span class='btn_video'>\n            </span><span class='btn_photo'>\n            </span><span class='btn_where'>\n            </span><span class='btn_cont'>\n            </span><span class='btn_cont_tail'>\n            </span>\n            <div class='links'>\n                       <a href='index.html'><span class='link_main'>\n                    \u0413\u043b\u0430\u0432\u043d\u0430\u044f\n                </span></a><a href='programm.html'><span class='link_prog'>\n                    \u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430\n                </span></a><span class='link_video'>\n                    \u0412\u0438\u0434\u0435\u043e\n                </span><a href='photo.html'><span class='link_photo'>\n                    \u0424\u043e\u0442\u043e\n                </span></a><a href='where.html'><span class='link_where'>\n                    \u041a\u0430\u043a \u0434\u043e\u0431\u0440\u0430\u0442\u044c\u0441\u044f?\n                </span></a><a href='contacts.html'><span class='link_cont'>\n                    \u041a\u043e\u043d\u0442\u0430\u043a\u0442\u044b\n                </span></a>\n            </div>\n        </div>\n        <div id='content'>")
        # SOURCE LINE 45
        __M_writer(unicode(self.body()))
        __M_writer(u"</div>\n        <div class='footer'></div>\n    </div>\n</div>\n</body>\n</html>")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context):
    context.caller_stack._push_frame()
    try:
        PATH = context.get('PATH', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 6
        __M_writer(u'\n<title>\u041f\u0443\u0445 \u0438 \u0432\u0441\u0435-\u0432\u0441\u0435-\u0432\u0441\u0435</title>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n<script type="text/javascript" src="')
        # SOURCE LINE 9
        __M_writer(unicode(PATH('/js/jquery.js')))
        __M_writer(u'"></script>\n<script type="text/javascript" src="')
        # SOURCE LINE 10
        __M_writer(unicode(PATH('/js/jquery.lightbox.js')))
        __M_writer(u'"></script>\n<link rel="stylesheet" type="text/css" href="')
        # SOURCE LINE 11
        __M_writer(unicode(PATH('/css/2011.css')))
        __M_writer(u'"/>\n<link rel="stylesheet" type="text/css" href="')
        # SOURCE LINE 12
        __M_writer(unicode(PATH('/css/jquery.lightbox.css')))
        __M_writer(u'"/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


