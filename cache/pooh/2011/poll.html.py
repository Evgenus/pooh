from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1292461655.016
_template_filename='D:/Work/Distributives/pooh/source/pooh/2011/poll.html'
_template_uri='/pooh/2011/poll.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = ['head', 'page_id']


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
        __M_writer(u'\n\n')
        # SOURCE LINE 83
        __M_writer(u'\n\n<div style="padding:0px 80px 0px 80px">\n\n')
        # SOURCE LINE 87
        for i in range(10):
            # SOURCE LINE 88
            __M_writer(u'<div class="poll">\n    <div class="ui-widget-content ui-corner-top poll-head">\n        \u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435\n    </div>\n    <div class="ui-widget-content ui-corner-bottom poll-content">\n        <a class="gall" style="float:left" href="')
            # SOURCE LINE 93
            __M_writer(unicode(PATH('/images/2011/photo/01.jpg')))
            __M_writer(u'"><img src="')
            __M_writer(unicode(PATH('/images/2011/photo/thumbnails/01.jpg')))
            __M_writer(u'"/></a>\n        <a class="gall" style="float:left" href="')
            # SOURCE LINE 94
            __M_writer(unicode(PATH('/images/2011/photo/01.jpg')))
            __M_writer(u'"><img src="')
            __M_writer(unicode(PATH('/images/2011/photo/thumbnails/01.jpg')))
            __M_writer(u'"/></a>\n        <div class=\'rat-container\'>\n        \t<form class="rat" id="ID')
            # SOURCE LINE 96
            __M_writer(unicode(i))
            __M_writer(u'" action="" method="post">\n        \t\t<select name="rate">\n        \t\t\t\t<option value="1" selected="selected" />Not so great</option>\n        \t\t\t\t<option value="2"  />Quite good</option>\n        \t\t\t\t<option value="3"  />Good</option>\n        \t\t\t\t<option value="4"  />Great!</option>\n        \t\t\t\t<option value="5"  />Excellent!</option>\n        \t\t</select>\n        \t\t<input type="submit" value="Rate it!" />\n        \t</form>\n        </div>\n        <div style="clear:left;"></div>\n    </div>\n</div>\n')
        # SOURCE LINE 111
        __M_writer(u"\n<p style='clear:left'></p>\n\n<script>\n$('a.gall').lightBox();\n</script>\n\n</div>")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context):
    context.caller_stack._push_frame()
    try:
        PATH = context.get('PATH', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n')
        # SOURCE LINE 5
        __M_writer(unicode(parent.head()))
        __M_writer(u'\n<script type="text/javascript" src="')
        # SOURCE LINE 6
        __M_writer(unicode(PATH('/js/jquery-ui.js')))
        __M_writer(u'"></script>\n<script type="text/javascript" src="')
        # SOURCE LINE 7
        __M_writer(unicode(PATH('/js/jquery.ui.stars.js')))
        __M_writer(u'"></script>\n<link rel="stylesheet" type="text/css" href="')
        # SOURCE LINE 8
        __M_writer(unicode(PATH('/css/jquery.ui.stars.css')))
        __M_writer(u'"/>\n<link rel="stylesheet" type="text/css" href="')
        # SOURCE LINE 9
        __M_writer(unicode(PATH('/css/south-street/jquery-ui.css')))
        __M_writer(u'"/>\n<script type="text/javascript">\nfunction makeRating(index, element) {\n    var rat = $(element);\n\trat.children().not("select").hide();\n\n\t// Create caption element\n\tvar caption = $(\'<div id="caption">\');\n\tvar id = rat.attr(\'id\');\n\tvar messages = $(\'<div id="messages"/>\');\n\n\t// Create stars\n\trat.stars({\n\t\tinputType: "select",\n\t\toneVoteOnly: true,\n\t\tcaptionEl: caption,\n\t\tcallback: function(ui, type, value)\n\t\t{\n\t\t\t// Display message to the user at the begining of request\n\t\t\tmessages.text("Saving...").fadeIn(30);\n\t\t\t$.post("demo4.php", {rate: value, name: id}, function(json)\n\t\t\t{\n\t\t\t\t// Select stars from "Average rating" control to match the returned average rating value\n\t\t\t\tui.select(Math.round(json.avg));\n\n\t\t\t\t// Update widget\'s caption\n\t\t\t\tcaption.text(" (" + json.votes + " votes; " + json.avg + ")");\n\n\t\t\t\t// Display confirmation message to the user\n\t\t\t\tmessages.text("Thanks!").stop().css("opacity", 1).fadeIn(30);\n\n\t\t\t\t// Hide confirmation message after 2 sec...\n\t\t\t\tsetTimeout(function(){\n\t\t\t\t\tmessages.fadeOut(1000)\n\t\t\t\t}, 2000);\n\n\t\t\t}, "json");\n\t\t}\n\t});\n\t// Since the <option value="3"> was selected by default, we must remove this selection from Stars.\n\trat.stars("selectID", -1);\n\t// Append caption element !after! the Stars\n\tcaption.appendTo(rat);\n\t// Create element to use for confirmation messages\n\tmessages.appendTo(rat);\n}\n$(function(){\n    $(\'.rat\').map(makeRating);\n});\n</script>\n<style>\n.poll-head {\n    border-bottom: 0 none;\n    padding-top: 5px;\n    text-align: center;\n}\n.poll-content {\n    border-top: 0 none;\n    padding-bottom: 10px;\n}\n.poll {\n    float:left;\n    margin:20px 10px 0px 10px;\n}\n.rat { clear:left; }\n.rat > * {float: left; line-height: 1.4em;}\n#messages, #caption {padding-left: .5em;}\n#messages {color: #fd1c24;}\n.rat-container {\n    clear: left;\n    height: 20px;\n    margin-left: 10px;\n}\n</style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_id(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'poll')
        return ''
    finally:
        context.caller_stack._pop_frame()


