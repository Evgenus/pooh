from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1291324640.1270001
_template_filename='D:/Work/Research/__FUN__/POOH/pooh/source/pooh/2011/contacts.html'
_template_uri='/pooh/2011/contacts.html'
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
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n<div>\n<h3>\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0442\u043e\u0440\u044b</h3>\n\n<h4>\u041c\u0438\u0445\u0430\u0438\u043b \u0420\u044b\u0431\u0430\u043a</h4>\n<ul class="contact_info">\n\t<li><span class="micon">e-mail</span>:<a href="mailto:michael.rybak@gmail.com"> michael.rybak@gmail.com</a></li>\n\t<li><span class="ljicon">livejournal</span>: <a href="http://mrybak.livejournal.com/">mrybak.livejournal.com</a></li>\n\t<li><span class="vicon">\u0432\u043a\u043e\u043d\u0442\u0430\u043a\u0442\u0435</span>: <a href="http://vkontakte.ru/id44555731">Michael Rybak</a></li>\n</ul>\n\n<h4>\u0410\u043d\u0430\u0442\u043e\u043b\u0438\u0439 \u0428\u0443\u0441\u0442\u0435\u0440\u043e\u0432</h4>\n<ul class="contact_info">\n\t<li><span class="micon">e-mail</span>:<a href="mailto:tolyan.shu@gmail.com"> tolyan.shu@gmail.com</a></li>\n\t<li><span class="ljicon">livejournal</span>: <a href="http://sun-prince.livejournal.com/">sun-prince.livejournal.com</a></li>\n\t<li><span class="vicon">\u0432\u043a\u043e\u043d\u0442\u0430\u043a\u0442\u0435</span>: <a href="http://vkontakte.ru/id4255340">Sun Prince</a></li>\n</ul>\n\n<h3>\u041e\u0440\u0433\u043a\u043e\u043c\u0438\u0442\u0435\u0442</h3>\n\n<h4>\u0414\u0435\u043d\u0438\u0441 \u0417\u0432\u0435\u0437\u0434\u043e\u0432</h4>\n<ul class="contact_info">\n    <li>\u0417\u0432\u0443\u043a\u043e\u0440\u0435\u0436\u0438\u0441\u0441\u0435\u0440.</li>\n    <li><span class="micon">e-mail</span>:<a href="mailto:s1iderorama@gmail.com"> s1iderorama@gmail.com</a></li>\n    <li><span class="icqicon">icq: 9021624</span></li>\n</ul>\n\n<h4>\u0422\u0430\u0442\u044c\u044f\u043d\u0430 \u0427\u0435\u0440\u043d\u044b\u0448\u043e\u0432\u0430</h4>\n<ul class="contact_info">\n    <li>\u0414\u0438\u0437\u0430\u0439\u043d \u0441\u0430\u0439\u0442\u0430.</li>\n\t<li><span class="micon">e-mail</span>:<a href="mailto:chii-chan@i.ua"> chii-chan@i.ua</a></li>\n\t<li><span class="ljicon">livejournal</span>: <a href="http://harumambura.livejournal.com/">harumambura.livejournal.com</a></li>\n\t<li><span class="vicon">\u0432\u043a\u043e\u043d\u0442\u0430\u043a\u0442\u0435</span>: <a href="http://vkontakte.ru/id2422002">harumambura</a></li>\n</ul>\n\n\n<h4>\u0415\u0432\u0433\u0435\u043d\u0438\u0439 \u0427\u0435\u0440\u043d\u044b\u0448\u043e\u0432</h4>\n<ul class="contact_info">\n    <li>\u0412\u0451\u0440\u0441\u0442\u043a\u0430 \u0441\u0430\u0439\u0442\u0430.</li>\n\t<li><span class="micon">e-mail</span>:<a href="mailto:chernyshov.eugene@gmail.com"> chernyshov.eugene@gmail.com</a></li>\n\t<li><span class="ljicon">livejournal</span>: <a href="http://ev-genus.livejournal.com/">ev-genus.livejournal.com</a></li>\n</ul>\n\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_id(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'cont')
        return ''
    finally:
        context.caller_stack._pop_frame()


