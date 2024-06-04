# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1717493956.662872
_enable_loop = True
_template_filename = 'static/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        poste = context.get('poste', UNDEFINED)
        clermont_compo = context.get('clermont_compo', UNDEFINED)
        events = context.get('events', UNDEFINED)
        toulouse_compo = context.get('toulouse_compo', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n\r\n<head>\r\n  <!-- Basic -->\r\n  <meta charset="utf-8" />\r\n  <meta http-equiv="X-UA-Compatible" content="IE=edge" />\r\n  <!-- Mobile Metas -->\r\n  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />\r\n  <!-- Site Metas -->\r\n  <meta name="keywords" content="" />\r\n  <meta name="description" content="" />\r\n  <meta name="author" content="" />\r\n\r\n  <title>TouchRugby</title>\r\n\r\n\r\n  <!-- bootstrap core css -->\r\n  <link rel="stylesheet" type="text/css" href="/static/css/bootstrap.css" />\r\n\r\n  <!-- fonts style -->\r\n  <link href="/static/css/fonts2.css" rel="stylesheet">\r\n\r\n  <!-- font awesome style -->\r\n  <link href="/static/css/font-awesome.min.css" rel="stylesheet" />\r\n  <!-- nice select -->\r\n  <link rel="stylesheet" href="/static/css/fonts1.css" integrity="sha256-mLBIhmBvigTFWPSCtvdu6a76T+3Xyt+K571hupeFLg4=" crossorigin="anonymous" />\r\n\r\n  <!-- Custom styles for this template -->\r\n  <link href="/static/css/style.css" rel="stylesheet"/>\r\n  <link href="/static/css/match_direct.css" rel="stylesheet"/>\r\n  <link href="/static/css/compo.css" rel="stylesheet"/>\r\n  <!-- responsive style -->\r\n  <link href="/static/css/responsive.css" rel="stylesheet" />\r\n\r\n</head>\r\n\r\n<body>\r\n\r\n  <div class="hero_area">\r\n    <!-- header section strats -->\r\n    <header class="header_section">\r\n      <div class="container-fluid">\r\n        <nav class="navbar navbar-expand-lg custom_nav-container ">\r\n          <a class="navbar-brand" href="index">\r\n            <span>\r\n              TouchRugby\r\n            </span>\r\n          </a>\r\n\r\n          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">\r\n            <span class=""> </span>\r\n          </button>\r\n\r\n          <div class="collapse navbar-collapse" id="navbarSupportedContent">\r\n            <ul class="navbar-nav  ml-auto">\r\n              <li class="nav-item active">\r\n                <a class="nav-link" href="index">Home</a>\r\n              </li>\r\n              <li class="nav-item">\r\n                <a class="nav-link" href="equipe"> Equipes</a>\r\n              </li>\r\n              <li class="nav-item">\r\n                <a class="nav-link" href="joueur">Joueurs</a>\r\n                <div class="dropdown-content">\r\n                    <a href="/get_joueur">Liste des joueurs</a>\r\n                    <div class="dropdown-submenu">\r\n                      <!-- Menu déroulant pour choisir le poste -->\r\n                      <select id="posteDropdown" onchange="window.location.href=this.value;">\r\n                          <option value="#">Liste des joueurs par poste</option>\r\n')
        for postes in poste : 
            __M_writer('                          <option value="/joueur_par_poste?poste=')
            __M_writer(str(postes[0]))
            __M_writer('">')
            __M_writer(str(postes[0]))
            __M_writer('</option>\r\n')
        __M_writer('                      </select>\r\n                  </div>\r\n                    <a href="/joueur_par_age">Liste des joueurs par âge</a>\r\n                    <form action="/joueur_par_nom" method="get">\r\n                      <label for="nom">Nom du joueur :</label>\r\n                      <input type="text" id="nom" name="nom" required>\r\n                      <button type="submit">Chercher</button>\r\n                  </form>\r\n                </div>\r\n            </li>\r\n              <li class="nav-item">\r\n                <a class="nav-link" href="matchs">Matchs</a>\r\n              </li>\r\n              <li class="nav-item">\r\n                <a class="nav-link" href="#">\r\n                  <i class="fa fa-user" aria-hidden="true"></i>\r\n                  <span>\r\n                    Login\r\n                  </span>\r\n                </a>\r\n              </li>\r\n              <li class="nav-item">\r\n                <a class="nav-link" href="#">\r\n                  <i class="fa fa-user" aria-hidden="true"></i>\r\n                  <span>\r\n                    Sign Up\r\n                  </span>\r\n                </a>\r\n              </li>\r\n              <form class="form-inline">\r\n                <button class="btn   nav_search-btn" type="submit">\r\n                  <i class="fa fa-search" aria-hidden="true"></i>\r\n                </button>\r\n              </form>\r\n            </ul>\r\n          </div>\r\n        </nav>\r\n      </div>\r\n    </header>\r\n    <!-- end header section -->\r\n  <!-- live match simulation section -->\r\n  <section class="job_section layout_padding">\r\n    <div class="container">\r\n      <div class="header">\r\n        <div class="team-info">\r\n          <img src="/static/images/logo_6.png" alt="Team A Logo">\r\n          <h2>Clermont</h2>\r\n        </div>\r\n        <div class="scoreboard" id="scoreboard">20 - 28</div>\r\n        <div class="team-info">\r\n          <h2>Toulouse</h2>\r\n          <img src="/static/images/logo_14.png" alt="Team B Logo">\r\n        </div>\r\n      </div>\r\n      <div class="main">\r\n        <div class="field" id="field">\r\n          <div class="team-composition" id="team-composition-clermont">\r\n            <h3>Clermont Composition</h3>\r\n            <ul id="clermont-players">\r\n')
        for joueur in clermont_compo:
            __M_writer('              <li>')
            __M_writer(str(joueur[0]))
            __M_writer(' ')
            __M_writer(str(joueur[1]))
            __M_writer('</li>\r\n')
        __M_writer('            </ul>\r\n          </div>\r\n          <div class="team-composition" id="team-composition-toulouse">\r\n            <h3>Toulouse Composition</h3>\r\n            <ul id="toulouse-players">\r\n')
        for joueur in toulouse_compo:
            __M_writer('              <li>')
            __M_writer(str(joueur[0]))
            __M_writer(' ')
            __M_writer(str(joueur[1]))
            __M_writer('</li>\r\n')
        __M_writer('            </ul>\r\n          </div>\r\n        </div>\r\n        <div class="events-log" id="events-log">\r\n          <h3>Events</h3>\r\n          <ul id="events"></ul>\r\n')
        for event in events :
            __M_writer('            <li>')
            __M_writer(str(event['time']))
            __M_writer('- ')
            __M_writer(str(event['team']))
            __M_writer(' - ')
            __M_writer(str(event['event']))
            __M_writer(' - ')
            __M_writer(str(event['player']))
            __M_writer('</li>\r\n')
        __M_writer('        </div>\r\n        <div class="stats">\r\n          <h3>Stats</h3>\r\n          <p id="possession">Possession: 50% - 50%</p>\r\n        </div>\r\n      </div>\r\n    </div>\r\n  </section>\r\n\r\n  <!-- end live match simulation section -->\r\n\r\n  <!-- info section -->\r\n  <section class="info_section ">\r\n    <div class="container">\r\n      <div class="row">\r\n        <div class="col-md-2 info_links">\r\n          <img src="images/top14.jpg"/>\r\n        </div>\r\n        <div class="col-md-3">\r\n        </div>\r\n      </div>\r\n        <div class="col-md-3">\r\n          \r\n          </div>\r\n        </div>\r\n      </div>\r\n    </div>\r\n  </section>\r\n  <!-- end info_section -->\r\n\r\n\r\n  <!-- footer section -->\r\n  <footer class="footer_section">\r\n    <div class="container">\r\n      <p>\r\n        &copy; <span id="displayYear"></span> All Rights Reserved By\r\n      </p>\r\n    </div>\r\n  </footer>\r\n  <!-- footer section -->\r\n\r\n  <!-- jQery -->\r\n  <script src="/static/js/jquery-3.4.1.min.js"></script>\r\n  <!-- bootstrap js -->\r\n  <script src="/static/js/bootstrap.js"></script>\r\n  <!-- nice select -->\r\n  <script src="/static/js/internet.js" integrity="sha256-Zr3vByTlMGQhvMfgkQ5BtWRSKBGa2QlspKYJnkjZTmo=" crossorigin="anonymous"></script>\r\n  <!-- custom js -->\r\n  <script src="/static/js/custom.js"></script>\r\n\r\n\r\n</body>\r\n\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "static/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"16": 0, "25": 1, "26": 71, "27": 72, "28": 72, "29": 72, "30": 72, "31": 72, "32": 74, "33": 133, "34": 134, "35": 134, "36": 134, "37": 134, "38": 134, "39": 136, "40": 141, "41": 142, "42": 142, "43": 142, "44": 142, "45": 142, "46": 144, "47": 150, "48": 151, "49": 151, "50": 151, "51": 151, "52": 151, "53": 151, "54": 151, "55": 151, "56": 151, "57": 153, "63": 57}}
__M_END_METADATA
"""
