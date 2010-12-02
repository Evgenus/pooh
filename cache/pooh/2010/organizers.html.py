from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1291324639.9519999
_template_filename='D:/Work/Research/__FUN__/POOH/pooh/source/pooh/2010/organizers.html'
_template_uri='/pooh/2010/organizers.html'
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
        __M_writer(u'\n<div id=\'orgs\'>\n<h2>\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0442\u043e\u0440\u044b</h2>\n\n<div class="info_block">\n    <a class="gall" href="')
        # SOURCE LINE 6
        __M_writer(unicode(PATH('/images/2010/org/mrms.jpg')))
        __M_writer(u'"><img src="')
        __M_writer(unicode(PATH('/images/2010/org/thumbnails/mrms.jpg')))
        __M_writer(u'"/></a>\n\t<p><a class="ljicon" href="http://mrybak.livejournal.com/">\u041c\u0438\u0445\u0430\u0438\u043b \u0420\u044b\u0431\u0430\u043a</a>: \u043a\u043e\u043d\u0446\u0435\u043f\u0446\u0438\u044f \u0432\u0435\u0447\u0435\u0440\u0430, \u043f\u043e\u043c\u043e\u0449\u044c \u0438 \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u043e\u0434\u0433\u043e\u0442\u043e\u0432\u043a\u0438 \u043d\u043e\u043c\u0435\u0440\u043e\u0432, \u0430\u0440\u0435\u043d\u0434\u0430 \u043f\u043e\u043c\u0435\u0449\u0435\u043d\u0438\u044f, \u0441\u0446\u0435\u043d\u0430\u0440\u0438\u0439, \u0430\u043f\u043f\u0430\u0440\u0430\u0442\u0443\u0440\u0430.</p>\n\t<p><a class="ljicon" href="http://miracle_sun.livejournal.com/">\u0412\u043b\u0430\u0434\u0438\u0441\u043b\u0430\u0432\u0430 \u0420\u044b\u0431\u0430\u043a</a>: \u043a\u043e\u043d\u0446\u0435\u043f\u0446\u0438\u044f \u0432\u0435\u0447\u0435\u0440\u0430, \u0430\u0440\u0435\u043d\u0434\u0430 \u043f\u043e\u043c\u0435\u0449\u0435\u043d\u0438\u044f, \u0441\u0446\u0435\u043d\u0430\u0440\u0438\u0439, \u0434\u0438\u0437\u0430\u0439\u043d, \u0432\u0435\u0440\u0441\u0442\u043a\u0430 \u0438 \u043f\u0435\u0447\u0430\u0442\u044c \u043f\u0440\u0438\u0433\u043b\u0430\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0445 \u0438 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043e\u043a, \u0434\u0438\u0437\u0430\u0439\u043d \u0438 \u0432\u0435\u0440\u0441\u0442\u043a\u0430 \u0441\u0430\u0439\u0442\u0430, \u043e\u043f\u0435\u0440\u0430\u0442\u043e\u0440 \u0430\u0443\u0434\u0438\u043e- \u0438 \u0432\u0438\u0434\u0435\u043e\u0441\u043e\u043f\u0440\u043e\u0432\u043e\u0436\u0434\u0435\u043d\u0438\u044f.</p>\n</div>\n\n<div class="info_block">\n    <a class="gall" href="')
        # SOURCE LINE 12
        __M_writer(unicode(PATH('/images/2010/org/nk.jpg')))
        __M_writer(u'"><img src="')
        __M_writer(unicode(PATH('/images/2010/org/thumbnails/nk.jpg')))
        __M_writer(u'"/></a>\n\t<p><a class="ljicon" href="http://nkedrova.livejournal.com/">\u041d\u0430\u0442\u0430\u043b\u044c\u044f \u041a\u0435\u0434\u0440\u043e\u0432\u0430</a>: \u043a\u043e\u043d\u0446\u0435\u043f\u0446\u0438\u044f \u0432\u0435\u0447\u0435\u0440\u0430, \u0443\u043a\u0440\u0430\u0448\u0435\u043d\u0438\u0435 \u0437\u0430\u043b\u0430, \u0441\u0446\u0435\u043d\u0430\u0440\u0438\u0439, \u043f\u0435\u0447\u0430\u0442\u044c \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043e\u043a, \u0440\u0430\u0437\u043c\u0435\u0449\u0435\u043d\u0438\u0435 \u0438\u043d\u043e\u0433\u043e\u0440\u043e\u0434\u043d\u0438\u0445 \u0443\u0447\u0430\u0441\u0442\u043d\u0438\u043a\u043e\u0432.</p>\n</div>\n\n<div class="info_block">\n    <a class="gall" href="')
        # SOURCE LINE 17
        __M_writer(unicode(PATH('/images/2010/org/dz.jpg')))
        __M_writer(u'"><img src="')
        __M_writer(unicode(PATH('/images/2010/org/thumbnails/dz.jpg')))
        __M_writer(u'"/></a>\n\t<p><a class="green_a" href="mailto:s1iderorama@gmail.com">\u0414\u0435\u043d\u0438\u0441 \u0417\u0432\u0435\u0437\u0434\u043e\u0432</a>: \u0437\u0432\u0443\u043a\u043e\u0440\u0435\u0436\u0438\u0441\u0441\u0435\u0440</p>\n</div>\n\n<div class="info_block">\n    <a class="gall" href="')
        # SOURCE LINE 22
        __M_writer(unicode(PATH('/images/2010/org/vosp.jpg')))
        __M_writer(u'"><img src="')
        __M_writer(unicode(PATH('/images/2010/org/thumbnails/vosp.jpg')))
        __M_writer(u'"/></a>\n\t<p><a class="ljicon" href="http://vospi.livejournal.com/">\u0421\u0435\u0440\u0433\u0435\u0439 \u0410\u043d\u0438\u043a\u0438\u043d</a>: \u0430\u0441\u0441\u0438\u0441\u0442\u0435\u043d\u0442 \u0437\u0432\u0443\u043a\u043e\u0440\u0435\u0436\u0438\u0441\u0441\u0435\u0440\u0430, \u0430\u0441\u0441\u0438\u0441\u0442\u0435\u043d\u0442 \u043f\u043e \u0441\u0446\u0435\u043d\u0435.</p>\n</div>\t\n\n<div class="info_block">\n    <a class="gall" href="')
        # SOURCE LINE 27
        __M_writer(unicode(PATH('/images/2010/org/xsi.jpg')))
        __M_writer(u'"><img src="')
        __M_writer(unicode(PATH('/images/2010/org/thumbnails/xsi.jpg')))
        __M_writer(u'"/></a>\n\t<p><a class="ljicon" href="http://lord-xsi.livejournal.com/">\u0410\u043d\u0434\u0440\u0435\u0439 \u0412\u043b\u0430\u0441\u043e\u0432</a>: \u043a\u043e\u043d\u0446\u0435\u043f\u0446\u0438\u044f \u0432\u0435\u0447\u0435\u0440\u0430, \u0440\u0435\u043a\u0432\u0438\u0437\u0438\u0442, \u0430\u0441\u0441\u0438\u0441\u0442\u0435\u043d\u0442 \u043f\u043e \u0441\u0446\u0435\u043d\u0435.</p>\n</div>\t\n\n<div class="info_block">\n    <a class="gall" href="')
        # SOURCE LINE 32
        __M_writer(unicode(PATH('/images/2010/org/shan.jpg')))
        __M_writer(u'"><img src="')
        __M_writer(unicode(PATH('/images/2010/org/thumbnails/shan.jpg')))
        __M_writer(u'"/></a>\n\t<p><a class="ljicon" href="http://shannar.livejournal.com/">\u0428\u0430\u043d\u043d\u0430\u0440 \u0434\u0435 \u041a\u0430\u0441\u0441\u0430\u043b</a>: \u0432\u0438\u0434\u0435\u043e\u0441\u044a\u0451\u043c\u043a\u0430.</p>\n</div>\n\n<div class="info_block">\n    <a class="gall" href="')
        # SOURCE LINE 37
        __M_writer(unicode(PATH('/images/2010/org/vasay.jpg')))
        __M_writer(u'"><img src="')
        __M_writer(unicode(PATH('/images/2010/org/thumbnails/vasay.jpg')))
        __M_writer(u'"/></a>\n\t<p><a class="ljicon" href="http://vasay-san.livejournal.com/">\u0412\u0430\u0441\u0438\u043b\u0438\u0439 \u0413\u043e\u043d\u0447\u0430\u0440\u043e\u0432</a>: \u0432\u0438\u0434\u0435\u043e\u0441\u044a\u0451\u043c\u043a\u0430.</p>\n</div>\n\n<div style="clear:left;"></div>\n<script>\n$(\'#orgs a.gall\').lightBox();\n</script>\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


