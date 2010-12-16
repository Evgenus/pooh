from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1292463556.1070001
_template_filename='D:/Work/Distributives/pooh/source/pooh/css/2011.css'
_template_uri='/pooh/css/2011.css'
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
        __M_writer(u'* {\n    margin: 0px;\n}\n\nbody {\n    font-family: Myriad Pro;\n    font-size: 14px;\n    background-image: url(')
        # SOURCE LINE 8
        __M_writer(unicode(PATH('/images/2011/bear.png')))
        __M_writer(u');\n}\n\n.holder {\n    top: 0px;\n    left: 50%;\n    width: 1px;\n    position: relative;\n}\n\n.main {\n    width: 100%;\n    height: 100%;\n}\n\n.head {\n    width:  926px;\n    height: 290px;\n    left: -463px;\n    top: 0px;\n    position: relative;\n    background-image: url(')
        # SOURCE LINE 29
        __M_writer(unicode(PATH('/images/2011/header.png')))
        __M_writer(u');\n    background-repeat: no-repeat;\n}\n\n.buttons {\n    width:  950px;\n    height: 42px;\n    left: -475px;\n    top: 0px;\n    position: relative;\n}\n\n.buttons span {\n    display: inline-block;\n    height: 42px;\n}\n\n.btn_main_head  {   width:  15px;   background-image: url(')
        # SOURCE LINE 46
        __M_writer(unicode(PATH('/images/2011/green_main.png')))
        __M_writer(u');  }\n.btn_main       {   width: 97px;    background-image: url(')
        # SOURCE LINE 47
        __M_writer(unicode(PATH('/images/2011/green.png')))
        __M_writer(u');       }\n.btn_prog       {   width: 155px;   background-image: url(')
        # SOURCE LINE 48
        __M_writer(unicode(PATH('/images/2011/green.png')))
        __M_writer(u');       }\n.btn_video      {   width: 112px;   background-image: url(')
        # SOURCE LINE 49
        __M_writer(unicode(PATH('/images/2011/green.png')))
        __M_writer(u');       }\n.btn_photo      {   width: 106px;   background-image: url(')
        # SOURCE LINE 50
        __M_writer(unicode(PATH('/images/2011/green.png')))
        __M_writer(u');       }\n.btn_poll       {   width: 155px;   background-image: url(')
        # SOURCE LINE 51
        __M_writer(unicode(PATH('/images/2011/green.png')))
        __M_writer(u');       }\n.btn_where      {   width: 180px;   background-image: url(')
        # SOURCE LINE 52
        __M_writer(unicode(PATH('/images/2011/green.png')))
        __M_writer(u');       }\n.btn_cont       {   width: 112px;   background-image: url(')
        # SOURCE LINE 53
        __M_writer(unicode(PATH('/images/2011/green.png')))
        __M_writer(u');       }\n.btn_cont_tail  {   width:  15px;   background-image: url(')
        # SOURCE LINE 54
        __M_writer(unicode(PATH('/images/2011/green_cont.png')))
        __M_writer(u');  }\n\n.at_main    .btn_main_head  {   background-image: url(')
        # SOURCE LINE 56
        __M_writer(unicode(PATH('/images/2011/orange_main.png')))
        __M_writer(u'); }\n.at_main    .btn_main       {   background-image: url(')
        # SOURCE LINE 57
        __M_writer(unicode(PATH('/images/2011/orange.png')))
        __M_writer(u');      }\n.at_prog    .btn_prog       {   background-image: url(')
        # SOURCE LINE 58
        __M_writer(unicode(PATH('/images/2011/orange.png')))
        __M_writer(u');      }\n.at_video   .btn_video      {   background-image: url(')
        # SOURCE LINE 59
        __M_writer(unicode(PATH('/images/2011/orange.png')))
        __M_writer(u');      }\n.at_photo   .btn_photo      {   background-image: url(')
        # SOURCE LINE 60
        __M_writer(unicode(PATH('/images/2011/orange.png')))
        __M_writer(u');      }\n.at_poll    .btn_poll       {   background-image: url(')
        # SOURCE LINE 61
        __M_writer(unicode(PATH('/images/2011/orange.png')))
        __M_writer(u');      }\n.at_where   .btn_where      {   background-image: url(')
        # SOURCE LINE 62
        __M_writer(unicode(PATH('/images/2011/orange.png')))
        __M_writer(u');      }\n.at_cont    .btn_cont       {   background-image: url(')
        # SOURCE LINE 63
        __M_writer(unicode(PATH('/images/2011/orange.png')))
        __M_writer(u');      }\n.at_cont    .btn_cont_tail  {   background-image: url(')
        # SOURCE LINE 64
        __M_writer(unicode(PATH('/images/2011/orange_cont.png')))
        __M_writer(u'); }\n\n.links {\n    width:  950px;\n    height: 42px;\n    left: 0px;\n    top: 7px;\n    position: absolute;\n    z-index: 30;\n}\n\n.link_main   { width: 112px;    color: #495257; }\n.link_prog   { width: 155px;    color: #495257; }\n.link_video  { width: 112px;    color: #aaa;    }\n.link_photo  { width: 106px;    color: #495257; }\n.link_poll   { width: 155px;    color: #495257; }\n.link_where  { width: 180px;    color: #495257; }\n.link_cont   { width: 127px;    color: #495257; }\n\n.links span {\n    display: inline-block;\n    height: 35px;\n    text-align: center;\n    font-size: 18px;\n    font-weight: bold;\n}\n\n.links a {\n    text-decoration: none;\n}\n\n.links a:hover span {\n    text-decoration: underline;\n}\n\n.footer {\n    width:  926px;\n    height: 50px;\n    left: -463px;\n    bottom: 0px;\n    position: relative;\n    background-image: url(')
        # SOURCE LINE 105
        __M_writer(unicode(PATH('/images/2011/footer.png')))
        __M_writer(u');\n    background-repeat: no-repeat;\n}\n\n#content {\n    width: 860px;\n    left: -450px;\n    min-height:410px;\n    position: relative;\n    padding-left: 20px;\n    padding-right: 20px;\n    background-color: #fff;\n    border-left: 1px solid gray;\n    border-right: 1px solid gray;\n}\n\nspan.date {\n    float:right;\n    font-style: italic;\n}\n\nh3 {\n    font-size: 18px;\n    color: #a7cd34;\n    font-weight: bold;\n    padding-top: 20px;\n    padding-bottom: 20px;\n}\n\nh4 {\n    padding-bottom: 10px;\n}\n\np {\n    text-align: justify;\n    text-indent: 20px;\n    margin-bottom: 10px;\n}\n\ndiv.news {\n    padding-top: 20px;\n    padding-bottom: 20px;\n    clear: right;\n}\n\n.contact_info li {\n    list-style-type: none;\n}\n\n.ljicon {\n    background:transparent url(')
        # SOURCE LINE 155
        __M_writer(unicode(PATH('/images/ljicon.png')))
        __M_writer(u') no-repeat scroll 0 0;\n    padding-left:24px;\n    text-align:left;\n}\n\n.weblink {\n    background:transparent url(')
        # SOURCE LINE 161
        __M_writer(unicode(PATH('/images/firefox.png')))
        __M_writer(u') no-repeat scroll 0 0;\n    padding-left:24px;\n    text-align:left;\n}\n\n.vicon {\n    background:transparent url(')
        # SOURCE LINE 167
        __M_writer(unicode(PATH('/images/vicon.png')))
        __M_writer(u') no-repeat scroll 0 0;\n    padding-left:24px;\n    text-align:left;\n}\n\n.micon {\n    background:transparent url(')
        # SOURCE LINE 173
        __M_writer(unicode(PATH('/images/micon.png')))
        __M_writer(u') no-repeat scroll 0 0;\n    padding-left:24px;\n    text-align:left;\n}\n\n.sicon {\n    background:transparent url(')
        # SOURCE LINE 179
        __M_writer(unicode(PATH('/images/sicon.png')))
        __M_writer(u') no-repeat scroll 0 0;\n    padding-left:24px;\n    text-align:left;\n}\n\n.icqicon {\n    background:transparent url(')
        # SOURCE LINE 185
        __M_writer(unicode(PATH('/images/icqicon.png')))
        __M_writer(u') no-repeat scroll 0 0;\n    padding-left:24px;\n    text-align:left;\n}\n\n.contact_info a, p a {\n    color: #fe942a;\n    text-decoration: none;\n    font-weight: bold;\n}\n\n.contact_info a:hover, p a:hover {\n    color: #ffb200;\n    text-decoration: underline;\n    font-weight: bold;\n}\n\n.contact_info {\n    padding-bottom: 20px;\n}\n\na.gall img {\n    padding: 10px;\n    margin: 10px;\n    background-color: white;\n    border: 1px solid grey;\n}')
        return ''
    finally:
        context.caller_stack._pop_frame()


