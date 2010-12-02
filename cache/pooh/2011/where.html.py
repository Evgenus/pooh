from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1291324640.3239999
_template_filename='D:/Work/Research/__FUN__/POOH/pooh/source/pooh/2011/where.html'
_template_uri='/pooh/2011/where.html'
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
        __M_writer(u'\n<div>\n<h3>\u0412\u0440\u0435\u043c\u044f \u0438 \u043c\u0435\u0441\u0442\u043e \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f</h3>\n\u0421\u0443\u0431\u0431\u043e\u0442\u0430, 27 \u043d\u043e\u044f\u0431\u0440\u044f, 16:00-20:00, \u043a\u043e\u043d\u0444\u0435\u0440\u0435\u043d\u0446-\u0437\u0430\u043b \u0413\u041a \xab\u0422\u0443\u0440\u0438\u0441\u0442\xbb<br>\n\u0443\u043b. \u0420. \u041e\u043a\u0438\u043f\u043d\u043e\u0439 2<br><br>\n<script src="http://api-maps.yandex.ru/1.1/?key=AA8_10wBAAAAmfPpTAIAbuSHXBDYTg6iLCq6CwCCBINbTl4AAAAAAAAAAACO18VXaueiJaUjUWBeYoGBcxS6Mw==&wizard=constructor" type="text/javascript"></script>\n<script type="text/javascript">\n    YMaps.jQuery(window).load(function () {\n        var map = new YMaps.Map(YMaps.jQuery("#YMapsID-1043")[0]);\n        map.setCenter(new YMaps.GeoPoint(30.597957,50.451293), 17, YMaps.MapType.MAP);\n        map.addControl(new YMaps.Zoom());\n        map.addControl(new YMaps.ToolBar());\n        map.addControl(new YMaps.TypeControl());\n\n        YMaps.Styles.add("constructor#pmorlPlacemark", {\n            iconStyle : {\n                href : "http://api-maps.yandex.ru/i/0.3/placemarks/pmorl.png",\n                size : new YMaps.Point(36,41),\n                offset: new YMaps.Point(-13,-40)\n            }\n        });\n\n\n        YMaps.Styles.add("constructor#pmgrsPlacemark", {\n            iconStyle : {\n                href : "http://api-maps.yandex.ru/i/0.3/placemarks/pmgrs.png",\n                size : new YMaps.Point(19,20),\n                offset: new YMaps.Point(-7,-19)\n            }\n        });\n\n\n        YMaps.Styles.add("constructor#FF3732c85Polyline", {\n            lineStyle : {\n                strokeColor : "FF3732c8",\n                strokeWidth : 5\n            }\n        });\n       map.addOverlay(createObject("Placemark", new YMaps.GeoPoint(30.597032,50.450808), "constructor#pmorlPlacemark", "\u0433\u043e\u0441\u0442\u0438\u043d\u0438\u0446\u0430 \\"\u0422\u0443\u0440\u0438\u0441\u0442\\"<br/>\u0443\u043b. \u0420. \u041e\u043a\u0438\u043f\u043d\u043e\u0439 2"));\n       map.addOverlay(createObject("Placemark", new YMaps.GeoPoint(30.599094,50.451328), "constructor#pmgrsPlacemark", "McDonalds"));\n       map.addOverlay(createObject("Polyline", [new YMaps.GeoPoint(30.597373,50.45128),new YMaps.GeoPoint(30.59777,50.450719),new YMaps.GeoPoint(30.597375,50.450582),new YMaps.GeoPoint(30.5973,50.450646)], "constructor#FF3732c85Polyline", ""));\n\n        function createObject (type, point, style, description) {\n            var allowObjects = ["Placemark", "Polyline", "Polygon"],\n                index = YMaps.jQuery.inArray( type, allowObjects),\n                constructor = allowObjects[(index == -1) ? 0 : index];\n                description = description || "";\n\n            var object = new YMaps[constructor](point, {style: style, hasBalloon : !!description});\n            object.description = description;\n\n            return object;\n        }\n    });\n</script>\n\n<div id="YMapsID-1043" style="width:580px;height:402px"></div>\n<br><br><br>\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_id(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'where')
        return ''
    finally:
        context.caller_stack._pop_frame()


