# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1725903920.4922247
_enable_loop = True
_template_filename = 'themes/lotabout/templates/zzz_helper.tmpl'
_template_uri = 'zzz_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_headstart', 'html_stylesheets', 'html_feedlinks', 'late_load_js', 'html_tags', 'html_title', 'html_translations', 'html_sourcelink']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        def html_stylesheets():
            return render_html_stylesheets(context)
        comment_system = context.get('comment_system', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        title = context.get('title', UNDEFINED)
        striphtml = context.get('striphtml', UNDEFINED)
        is_rtl = context.get('is_rtl', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        description = context.get('description', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        twitter_card = context.get('twitter_card', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        nextlink = context.get('nextlink', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!DOCTYPE html>\n<html ')
        __M_writer("prefix='")
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
            __M_writer('og: http://ogp.me/ns# article: http://ogp.me/ns/article# ')
        if comment_system == 'facebook':
            __M_writer('fb: http://ogp.me/ns/fb#\n')
        __M_writer("' ")
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
            __M_writer('vocab="http://ogp.me/ns" ')
        if is_rtl:
            __M_writer('dir="rtl" ')
        __M_writer('lang="')
        __M_writer(str(lang))
        __M_writer('">\n<head>\n    <meta charset="utf-8">\n')
        if description:
            __M_writer('    <meta name="description" content="')
            __M_writer(str(description))
            __M_writer('">\n')
        __M_writer('    <meta name="viewport" content="width=device-width">\n    <title>')
        __M_writer(striphtml(str(title)))
        __M_writer(' | ')
        __M_writer(striphtml(str(blog_title)))
        __M_writer('</title>\n\n    ')
        __M_writer(str(html_stylesheets()))
        __M_writer('\n    ')
        __M_writer(str(html_feedlinks()))
        __M_writer('\n')
        if permalink:
            __M_writer('      <link rel="canonical" href="')
            __M_writer(str(abs_link(permalink)))
            __M_writer('">\n')
        __M_writer('\n')
        if favicons:
            pass
            for name, file, size in favicons:
                __M_writer('            <link rel="')
                __M_writer(str(name))
                __M_writer('" href="')
                __M_writer(str(file))
                __M_writer('" sizes="')
                __M_writer(str(size))
                __M_writer('"/>\n')
        __M_writer('\n')
        if comment_system == 'facebook':
            __M_writer('        <meta property="fb:app_id" content="')
            __M_writer(str(comment_system_id))
            __M_writer('">\n')
        __M_writer('\n')
        if prevlink:
            __M_writer('        <link rel="prev" href="')
            __M_writer(str(prevlink))
            __M_writer('" type="text/html">\n')
        if nextlink:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(nextlink))
            __M_writer('" type="text/html">\n')
        __M_writer('\n    ')
        __M_writer(str(mathjax_config))
        __M_writer('\n')
        if use_cdn:
            __M_writer('        <!--[if lt IE 9]><script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\n')
        else:
            __M_writer('        <!--[if lt IE 9]><script src="')
            __M_writer(str(url_replacer(permalink, '/assets/js/html5.js', lang)))
            __M_writer('"></script><![endif]-->\n')
        __M_writer('\n    ')
        __M_writer(str(extra_head_data))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_bundles = context.get('use_bundles', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            pass
            if use_cdn:
                __M_writer('            <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n            <link rel="stylesheet" id=\'css_theme\' href="/assets/css/theme.gray.css" type="text/css"/>\n')
            else:
                __M_writer('            <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\n            <link rel="stylesheet" id=\'css_theme\' href="/assets/css/theme.gray.css" type="text/css"/>\n')
        else:
            __M_writer('        <link href="/assets/css/font-awesome.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/style.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/flip.css" rel="stylesheet" type="text/css">\n        <link rel="stylesheet" id=\'css_theme\' href="/assets/css/theme.gray.css" type="text/css"/>\n\n')
            if has_custom_css:
                __M_writer('            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if rss_link:
            __M_writer('        ')
            __M_writer(str(rss_link))
            __M_writer('\n')
        elif generate_rss:
            pass
            if len(translations) > 1:
                pass
                for language in translations:
                    __M_writer('                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('rss', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(str(_link('rss', None)))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_bundles = context.get('use_bundles', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            pass
            if use_cdn:
                __M_writer('            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>\n            <script src="//cdnjs.cloudflare.com/ajax/libs/jquery-timeago/1.1.0/jquery.timeago.min.js"></script>\n')
            else:
                __M_writer('            <script src="/assets/js/all-nocdn.js" type="text/javascript"></script>\n')
        else:
            pass
            if use_cdn:
                __M_writer('            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>\n            <script src="//cdnjs.cloudflare.com/ajax/libs/jquery-timeago/1.1.0/jquery.timeago.min.js"></script>\n')
            else:
                __M_writer('            <script src="/assets/js/jquery-1.10.2.min.js" type="text/javascript"></script>\n            <script src="/assets/js/jquery.timeago.js" type="text/javascript"></script>\n            <script src="/assets/js/scripts.js" type="text/javascript"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_tags(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        theme_tag = context.get('theme_tag', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n    <div itemprop="keywords" class="tags right">\n        <span class=tags>\n            <span class=\'muted small\'> <i class="icon-tag"></i> </span>\n')
        for tag in post.tags:
            __M_writer('        <a\n')
            if theme_tag is not UNDEFINED:
                pass
                for (theme, tag_name) in theme_tag.items():
                    pass
                    if tag_name == tag:
                        __M_writer("                    class='small ")
                        __M_writer(str(theme))
                        __M_writer("'\n                    id='tag-theme' \n                    data-theme='")
                        __M_writer(str(theme))
                        __M_writer("'\n\n")
            __M_writer('        href="')
            __M_writer(str(_link('tag', tag)))
            __M_writer('" rel="tag">')
            __M_writer(str(tag))
            __M_writer('</a>\n')
        __M_writer('        </span>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        title = context.get('title', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if title and not post.meta('hidetitle'):
            __M_writer('    <h1 class="p-name entry-title" itemprop="headline name">')
            __M_writer(filters.html_escape(str(title)))
            __M_writer('</h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        len = context.get('len', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            pass
            for langname in translations.keys():
                pass
                if langname != lang and post.is_translation_available(langname):
                    __M_writer('                <a href="')
                    __M_writer(str(post.permalink(langname)))
                    __M_writer('" rel="alternate" hreflang="')
                    __M_writer(str(langname))
                    __M_writer('">\n                ')
                    __M_writer(str(messages("LANGUAGE", langname)))
                    __M_writer('</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_sourcelink(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if show_sourcelink:
            __M_writer('        &nbsp;&nbsp;|&nbsp;&nbsp;\n        <a href="')
            __M_writer(str(post.source_link()))
            __M_writer('" id="sourcelink">')
            __M_writer(str(messages("Source")))
            __M_writer('</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/lotabout/templates/zzz_helper.tmpl", "uri": "zzz_helper.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 2, "22": 61, "23": 84, "24": 98, "25": 119, "26": 143, "27": 149, "28": 160, "29": 167, "35": 3, "62": 3, "63": 6, "64": 7, "65": 8, "66": 10, "67": 11, "68": 13, "69": 14, "70": 15, "71": 17, "72": 18, "73": 21, "74": 21, "75": 21, "76": 24, "77": 25, "78": 25, "79": 25, "80": 27, "81": 28, "82": 28, "83": 28, "84": 28, "85": 30, "86": 30, "87": 31, "88": 31, "89": 32, "90": 33, "91": 33, "92": 33, "93": 35, "94": 36, "96": 37, "97": 38, "98": 38, "99": 38, "100": 38, "101": 38, "102": 38, "103": 38, "104": 41, "105": 42, "106": 43, "107": 43, "108": 43, "109": 45, "110": 46, "111": 47, "112": 47, "113": 47, "114": 49, "115": 50, "116": 50, "117": 50, "118": 52, "119": 53, "120": 53, "121": 54, "122": 55, "123": 56, "124": 57, "125": 57, "126": 57, "127": 59, "128": 60, "129": 60, "135": 63, "142": 63, "143": 64, "145": 65, "146": 66, "147": 68, "148": 69, "149": 72, "150": 73, "151": 80, "152": 81, "158": 86, "167": 86, "168": 87, "169": 88, "170": 88, "171": 88, "172": 89, "174": 90, "176": 91, "177": 92, "178": 92, "179": 92, "180": 92, "181": 92, "182": 94, "183": 95, "184": 95, "185": 95, "191": 100, "197": 100, "198": 101, "200": 102, "201": 103, "202": 105, "203": 106, "204": 108, "206": 109, "207": 110, "208": 112, "209": 113, "215": 122, "221": 122, "222": 127, "223": 128, "224": 129, "226": 130, "228": 131, "229": 132, "230": 132, "231": 132, "232": 134, "233": 134, "234": 139, "235": 139, "236": 139, "237": 139, "238": 139, "239": 141, "245": 145, "251": 145, "252": 146, "253": 147, "254": 147, "255": 147, "261": 151, "269": 151, "270": 152, "272": 153, "274": 154, "275": 155, "276": 155, "277": 155, "278": 155, "279": 155, "280": 156, "281": 156, "287": 162, "294": 162, "295": 163, "296": 164, "297": 165, "298": 165, "299": 165, "300": 165, "306": 300}}
__M_END_METADATA
"""
