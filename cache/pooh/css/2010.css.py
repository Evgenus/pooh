from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1291324640.3529999
_template_filename='D:/Work/Research/__FUN__/POOH/pooh/source/pooh/css/2010.css'
_template_uri='/pooh/css/2010.css'
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
        __M_writer(u'* {\n    margin: 0px;\n}\n\nbody {\n    background-color: #ffffcc;\n}\n\nh3 {\n     margin-top: 20px;\n     margin-bottom: 10px;\n}\n\n.holder {\n    top: 0px;\n    left: 50%;\n    width: 1px;\n    position: relative;\n}\n\n.header {\n    width:  100%;\n    height: 348px;\n    background-image: url(')
        # SOURCE LINE 24
        __M_writer(unicode(PATH('/images/2010/top1.png')))
        __M_writer(u');\n    background-repeat: repeat-x;\n}\n\n.title {\n    height: 348px;\n    width: 800px;\n    left: -400px;\n    position: relative;\n    background-image: url(')
        # SOURCE LINE 33
        __M_writer(unicode(PATH('/images/2010/top.png')))
        __M_writer(u');\n    background-repeat: no-repeat;\n}\n\n.main {\n    width:  100%;\n    min-height: 410px;\n}\n\n.content {\n    width: 800px;\n    left: -400px;\n    position: relative;\n    color: #000000;\n    text-align: justify;\n    font-family: Arial;\n}\n\n.content p {\n    font-family: Arial;\n    text-indent: 30px;\n    margin-bottom: 10px;\n    font-size: 14px;\n    line-height: 1.5;\n}\n\n.content h2 {\n    font-family: Arial;\n    margin-bottom: 15px;\n    margin-top: 25px;\n    color: #FE942A;\n}\n\n.menu {\n    float: right;\n    width: 210px;\n    background-image: url(')
        # SOURCE LINE 69
        __M_writer(unicode(PATH('/images/2010/menu_rep.png')))
        __M_writer(u');\n    background-repeat: repeat-y;\n    margin-left: 10px;\n}\n\n.menu_body {\n    min-height: 370px;\n    background-image: url(')
        # SOURCE LINE 76
        __M_writer(unicode(PATH('/images/2010/menu.png')))
        __M_writer(u');\n    background-repeat: no-repeat;\n}\n\n.menu_end {\n    height: 40px;\n    background-image: url(')
        # SOURCE LINE 82
        __M_writer(unicode(PATH('/images/2010/menu_but.png')))
        __M_writer(u');\n    background-repeat: no-repeat;\n    position: relative;\n    bottom: 0px;\n}\n\n.buttons {\n    background-image: url(')
        # SOURCE LINE 89
        __M_writer(unicode(PATH('/images/2010/buttons.png')))
        __M_writer(u');\n    height: 372px;\n    background-repeat: no-repeat;\n    position: relative;\n    left: 45px;\n    top:  20px;\n    z-index: 100;\n    background-position: 0px 10px;\n}\n\n.button {\n    height: 40px;\n    width:  185px;\n    left: -50px;\n    position: relative;\n    cursor: pointer;\n}\n\n.button:hover {\n    background-image: url(')
        # SOURCE LINE 108
        __M_writer(unicode(PATH('/images/2010/bee.png')))
        __M_writer(u');\n    background-repeat: no-repeat;\n}\n\n\n.footer {\n    width:  100%;\n    height: 156px;\n    background-image: url(')
        # SOURCE LINE 116
        __M_writer(unicode(PATH('/images/2010/bottom1.png')))
        __M_writer(u');\n    background-repeat: repeat-x;\n}\n\n.copyright {\n    height: 156px;\n    width: 800px;\n    left: -400px;\n    position: relative;\n    background-image: url(')
        # SOURCE LINE 125
        __M_writer(unicode(PATH('/images/2010/bottom.png')))
        __M_writer(u');\n    background-repeat: no-repeat;\n}\n\n#gallery td {\n    text-align: center;\n    vertical-align: middle;\n}\n\n#gallery img {\n    border: 0px;\n    margin: 0px;\n\n}\n\na {\n    color: #fe942a;\n    text-decoration: none;\n    font-weight: bold;\n}\n\na:hover {\n    color: #ffb200;\n    text-decoration: underline;\n    font-weight: bold;\n}\n\n.ljicon {\n    background:transparent url(')
        # SOURCE LINE 153
        __M_writer(unicode(PATH('/images/ljicon.png')))
        __M_writer(u') no-repeat scroll 0 0;\n    padding-left:24px;\n    text-align:left;\n}\n\nli {\n    list-style-type: none;\n}\n\n\n.vicon {\n    background:transparent url(')
        # SOURCE LINE 164
        __M_writer(unicode(PATH('/images/vicon.png')))
        __M_writer(u') no-repeat scroll 0 0;\n    padding-left:24px;\n    text-align:left;\n}\n\n.micon {\n    background:transparent url(')
        # SOURCE LINE 170
        __M_writer(unicode(PATH('/images/micon.png')))
        __M_writer(u') no-repeat scroll 0 0;\n    padding-left:24px;\n    text-align:left;\n}\n\n.sicon {\n    background:transparent url(')
        # SOURCE LINE 176
        __M_writer(unicode(PATH('/images/sicon.png')))
        __M_writer(u') no-repeat scroll 0 0;\n    padding-left:24px;\n    text-align:left;\n}\n\n.icqicon {\n    background:transparent url(')
        # SOURCE LINE 182
        __M_writer(unicode(PATH('/images/icqicon.png')))
        __M_writer(u') no-repeat scroll 0 0;\n    padding-left:24px;\n    text-align:left;\n}\n\n.contact_info {\n    line-height: 1.5;\n}\n\n.progr {\n    padding: 0;\n    margin-left: 0;\n    font-size: 14px;\n    line-height:1.5;\n}\n\n.numlist {\n    color: #fe942a;\n    font-weight: bold;\n}\n\n.info_block img {\n    float:left;\n    margin-right:15px;\n    margin-bottom:30px;\n    width:240px;\n    border:0;\n}\n\n.info_block {\n    clear:left;\n    display:block;\n    padding:0;\n}\n\ndiv.backicon {\n    background:transparent url(')
        # SOURCE LINE 218
        __M_writer(unicode(PATH('/images/baloon.png')))
        __M_writer(u') no-repeat scroll 0 0;\n    padding-left:0px;\n    margin-bottom: 30px;\n}\n\n.content .noind {\n    text-indent:0px;\n}\n\nol.progr li {\n    list-style-type: decimal;\n    margin-bottom: 15px\n}\n\nol.progr li :first-child {\n    font-weight: bold;\n}\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


