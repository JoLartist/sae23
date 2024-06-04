# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1717493969.899773
_enable_loop = True
_template_filename = 'static/templates/matchs.html'
_template_uri = 'matchs.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        poste = context.get('poste', UNDEFINED)
        matchs = context.get('matchs', UNDEFINED)
        equipe = context.get('equipe', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n\r\n<head>\r\n  <!-- Basic -->\r\n  <meta charset="utf-8" />\r\n  <meta http-equiv="X-UA-Compatible" content="IE=edge" />\r\n  <!-- Mobile Metas -->\r\n  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />\r\n  <!-- Site Metas -->\r\n  <meta name="keywords" content="" />\r\n  <meta name="description" content="" />\r\n  <meta name="author" content="" />\r\n\r\n  <title>TouchRugby</title>\r\n\r\n\r\n  <!-- bootstrap core css -->\r\n  <link rel="stylesheet" type="text/css" href="/static/css/bootstrap.css" />\r\n\r\n  <!-- fonts style -->\r\n  <link href="/static/css/fonts2.css" rel="stylesheet">\r\n\r\n  <!-- font awesome style -->\r\n  <link href="/static/css/font-awesome.min.css" rel="stylesheet" />\r\n  <!-- nice select -->\r\n  <link rel="stylesheet" href="/static/css/fonts1.css" integrity="sha256-mLBIhmBvigTFWPSCtvdu6a76T+3Xyt+K571hupeFLg4=" crossorigin="anonymous" />\r\n\r\n  <!-- Custom styles for this template -->\r\n  <link href="/static/css/style.css" rel="stylesheet" />\r\n  <link href="/static/css/match_direct.css" rel="stylesheet"/>\r\n  <link href="/static/css/compo.css" rel="stylesheet"/>\r\n  <!-- responsive style -->\r\n  <link href="/static/css/responsive.css" rel="stylesheet" />\r\n\r\n</head>\r\n<style>\r\n  h3 {\r\n    text-align: center;\r\n  }\r\n</style>\r\n\r\n<body class="sub_page">\r\n\r\n  <div class="hero_area">\r\n    <!-- header section strats -->\r\n    <header class="header_section">\r\n      <div class="container-fluid">\r\n        <nav class="navbar navbar-expand-lg custom_nav-container ">\r\n          <a class="navbar-brand" href="index">\r\n            <span>\r\n              TouchRugby\r\n            </span>\r\n          </a>\r\n\r\n          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">\r\n            <span class=""> </span>\r\n          </button>\r\n\r\n          <div class="collapse navbar-collapse" id="navbarSupportedContent">\r\n            <ul class="navbar-nav  ml-auto">\r\n              <li class="nav-item active">\r\n                <a class="nav-link" href="index">Home</a>\r\n              </li>\r\n              <li class="nav-item">\r\n                <a class="nav-link" href="equipe"> Equipes</a>\r\n              </li>\r\n              <li class="nav-item">\r\n                <a class="nav-link" href="joueur">Joueurs</a>\r\n                <div class="dropdown-content">\r\n                    <a href="/get_joueur">Liste des joueurs</a>\r\n                    <div class="dropdown-submenu">\r\n                      <!-- Menu déroulant pour choisir le poste -->\r\n                      <select id="posteDropdown" onchange="window.location.href=this.value;">\r\n                          <option value="#">Liste des joueurs par poste</option>\r\n')
        for postes in poste : 
            __M_writer('                          <option value="/joueur_par_poste?poste=')
            __M_writer(str(postes[0]))
            __M_writer('">')
            __M_writer(str(postes[0]))
            __M_writer('</option>\r\n')
        __M_writer('                      </select>\r\n                  </div>\r\n                    <a href="/joueur_par_age">Liste des joueurs par âge</a>\r\n                    <form action="/joueur_par_nom" method="get">\r\n                      <label for="nom">Nom du joueur :</label>\r\n                      <input type="text" id="nom" name="nom" required>\r\n                      <button type="submit">Chercher</button>\r\n                  </form>\r\n                </div>\r\n            </li>\r\n              <li class="nav-item">\r\n                <a class="nav-link" href="matchs">Matchs</a>\r\n              </li>\r\n              <li class="nav-item">\r\n                <a class="nav-link" href="#">\r\n                  <i class="fa fa-user" aria-hidden="true"></i>\r\n                  <span>\r\n                    Login\r\n                  </span>\r\n                </a>\r\n              </li>\r\n              <li class="nav-item">\r\n                <a class="nav-link" href="#">\r\n                  <i class="fa fa-user" aria-hidden="true"></i>\r\n                  <span>\r\n                    Sign Up\r\n                  </span>\r\n                </a>\r\n              </li>\r\n              <form class="form-inline">\r\n                <button class="btn   nav_search-btn" type="submit">\r\n                  <i class="fa fa-search" aria-hidden="true"></i>\r\n                </button>\r\n              </form>\r\n            </ul>\r\n          </div>\r\n        </nav>\r\n      </div>\r\n    </header>\r\n    <!-- end header section -->\r\n  </div>\r\n')
        for match in matchs :
            __M_writer('  <section class="job_section layout_padding">\r\n      <div class="container">\r\n        <div class="header">\r\n          <div class="team-info">\r\n            <img src="/static/images/logo_')
            __M_writer(str(match[1]))
            __M_writer('.png" alt="Team A Logo">\r\n          </div>\r\n          <div class="scoreboard" id="scoreboard">')
            __M_writer(str(match[4]))
            __M_writer('</div>\r\n          <div class="team-info">\r\n            <img src="/static/images/logo_')
            __M_writer(str(match[2]))
            __M_writer('.png" alt="Team B Logo">\r\n          </div>\r\n        </div>\r\n      </div>\r\n      <h3 class="date_match">')
            __M_writer(str(match[3]))
            __M_writer('</h3>\r\n    </section>\r\n')
        __M_writer('\r\n  <button id="showFormsButton">Administrateur</button>\r\n\r\n  <div id="formsContainer" class="form-container">\r\n                  <h2>Insérer un nouveau match</h2>\r\n                <form method="post" action="insert_matchs">\r\n                  <label for="dom">Équipe Domicile:</label>\r\n                  <select id="dom" name="dom" required>\r\n')
        for equipes in equipe : 
            __M_writer('                    <option value="')
            __M_writer(str(equipes[0]))
            __M_writer('">')
            __M_writer(str(equipes[1]))
            __M_writer('</option>\r\n')
        __M_writer('                  </select><br>\r\n                  \r\n                  <label for="ext">Équipe Extérieure:</label>\r\n                  <select id="ext" name="ext" required>\r\n')
        for equipes in equipe : 
            __M_writer('                    <option value="')
            __M_writer(str(equipes[0]))
            __M_writer('">')
            __M_writer(str(equipes[1]))
            __M_writer('</option>\r\n')
        __M_writer('                  </select><br>\r\n                    \r\n                    <label for="date">Date (YYYY-MM-DD):</label>\r\n                    <input type="date" id="date" name="date" required><br>\r\n                    \r\n                    <label for="result">Résultat:</label>\r\n                    <input type="text" id="result" name="result" required><br>\r\n                    \r\n                    <input type="submit" value="Insérer le match">\r\n                </form>\r\n\r\n                <h1>Delete Match</h1>\r\n                <form action="/delete_match" method="post">\r\n                    <label for="match_id">Score du match :</label><br>\r\n                    <select id="match_id" name="match_id" required>\r\n')
        for match in matchs :
            __M_writer('                      <option value="')
            __M_writer(str(match[0]))
            __M_writer('">')
            __M_writer(str(match[4]))
            __M_writer('</option>\r\n')
        __M_writer('                    </select><br>\r\n                    <button type="submit">Delete Match</button>\r\n                </form>\r\n            </div>\r\n\r\n  <!-- info section -->\r\n  <section class="info_section ">\r\n    <div class="container">\r\n      <div class="row">\r\n        <div class="col-md-2 info_links">\r\n          <img src="images/top14.jpg"/>\r\n        </div>\r\n        <div class="col-md-3">\r\n        </div>\r\n      </div>\r\n        <div class="col-md-3">\r\n          \r\n          </div>\r\n        </div>\r\n      </div>\r\n    </div>\r\n  </section>\r\n  <!-- end info_section -->\r\n\r\n  <!-- footer section -->\r\n  <footer class="footer_section">\r\n    <div class="container">\r\n      <p>\r\n        &copy; <span id="displayYear"></span> All Rights Reserved By\r\n      </p>\r\n    </div>\r\n  </footer>\r\n  <!-- footer section -->\r\n\r\n  <!-- jQery -->\r\n  <script src="/static/js/jquery-3.4.1.min.js"></script>\r\n  <!-- bootstrap js -->\r\n  <script src="/static/js/bootstrap.js"></script>\r\n  <!-- nice select -->\r\n  <script src="/static/js/internet.js" integrity="sha256-Zr3vByTlMGQhvMfgkQ5BtWRSKBGa2QlspKYJnkjZTmo=" crossorigin="anonymous"></script>\r\n  <!-- custom js -->\r\n  <script src="/static/js/custom.js"></script>\r\n  <script src="/static/js/bouton.js"></script>\r\n\r\n</body>\r\n\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "static/templates/matchs.html", "uri": "matchs.html", "source_encoding": "utf-8", "line_map": {"16": 0, "24": 1, "25": 76, "26": 77, "27": 77, "28": 77, "29": 77, "30": 77, "31": 79, "32": 120, "33": 121, "34": 125, "35": 125, "36": 127, "37": 127, "38": 129, "39": 129, "40": 133, "41": 133, "42": 136, "43": 144, "44": 145, "45": 145, "46": 145, "47": 145, "48": 145, "49": 147, "50": 151, "51": 152, "52": 152, "53": 152, "54": 152, "55": 152, "56": 154, "57": 169, "58": 170, "59": 170, "60": 170, "61": 170, "62": 170, "63": 172, "69": 63}}
__M_END_METADATA
"""
