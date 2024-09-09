# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1725903920.5402863
_enable_loop = True
_template_filename = 'themes/lotabout/templates/zzz_footer.tmpl'
_template_uri = 'zzz_footer.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_footer']


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
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_footer(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        email = _import_ns.get('email', context.get('email', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        github = _import_ns.get('github', context.get('github', UNDEFINED))
        content_footer = _import_ns.get('content_footer', context.get('content_footer', UNDEFINED))
        twitter = _import_ns.get('twitter', context.get('twitter', UNDEFINED))
        html_feedlinks = _import_ns.get('html_feedlinks', context.get('html_feedlinks', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n\n    <footer class=\'footer\'>\n        <div class="container clearfix">\n            <div class="social pull-left">\n                <ul>\n')
        if email:
            __M_writer('                    <a href="mailto:')
            __M_writer(str(email))
            __M_writer('" target="_blank">\n                        <li><i class="icon-envelope icon-large"></i> \n                        </li>\n                    </a>\n')
        __M_writer('\n')
        if twitter:
            __M_writer('                    <a href="http://twitter.com/')
            __M_writer(str(twitter))
            __M_writer('" target="_blank">\n                        <li><i class="icon-twitter-sign icon-large"></i>\n                        </li>\n                    </a>\n')
        __M_writer('\n')
        if github:
            __M_writer('                    <a href="https://github.com/')
            __M_writer(str(github))
            __M_writer('" target="_blank">\n                        <li><i class="icon-github-sign icon-large"></i>\n                        </li>\n                    </a>\n')
        __M_writer('\n                    ')
        __M_writer(str(html_feedlinks()))
        __M_writer('\n\n                    <a href="')
        __M_writer(str(_link('rss', None, lang)))
        __M_writer('" target="_blank">\n                        <li> <i class="icon-rss icon-large"></i> \n                        </li>\n                    </a>\n                </ul>\n            </div>\n')
        if content_footer:
            __M_writer('            <div class="copyright pull-right">\n                <p>')
            __M_writer(str(content_footer))
            __M_writer('</p>\n                ')
            __M_writer(str(template_hooks['page_footer']()))
            __M_writer('\n            </div>\n')
        __M_writer('            ')
        __M_writer(str(template_hooks['page_footer']()))
        __M_writer('\n        </div>\n    </footer>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/lotabout/templates/zzz_footer.tmpl", "uri": "zzz_footer.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 0, "33": 2, "34": 48, "40": 4, "54": 4, "55": 10, "56": 11, "57": 11, "58": 11, "59": 16, "60": 17, "61": 18, "62": 18, "63": 18, "64": 23, "65": 24, "66": 25, "67": 25, "68": 25, "69": 30, "70": 31, "71": 31, "72": 33, "73": 33, "74": 39, "75": 40, "76": 41, "77": 41, "78": 42, "79": 42, "80": 45, "81": 45, "82": 45, "88": 82}}
__M_END_METADATA
"""
