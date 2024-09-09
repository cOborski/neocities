# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1725903920.4255586
_enable_loop = True
_template_filename = 'C:/Python312/Lib/site-packages/nikola/data/themes/base/templates/comments_helper.tmpl'
_template_uri = 'comments_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_form', 'comment_link', 'comment_link_script']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('comments_helper_impl', context._clean_inheritance_tokens(), templateuri='comments_helper_' + (context['comment_system']) + '.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments_helper_impl')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comments_helper_impl = _mako_get_namespace(context, 'comments_helper_impl')
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(comments_helper_impl.comment_form(url, title, identifier)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comments_helper_impl = _mako_get_namespace(context, 'comments_helper_impl')
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(comments_helper_impl.comment_link(link, identifier)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        comments_helper_impl = _mako_get_namespace(context, 'comments_helper_impl')
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(comments_helper_impl.comment_link_script()))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Python312/Lib/site-packages/nikola/data/themes/base/templates/comments_helper.tmpl", "uri": "comments_helper.tmpl", "source_encoding": "utf-8", "line_map": {"23": 3, "26": 0, "31": 2, "32": 3, "33": 7, "34": 11, "35": 15, "41": 5, "46": 5, "47": 6, "48": 6, "54": 9, "59": 9, "60": 10, "61": 10, "67": 13, "72": 13, "73": 14, "74": 14, "80": 74}}
__M_END_METADATA
"""
