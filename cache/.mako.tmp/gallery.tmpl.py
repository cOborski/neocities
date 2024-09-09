# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1725903920.642869
_enable_loop = True
_template_filename = 'C:/Python312/Lib/site-packages/nikola/data/themes/base/templates/gallery.tmpl'
_template_uri = 'gallery.tmpl'
_source_encoding = 'utf-8'
_exports = ['sourcelink', 'content', 'extra_head', 'extra_js']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('ui', context._clean_inheritance_tokens(), templateuri='ui_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'ui')] = ns

    ns = runtime.TemplateNamespace('post_helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'post_helper')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        ui = _mako_get_namespace(context, 'ui')
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        len = context.get('len', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        photo_array = context.get('photo_array', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        enable_comments = context.get('enable_comments', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        photo_array_json = context.get('photo_array_json', UNDEFINED)
        title = context.get('title', UNDEFINED)
        post_helper = _mako_get_namespace(context, 'post_helper')
        _link = context.get('_link', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        galleries_use_thumbnail = context.get('galleries_use_thumbnail', UNDEFINED)
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        folders = context.get('folders', UNDEFINED)
        crumbs = context.get('crumbs', UNDEFINED)
        post = context.get('post', UNDEFINED)
        thumbnail_size = context.get('thumbnail_size', UNDEFINED)
        gallery_path = context.get('gallery_path', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        ui = _mako_get_namespace(context, 'ui')
        galleries_use_thumbnail = context.get('galleries_use_thumbnail', UNDEFINED)
        folders = context.get('folders', UNDEFINED)
        photo_array = context.get('photo_array', UNDEFINED)
        crumbs = context.get('crumbs', UNDEFINED)
        post = context.get('post', UNDEFINED)
        thumbnail_size = context.get('thumbnail_size', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        enable_comments = context.get('enable_comments', UNDEFINED)
        title = context.get('title', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(ui.breadcrumbs(crumbs)))
        __M_writer('\n')
        if title:
            __M_writer('    <h1>')
            __M_writer(filters.html_escape(str(title)))
            __M_writer('</h1>\n')
        if post:
            __M_writer('    <p>\n        ')
            __M_writer(str(post.text()))
            __M_writer('\n    </p>\n')
        if folders:
            pass
            if galleries_use_thumbnail:
                pass
                for (folder, ftitle, fpost) in folders:
                    __M_writer('            <div class="thumnbnail-container">\n                <a href="')
                    __M_writer(str(folder))
                    __M_writer('" class="thumbnail image-reference" title="')
                    __M_writer(filters.html_escape(str(ftitle)))
                    __M_writer('">\n')
                    if fpost and fpost.previewimage:
                        __M_writer('                        <img src="')
                        __M_writer(str(fpost.previewimage))
                        __M_writer('" alt="')
                        __M_writer(filters.html_escape(str(ftitle)))
                        __M_writer('" loading="lazy" style="max-width:')
                        __M_writer(str(thumbnail_size))
                        __M_writer('px; max-height:')
                        __M_writer(str(thumbnail_size))
                        __M_writer('px;" />\n')
                    else:
                        __M_writer('                        <div style="height: ')
                        __M_writer(str(thumbnail_size))
                        __M_writer('px; width: ')
                        __M_writer(str(thumbnail_size))
                        __M_writer('px; background-color: #eee;"></div>\n')
                    __M_writer('                <p class="thumbnail-caption">')
                    __M_writer(filters.html_escape(str(ftitle)))
                    __M_writer('</p>\n                </a>\n            </div>\n')
            else:
                __M_writer('            <ul>\n')
                for folder, ftitle in folders:
                    __M_writer('                <li><a href="')
                    __M_writer(str(folder))
                    __M_writer('">&#x1f4c2;&nbsp;')
                    __M_writer(filters.html_escape(str(ftitle)))
                    __M_writer('</a></li>\n')
                __M_writer('            </ul>\n')
        __M_writer('\n<div id="gallery_container"></div>\n')
        if photo_array:
            __M_writer('<noscript>\n<ul class="thumbnails">\n')
            for image in photo_array:
                __M_writer('        <li><a href="')
                __M_writer(str(image['url']))
                __M_writer('" class="thumbnail image-reference" title="')
                __M_writer(filters.html_escape(str(image['title'])))
                __M_writer('">\n            <img src="')
                __M_writer(str(image['url_thumb']))
                __M_writer('" alt="')
                __M_writer(filters.html_escape(str(image['title'])))
                __M_writer('" loading="lazy" /></a>\n')
            __M_writer('</ul>\n</noscript>\n')
        if site_has_comments and enable_comments:
            __M_writer('    ')
            __M_writer(str(comments.comment_form(None, permalink, title)))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        parent = context.get('parent', UNDEFINED)
        len = context.get('len', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        post = context.get('post', UNDEFINED)
        gallery_path = context.get('gallery_path', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        post_helper = _mako_get_namespace(context, 'post_helper')
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n<link rel="alternate" type="application/rss+xml" title="RSS" href="rss.xml">\n<style type="text/css">\n    #gallery_container {\n        position: relative;\n    }\n    .image-block {\n        position: absolute;\n    }\n</style>\n')
        if len(translations) > 1:
            pass
            for langname in translations.keys():
                pass
                if langname != lang:
                    __M_writer('             <link rel="alternate" hreflang="')
                    __M_writer(str(langname))
                    __M_writer('" href="')
                    __M_writer(str(_link('gallery', gallery_path, langname)))
                    __M_writer('">\n')
        __M_writer('<link rel="alternate" type="application/rss+xml" title="RSS" href="rss.xml">\n')
        if post:
            __M_writer('    ')
            __M_writer(str(post_helper.open_graph_metadata(post)))
            __M_writer('\n    ')
            __M_writer(str(post_helper.twitter_card_information(post)))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        photo_array_json = context.get('photo_array_json', UNDEFINED)
        thumbnail_size = context.get('thumbnail_size', UNDEFINED)
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        __M_writer('\n<script src="/assets/js/justified-layout.min.js"></script>\n<script src="/assets/js/gallery.min.js"></script>\n<script>\nvar jsonContent = ')
        __M_writer(str(photo_array_json))
        __M_writer(';\nvar thumbnailSize = ')
        __M_writer(str(thumbnail_size))
        __M_writer(";\nrenderGallery(jsonContent, thumbnailSize);\nwindow.addEventListener('resize', function(){renderGallery(jsonContent, thumbnailSize)});\n</script>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Python312/Lib/site-packages/nikola/data/themes/base/templates/gallery.tmpl", "uri": "gallery.tmpl", "source_encoding": "utf-8", "line_map": {"23": 3, "26": 4, "29": 5, "35": 0, "68": 2, "69": 3, "70": 4, "71": 5, "76": 6, "81": 55, "86": 80, "91": 91, "97": 6, "108": 8, "126": 8, "127": 9, "128": 9, "129": 10, "130": 11, "131": 11, "132": 11, "133": 13, "134": 14, "135": 15, "136": 15, "137": 18, "139": 19, "141": 20, "142": 21, "143": 22, "144": 22, "145": 22, "146": 22, "147": 23, "148": 24, "149": 24, "150": 24, "151": 24, "152": 24, "153": 24, "154": 24, "155": 24, "156": 24, "157": 25, "158": 26, "159": 26, "160": 26, "161": 26, "162": 26, "163": 28, "164": 28, "165": 28, "166": 32, "167": 33, "168": 34, "169": 35, "170": 35, "171": 35, "172": 35, "173": 35, "174": 37, "175": 40, "176": 42, "177": 43, "178": 45, "179": 46, "180": 46, "181": 46, "182": 46, "183": 46, "184": 47, "185": 47, "186": 47, "187": 47, "188": 49, "189": 52, "190": 53, "191": 53, "192": 53, "198": 57, "212": 57, "213": 58, "214": 58, "215": 68, "217": 69, "219": 70, "220": 71, "221": 71, "222": 71, "223": 71, "224": 71, "225": 75, "226": 76, "227": 77, "228": 77, "229": 77, "230": 78, "231": 78, "237": 82, "245": 82, "246": 86, "247": 86, "248": 87, "249": 87, "255": 249}}
__M_END_METADATA
"""
