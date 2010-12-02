from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1291324581.3280001
_template_filename='D:/Work/Research/__FUN__/POOH/pooh/source/pooh/2010/contacts.html'
_template_uri='/pooh/2010/contacts.html'
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
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n<div>\n<h2>\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u044b</h2>\n<div class="contact_block">\n\n<h3>\u041c\u0438\u0445\u0430\u0438\u043b \u0420\u044b\u0431\u0430\u043a:</h3>\n<ul class="contact_info">\n\t<li>\u041e\u0431\u0440\u0430\u0449\u0430\u0442\u044c\u0441\u044f \u043f\u043e \u0432\u043e\u043f\u0440\u043e\u0441\u0430\u043c \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438 \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0439 \u0438 \u0442\u0432\u043e\u0440\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u0447\u0435\u0441\u0442\u0432\u0430.</li>\n\t<li><span class="micon">e-mail</span>:<a class="green_a" href="mailto:michael.rybak@gmail.com"> michael.rybak@gmail.com</a></li>\n\t<li><span class="ljicon">livejournal</span>: <a class="green_a" href="http://mrybak.livejournal.com/">mrybak.livejournal.com</a></li>\n\t<li><span class="vicon">\u0432\u043a\u043e\u043d\u0442\u0430\u043a\u0442\u0435</span>: <a class="green_a" href="http://vkontakte.ru/id44555731">Michael Rybak</a></li>\n</ul>\n\n<h3>\u0421\u0435\u0440\u0433\u0435\u0439 \u0410\u043d\u0438\u043a\u0438\u043d:</h3>\n<ul class="contact_info">\n    <li>\u041a\u043e\u043c\u043f\u043e\u0437\u0438\u0442\u043e\u0440, \u0440\u0430\u0431\u043e\u0442\u0430 \u0441\u043e \u0437\u0432\u0443\u043a\u043e\u043c.</li>\n    <li><span class="ljicon">livejournal</span>: <a class="green_a" href="http://vospi.livejournal.com/">vospi.livejournal.com</a></li>\n    <li><span class="sicon">\u041c\u0443\u0437\u044b\u043a\u0430\u043b\u044c\u043d\u043e\u0435 \u043f\u043e\u0440\u0442\u0444\u043e\u043b\u0438\u043e</span>: <a class="green_a" href="http://vospi.com/">vospi.com</a></li>\n</ul>\n\n<h3>\u0414\u0435\u043d\u0438\u0441 \u0417\u0432\u0435\u0437\u0434\u043e\u0432:</h3>\n<ul class="contact_info">\n    <li>\u0417\u0432\u0443\u043a\u043e\u0440\u0435\u0436\u0438\u0441\u0441\u0435\u0440.</li>\n    <li><span class="micon">e-mail</span>:<a class="green_a" href="mailto:s1iderorama@gmail.com"> s1iderorama@gmail.com</a></li>\n    <li><span class="icqicon">icq: 9021624</span></li>\n</ul>\n\n<h3>\u0410\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440 \u041c\u0430\u0440\u0438\u043d\u0438\u0447:</h3>\n<ul class="contact_info">\n\t<li><span class="sicon">\u0421\u0430\u0439\u0442  \u0441\u0432\u0438\u043d\u0433-\u0434\u044d\u043d\u0441-\u0442\u0443\u0441\u043e\u0432\u043a\u0438</span>: <a class="green_a" href="http://www.swingdance.kiev.ua">http://www.swingdance.kiev.ua</a></li>\n\t<li><span class="ljicon">livejournal</span>: <a class="green_a" href="http://sashko_online.livejournal.com/">sashko_online.livejournal.com</a></li>\n\t<li><span class="vicon">\u0413\u0440\u0443\u043f\u043f\u0430 \u0432\u043a\u043e\u043d\u0442\u0430\u043a\u0442\u0435</span>: <a class="green_a" href="http://vkontakte.ru/club13472008">\u0428\u043a\u043e\u043b\u0430 \u043f\u0435\u0440\u043a\u0443\u0441\u0441\u0438\u0438 \u0438 \u0430\u0444\u0440\u043e\u0442\u0430\u043d\u0446\u0435\u0432</a></li>\n</ul>\n\n<h3>\u0414\u0438\u043c\u0430 \u0412\u043e\u0440\u043e\u043d\u0438\u043d:</h3>\n<ul class="contact_info">\n    <li><span class="ljicon">livejournal</span>: <a class="green_a" href="http://skyrave.livejournal.com">skyrave.livejournal.com</a></li>\n    <li><span class="micon">e-mail</span>: <a class="green_a" href="mailto:s1iderorama@gmail.com">ilrave@gmail.com</a></li>\n    <li><span class="icqicon">icq</span>: 85855778</li>\n</ul>\n\n<h3>GoDoPaTa School:</h3>\n<ul class="contact_info">\n    <li><span class="vicon">\u0413\u0440\u0443\u043f\u043f\u0430 \u0432\u043a\u043e\u043d\u0442\u0430\u043a\u0435</span>: <a class="green_a" href="http://vkontakte.ru/club13472008">\u0410\u0444\u0440\u0438\u043a\u0430\u043d\u0441\u043a\u0438\u0435 \u0442\u0430\u043d\u0446\u044b \u0432 \u041a\u0438\u0435\u0432\u0435</a></li>\n    <li><span class="sicon">\u0421\u0430\u0439\u0442</span>: <a class="green_a" href="http://godopata.com">http://godopata.com</a></li>\n</ul>\n\n<h3>Vasay Goncharov:</h3>\n<ul class="contact_info">\n    <li><span class="ljicon">livejournal</span>: <a class="green_a" href="http://vasay-san.livejournal.com/">vasay-san.livejournal.com</a></li>\n    <li><span class="micon">e-mail</span>: <a class="green_a" href="mailto:vassay@gmail.com">vassay@gmail.com</a></li>\n</ul>\n\n<h3>\u0414\u043c\u0438\u0442\u0440\u0438\u0439 \u0411\u0430\u0433\u0430\u0435\u0432:</h3>\n<ul class="contact_info">\n    <li><span class="sicon">\u0422\u0440\u0435\u0432\u0435\u043b\u043e\u0433</span>: <a class="green_a" href="http://owayt.blogspot.com">http://owayt.blogspot.com</a></li>\n    <li><span class="micon">e-mail</span>: <a class="green_a" href="mailto:dmitry.bagaev@gmail.com">dmitry.bagaev@gmail.com</a></li>\n</ul>\n\n</div>\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


