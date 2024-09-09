# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1725903920.4511676
_enable_loop = True
_template_filename = 'themes/lotabout/templates/post.tmpl'
_template_uri = 'post.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('zzz', context._clean_inheritance_tokens(), templateuri='zzz_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'zzz')] = ns

    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'zzz')._populate(_import_ns, ['*'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        helper = _mako_get_namespace(context, 'helper')
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        zzz = _mako_get_namespace(context, 'zzz')
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'zzz')._populate(_import_ns, ['*'])
        helper = _mako_get_namespace(context, 'helper')
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        def extra_head():
            return render_extra_head(context)
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if post.meta('keywords'):
            __M_writer('        <meta name="keywords" content="')
            __M_writer(filters.html_escape(str(post.meta('keywords'))))
            __M_writer('">\n')
        __M_writer('    <meta name="author" content="')
        __M_writer(str(post.author()))
        __M_writer('">\n    ')
        __M_writer(str(helper.open_graph_metadata(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.twitter_card_information(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.meta_translations(post)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'zzz')._populate(_import_ns, ['*'])
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        helper = _mako_get_namespace(context, 'helper')
        zzz = _mako_get_namespace(context, 'zzz')
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n    <div class="post">\n    ')
        __M_writer(str(zzz.html_title()))
        __M_writer('\n        <div class="meta clearfix">\n            <div class="authordate left">\n                <time class="timeago" datetime="')
        __M_writer(str(post.date.isoformat()))
        __M_writer('">')
        __M_writer(str(post.formatted_date('%Y/%m/%d')))
        __M_writer('</time>\n            ')
        __M_writer(str(zzz.html_translations(post)))
        __M_writer('\n            ')
        __M_writer(str(zzz.html_sourcelink()))
        __M_writer('\n            </div>\n            ')
        __M_writer(str(zzz.html_tags(post)))
        __M_writer('\n        </div>\n        ')
        __M_writer(str(post.text()))
        __M_writer('\n        ')
        __M_writer(str(helper.html_pager(post)))
        __M_writer('\n')
        if not post.meta('nocomments') and site_has_comments:
            __M_writer('            ')
            __M_writer(str(comments.comment_form(post.permalink(absolute=True), post.title(), post._base_path)))
            __M_writer('\n')
        __M_writer('        ')
        __M_writer(str(helper.mathjax_script(post)))
        __M_writer('\n    </div>\n')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/lotabout/templates/post.tmpl", "uri": "post.tmpl", "source_encoding": "utf-8", "line_map": {"23": 3, "26": 4, "29": 5, "35": 0, "52": 1, "53": 3, "54": 4, "55": 5, "56": 6, "61": 17, "66": 38, "72": 8, "83": 8, "84": 9, "85": 9, "86": 10, "87": 11, "88": 11, "89": 11, "90": 13, "91": 13, "92": 13, "93": 14, "94": 14, "95": 15, "96": 15, "97": 16, "98": 16, "104": 19, "117": 19, "118": 21, "119": 21, "120": 24, "121": 24, "122": 24, "123": 24, "124": 25, "125": 25, "126": 26, "127": 26, "128": 28, "129": 28, "130": 30, "131": 30, "132": 31, "133": 31, "134": 32, "135": 33, "136": 33, "137": 33, "138": 35, "139": 35, "140": 35, "141": 37, "142": 37, "148": 142}}
__M_END_METADATA
"""
