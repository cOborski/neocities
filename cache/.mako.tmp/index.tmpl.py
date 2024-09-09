# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1725903920.7089546
_enable_loop = True
_template_filename = 'themes/lotabout/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='index_helper.tmpl', callables=None,  calling_uri=_template_uri)
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
        posts = context.get('posts', UNDEFINED)
        theme_tag = context.get('theme_tag', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        comments = _mako_get_namespace(context, 'comments')
        _link = context.get('_link', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        posts = context.get('posts', UNDEFINED)
        theme_tag = context.get('theme_tag', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        comments = _mako_get_namespace(context, 'comments')
        _link = context.get('_link', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n\n')
        for post in posts:
            __M_writer('    <div class="post-entry">\n        <div class="num-of-comments">\n')
            if not post.meta('nocomments'):
                __M_writer('                ')
                __M_writer(str(comments.comment_link(post.permalink(), post.base_path)))
                __M_writer('\n')
            __M_writer('        </div>\n        <div class="info">\n            <div class="title"><a\n            href="')
            __M_writer(str(post.permalink()))
            __M_writer('">')
            __M_writer(str(post.title()))
            __M_writer('</a></div>\n            <div class="tags">\n                <ul>\n')
            for tag in post.tags:
                __M_writer('                    <li>\n                    <a \n')
                if theme_tag is not UNDEFINED:
                    pass
                    for (theme, tag_name) in theme_tag.items():
                        pass
                        if tag_name == tag:
                            __M_writer("                                class='tag-theme ")
                            __M_writer(str(theme))
                            __M_writer("'\n")
                __M_writer('                    href="')
                __M_writer(str(_link('tag', tag)))
                __M_writer('" rel="tag">')
                __M_writer(str(tag))
                __M_writer('</a>\n                    </li>\n')
            __M_writer('                </ul>\n            </div>\n            <time class="timeago" datetime="')
            __M_writer(str(post.date.isoformat()))
            __M_writer('">')
            __M_writer(str(post.formatted_date('%Y-%m-%d')))
            __M_writer('</time>\n            <div class="description"> ')
            __M_writer(str(post.description()))
            __M_writer(' </div>\n        </div>\n    </div>\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n    ')
        __M_writer(str(helper.html_pager()))
        __M_writer('\n    ')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n    ')
        __M_writer(str(helper.mathjax_script(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/lotabout/templates/index.tmpl", "uri": "index.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "32": 0, "44": 2, "45": 3, "46": 4, "51": 106, "57": 6, "68": 6, "69": 9, "70": 10, "71": 12, "72": 14, "73": 14, "74": 14, "75": 16, "76": 19, "77": 19, "78": 19, "79": 19, "80": 22, "81": 23, "82": 25, "84": 26, "86": 27, "87": 28, "88": 28, "89": 28, "90": 32, "91": 32, "92": 32, "93": 32, "94": 32, "95": 35, "96": 37, "97": 37, "98": 37, "99": 37, "100": 38, "101": 38, "102": 42, "103": 50, "104": 54, "105": 68, "106": 78, "107": 102, "108": 103, "109": 103, "110": 104, "111": 104, "112": 105, "113": 105, "119": 113}}
__M_END_METADATA
"""
