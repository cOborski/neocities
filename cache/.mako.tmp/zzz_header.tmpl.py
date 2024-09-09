# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1725903920.5277684
_enable_loop = True
_template_filename = 'themes/lotabout/templates/zzz_header.tmpl'
_template_uri = 'zzz_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_header', 'html_site_title', 'html_navigation_links']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n\n')
        __M_writer('\n\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def html_navigation_links():
            return render_html_navigation_links(context)
        def html_site_title():
            return render_html_site_title(context)
        __M_writer = context.writer()
        __M_writer('\n\n    <header id="header" class="header transparent">\n        <div class="container">\n            <div class="scroll top">\n                <a href=\'#\'><i class="icon-chevron-up icon-large"></i></a>\n            </div>\n\n            ')
        __M_writer(str(html_site_title()))
        __M_writer('\n            ')
        __M_writer(str(html_navigation_links()))
        __M_writer('\n')
        __M_writer("        </div>\n        <div class='separator clearfix'></div>\n    </header>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_site_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        show_blog_title = _import_ns.get('show_blog_title', context.get('show_blog_title', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        blog_description = _import_ns.get('blog_description', context.get('blog_description', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    <div class="brand">\n        <div class="flip_container">\n            <div class="flipper">\n                <div class="front">\n                    <p><a href="')
        __M_writer(str(abs_link('/')))
        __M_writer('" title="')
        __M_writer(str(blog_title))
        __M_writer('" rel="home">\n')
        if logo_url:
            __M_writer('                        <img src="')
            __M_writer(str(logo_url))
            __M_writer('" alt="')
            __M_writer(str(blog_title))
            __M_writer('" id="logo">\n')
        __M_writer('\n')
        if show_blog_title:
            __M_writer('                        <span id="blog-title">')
            __M_writer(str(blog_title))
            __M_writer('</span>\n')
        __M_writer('                    </a></p>\n                </div>\n\n')
        if show_blog_title and blog_description:
            __M_writer('                <div class="back">\n                    <p><a href="')
            __M_writer(str(abs_link('/')))
            __M_writer('" title="')
            __M_writer(str(blog_description))
            __M_writer('" rel="home">\n                        <span id="blog-description">')
            __M_writer(str(blog_description))
            __M_writer('</span>\n                    </a></p>\n                </div>\t\t\t\n')
        __M_writer('            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        rel_link = _import_ns.get('rel_link', context.get('rel_link', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        tuple = _import_ns.get('tuple', context.get('tuple', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    <nav id="menu" role="navigation">\n    <ul>\n')
        for url, text in navigation_links[lang]:
            pass
            if isinstance(url, tuple):
                __M_writer('            <li> ')
                __M_writer(str(text))
                __M_writer('\n            <ul>\n')
                for suburl, text in url:
                    pass
                    if rel_link(permalink, suburl) == "#":
                        __M_writer('                    <li class="active"><a href="')
                        __M_writer(str(permalink))
                        __M_writer('">')
                        __M_writer(str(text))
                        __M_writer('</a></li>\n')
                    else:
                        __M_writer('                    <li><a href="')
                        __M_writer(str(suburl))
                        __M_writer('">')
                        __M_writer(str(text))
                        __M_writer('</a></li>\n')
                __M_writer('            </ul>\n')
            else:
                pass
                if rel_link(permalink, url) == "#":
                    __M_writer('                <li class="active"><a href="')
                    __M_writer(str(permalink))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer('</a></li>\n')
                else:
                    __M_writer('                <li><a href="')
                    __M_writer(str(url))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer('</a></li>\n')
        __M_writer('    ')
        __M_writer(str(template_hooks['menu']()))
        __M_writer('\n    ')
        __M_writer(str(template_hooks['menu_alt']()))
        __M_writer('\n    </ul>\n    </nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/lotabout/templates/zzz_header.tmpl", "uri": "zzz_header.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 0, "33": 2, "34": 22, "35": 51, "36": 81, "42": 4, "52": 4, "53": 12, "54": 12, "55": 13, "56": 13, "57": 19, "63": 25, "74": 25, "75": 30, "76": 30, "77": 30, "78": 30, "79": 31, "80": 32, "81": 32, "82": 32, "83": 32, "84": 32, "85": 34, "86": 35, "87": 36, "88": 36, "89": 36, "90": 38, "91": 41, "92": 42, "93": 43, "94": 43, "95": 43, "96": 43, "97": 44, "98": 44, "99": 48, "105": 54, "118": 54, "119": 57, "121": 58, "122": 59, "123": 59, "124": 59, "125": 61, "127": 62, "128": 63, "129": 63, "130": 63, "131": 63, "132": 63, "133": 64, "134": 65, "135": 65, "136": 65, "137": 65, "138": 65, "139": 68, "140": 69, "142": 70, "143": 71, "144": 71, "145": 71, "146": 71, "147": 71, "148": 72, "149": 73, "150": 73, "151": 73, "152": 73, "153": 73, "154": 77, "155": 77, "156": 77, "157": 78, "158": 78, "164": 158}}
__M_END_METADATA
"""
