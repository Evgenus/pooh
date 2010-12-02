from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1291324640.039
_template_filename='D:/Work/Research/__FUN__/POOH/pooh/source/pooh/2010/photo.html'
_template_uri='/pooh/2010/photo.html'
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
        __M_writer(u'\n<div id=\'gallery\'>\n<table>\n<tr>\n<td><a href="')
        # SOURCE LINE 5
        __M_writer(unicode(PATH('/images/2010/photo/01.jpg')))
        __M_writer(u'"><img src="')
        __M_writer(unicode(PATH('/images/2010/thumbnails/t_01.jpg')))
        __M_writer(u'"/></a></td>\n<td><a href="')
        # SOURCE LINE 6
        __M_writer(unicode(PATH('/images/2010/photo/02.jpg')))
        __M_writer(u'"><img src="')
        __M_writer(unicode(PATH('/images/2010/thumbnails/t_02.jpg')))
        __M_writer(u'"/></a></td>\n<td><a href="')
        # SOURCE LINE 7
        __M_writer(unicode(PATH('/images/2010/photo/03.jpg')))
        __M_writer(u'"><img src="')
        __M_writer(unicode(PATH('/images/2010/thumbnails/t_03.jpg')))
        __M_writer(u'"/></a></td>\n<td><a href="')
        # SOURCE LINE 8
        __M_writer(unicode(PATH('/images/2010/photo/04.jpg')))
        __M_writer(u'"><img src="')
        __M_writer(unicode(PATH('/images/2010/thumbnails/t_04.jpg')))
        __M_writer(u'"/></a></td>\n<tr>\n</tr>\n<td><a href="')
        # SOURCE LINE 11
        __M_writer(unicode(PATH('/images/2010/photo/05.jpg')))
        __M_writer(u'"><img src="')
        __M_writer(unicode(PATH('/images/2010/thumbnails/t_05.jpg')))
        __M_writer(u'"/></a></td>\n<td><a href="')
        # SOURCE LINE 12
        __M_writer(unicode(PATH('/images/2010/photo/06.jpg')))
        __M_writer(u'"><img src="')
        __M_writer(unicode(PATH('/images/2010/thumbnails/t_06.jpg')))
        __M_writer(u'"/></a></td>\n<td><a href="')
        # SOURCE LINE 13
        __M_writer(unicode(PATH('/images/2010/photo/07.jpg')))
        __M_writer(u'"><img src="')
        __M_writer(unicode(PATH('/images/2010/thumbnails/t_07.jpg')))
        __M_writer(u'"/></a></td>\n<td><a href="')
        # SOURCE LINE 14
        __M_writer(unicode(PATH('/images/2010/photo/08.jpg')))
        __M_writer(u'"><img src="')
        __M_writer(unicode(PATH('/images/2010/thumbnails/t_08.jpg')))
        __M_writer(u'"/></a></td>\n<tr>\n</tr>\n<td><a href="')
        # SOURCE LINE 17
        __M_writer(unicode(PATH('/images/2010/photo/09.jpg')))
        __M_writer(u'"><img src="')
        __M_writer(unicode(PATH('/images/2010/thumbnails/t_09.jpg')))
        __M_writer(u'"/></a></td>\n<td><a href="')
        # SOURCE LINE 18
        __M_writer(unicode(PATH('/images/2010/photo/10.jpg')))
        __M_writer(u'"><img src="')
        __M_writer(unicode(PATH('/images/2010/thumbnails/t_10.jpg')))
        __M_writer(u'"/></a></td>\n<td><a href="')
        # SOURCE LINE 19
        __M_writer(unicode(PATH('/images/2010/photo/11.jpg')))
        __M_writer(u'"><img src="')
        __M_writer(unicode(PATH('/images/2010/thumbnails/t_11.jpg')))
        __M_writer(u'"/></a></td>\n<td><a href="')
        # SOURCE LINE 20
        __M_writer(unicode(PATH('/images/2010/photo/12.jpg')))
        __M_writer(u'"><img src="')
        __M_writer(unicode(PATH('/images/2010/thumbnails/t_12.jpg')))
        __M_writer(u'"/></a></td>\n<tr>\n</tr>\n<td><a href="')
        # SOURCE LINE 23
        __M_writer(unicode(PATH('/images/2010/photo/13.jpg')))
        __M_writer(u'"><img src="')
        __M_writer(unicode(PATH('/images/2010/thumbnails/t_13.jpg')))
        __M_writer(u'"/></a></td>\n<td><a href="')
        # SOURCE LINE 24
        __M_writer(unicode(PATH('/images/2010/photo/14.jpg')))
        __M_writer(u'"><img src="')
        __M_writer(unicode(PATH('/images/2010/thumbnails/t_14.jpg')))
        __M_writer(u'"/></a></td>\n<td><a href="')
        # SOURCE LINE 25
        __M_writer(unicode(PATH('/images/2010/photo/15.jpg')))
        __M_writer(u'"><img src="')
        __M_writer(unicode(PATH('/images/2010/thumbnails/t_15.jpg')))
        __M_writer(u'"/></a></td>\n<td><a href="')
        # SOURCE LINE 26
        __M_writer(unicode(PATH('/images/2010/photo/16.jpg')))
        __M_writer(u'"><img src="')
        __M_writer(unicode(PATH('/images/2010/thumbnails/t_16.jpg')))
        __M_writer(u'"/></a></td>\n<tr>\n</tr>\n<td><a href="')
        # SOURCE LINE 29
        __M_writer(unicode(PATH('/images/2010/photo/17.jpg')))
        __M_writer(u'"><img src="')
        __M_writer(unicode(PATH('/images/2010/thumbnails/t_17.jpg')))
        __M_writer(u'"/></a></td>\n<td><a href="')
        # SOURCE LINE 30
        __M_writer(unicode(PATH('/images/2010/photo/18.jpg')))
        __M_writer(u'"><img src="')
        __M_writer(unicode(PATH('/images/2010/thumbnails/t_18.jpg')))
        __M_writer(u'"/></a></td>\n<td><a href="')
        # SOURCE LINE 31
        __M_writer(unicode(PATH('/images/2010/photo/19.jpg')))
        __M_writer(u'"><img src="')
        __M_writer(unicode(PATH('/images/2010/thumbnails/t_19.jpg')))
        __M_writer(u'"/></a></td>\n<td><a href="')
        # SOURCE LINE 32
        __M_writer(unicode(PATH('/images/2010/photo/20.jpg')))
        __M_writer(u'"><img src="')
        __M_writer(unicode(PATH('/images/2010/thumbnails/t_20.jpg')))
        __M_writer(u'"/></a></td>\n<tr>\n</tr>\n<td><a href="')
        # SOURCE LINE 35
        __M_writer(unicode(PATH('/images/2010/photo/21.jpg')))
        __M_writer(u'"><img src="')
        __M_writer(unicode(PATH('/images/2010/thumbnails/t_21.jpg')))
        __M_writer(u'"/></a></td>\n<td><a href="')
        # SOURCE LINE 36
        __M_writer(unicode(PATH('/images/2010/photo/22.jpg')))
        __M_writer(u'"><img src="')
        __M_writer(unicode(PATH('/images/2010/thumbnails/t_22.jpg')))
        __M_writer(u'"/></a></td>\n<td><a href="')
        # SOURCE LINE 37
        __M_writer(unicode(PATH('/images/2010/photo/23.jpg')))
        __M_writer(u'"><img src="')
        __M_writer(unicode(PATH('/images/2010/thumbnails/t_23.jpg')))
        __M_writer(u'"/></a></td>\n<td><a href="')
        # SOURCE LINE 38
        __M_writer(unicode(PATH('/images/2010/photo/24.jpg')))
        __M_writer(u'"><img src="')
        __M_writer(unicode(PATH('/images/2010/thumbnails/t_24.jpg')))
        __M_writer(u'"/></a></td>\n</tr>\n</table>\n<script>\n$(\'#gallery a\').lightBox();\n</script>\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


