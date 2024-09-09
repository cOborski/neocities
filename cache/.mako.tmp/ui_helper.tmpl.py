# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1725903920.664407
_enable_loop = True
_template_filename = 'C:/Python312/Lib/site-packages/nikola/data/themes/base/templates/ui_helper.tmpl'
_template_uri = 'ui_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['breadcrumbs']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_breadcrumbs(context,crumbs):
    __M_caller = context.caller_stack._push_frame()
    try:
        index_file = context.get('index_file', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if crumbs:
            __M_writer('<nav class="breadcrumbs">\n<ul class="breadcrumb">\n')
            for link, text in crumbs:
                pass
                if text != index_file:
                    pass
                    if link == '#':
                        __M_writer('                <li>')
                        __M_writer(str(text.rsplit('.html', 1)[0]))
                        __M_writer('</li>\n')
                    else:
                        __M_writer('                <li><a href="')
                        __M_writer(str(link))
                        __M_writer('">')
                        __M_writer(str(text))
                        __M_writer('</a></li>\n')
            __M_writer('</ul>\n</nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Python312/Lib/site-packages/nikola/data/themes/base/templates/ui_helper.tmpl", "uri": "ui_helper.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 18, "27": 2, "32": 2, "33": 3, "34": 4, "35": 6, "37": 7, "39": 8, "40": 9, "41": 9, "42": 9, "43": 10, "44": 11, "45": 11, "46": 11, "47": 11, "48": 11, "49": 15, "55": 49}}
__M_END_METADATA
"""
