# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1715183845.294906
_enable_loop = True
_template_filename = 'static/templates/index.txt'
_template_uri = 'index.txt'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html lang="fr">\r\n<head>\r\n    <meta charset="UTF-8">\r\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\r\n    <link rel="stylesheet" href="./static/css/styles_nav.css">\r\n    <link rel="stylesheet" href="./static/css/styles_index.css">\r\n    <title>TouchRugby</title>\r\n</head>\r\n<body>\r\n    <nav>\r\n        <a href="index.html">Accueil</a>\r\n        <!--INSERT MEMBER\'S PAGE-->\r\n<a href=\'equipe.html\'>Equipes</a><a href=\'joueurs.html\'>Joueurs</a>   </nav>\r\n\r\n    <section class="groupe">\r\n        <h1>Les équipes</h1>\r\n        <div class="listMember">\r\n            <!--ADD CARD-->\r\n<div class=\'card\'>      </div>\r\n    </section>\r\n</body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "static/templates/index.txt", "uri": "index.txt", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 1, "27": 21}}
__M_END_METADATA
"""
