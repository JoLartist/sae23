# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1717493811.202462
_enable_loop = True
_template_filename = 'static/templates/joueur.html'
_template_uri = 'joueur.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        poste = context.get('poste', UNDEFINED)
        equipes = context.get('equipes', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n\r\n<head>\r\n  <!-- Basic -->\r\n  <meta charset="utf-8" />\r\n  <meta http-equiv="X-UA-Compatible" content="IE=edge" />\r\n  <!-- Mobile Metas -->\r\n  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />\r\n  <!-- Site Metas -->\r\n  <meta name="keywords" content="" />\r\n  <meta name="description" content="" />\r\n  <meta name="author" content="" />\r\n\r\n  <title>TouchRugby</title>\r\n\r\n\r\n  <!-- bootstrap core css -->\r\n  <link rel="stylesheet" type="text/css" href="/static/css/bootstrap.css" />\r\n\r\n  <!-- fonts style -->\r\n  <link href="/static/css/fonts2.css" rel="stylesheet">\r\n\r\n  <!-- font awesome style -->\r\n  <link href="/static/css/font-awesome.min.css" rel="stylesheet" />\r\n  <!-- nice select -->\r\n  <link rel="stylesheet" href="/static/css/fonts1.css" integrity="sha256-mLBIhmBvigTFWPSCtvdu6a76T+3Xyt+K571hupeFLg4=" crossorigin="anonymous" />\r\n\r\n  <!-- Custom styles for this template -->\r\n  <link href="/static/css/style.css" rel="stylesheet" />\r\n  <!-- responsive style -->\r\n  <link href="/static/css/responsive.css" rel="stylesheet" />\r\n\r\n</head>\r\n\r\n<body class="sub_page">\r\n\r\n  <div class="hero_area">\r\n    <!-- header section strats -->\r\n    <header class="header_section">\r\n      <div class="container-fluid">\r\n        <nav class="navbar navbar-expand-lg custom_nav-container ">\r\n          <a class="navbar-brand" href="index">\r\n            <span>\r\n              TouchRugby\r\n            </span>\r\n          </a>\r\n\r\n          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">\r\n            <span class=""> </span>\r\n          </button>\r\n\r\n          <div class="collapse navbar-collapse" id="navbarSupportedContent">\r\n            <ul class="navbar-nav  ml-auto">\r\n              <li class="nav-item active">\r\n                <a class="nav-link" href="index">Home</a>\r\n              </li>\r\n              <li class="nav-item">\r\n                <a class="nav-link" href="equipe"> Equipes</a>\r\n              </li>\r\n              <li class="nav-item">\r\n                <a class="nav-link" href="joueur">Joueurs</a>\r\n                <div class="dropdown-content">\r\n                    <a href="/get_joueur">Liste des joueurs</a>\r\n                    <div class="dropdown-submenu">\r\n                      <!-- Menu déroulant pour choisir le poste -->\r\n                      <select id="posteDropdown" onchange="window.location.href=this.value;">\r\n                          <option value="#">Liste des joueurs par poste</option>\r\n')
        for postes in poste : 
            __M_writer('                          <option value="/joueur_par_poste?poste=')
            __M_writer(str(postes[0]))
            __M_writer('">')
            __M_writer(str(postes[0]))
            __M_writer('</option>\r\n')
        __M_writer('                          <!-- Ajoutez d\'autres options si nécessaire -->\r\n                      </select>\r\n                  </div>\r\n                    <a href="/joueur_par_age">Liste des joueurs par âge</a>\r\n                    <form action="/joueur_par_nom" method="get">\r\n                      <label for="nom">Nom du joueur :</label>\r\n                      <input type="text" id="nom" name="nom" required>\r\n                      <button type="submit">Chercher</button>\r\n                  </form>\r\n                </div>\r\n            </li>\r\n              <li class="nav-item">\r\n                <a class="nav-link" href="matchs">Matchs</a>\r\n              </li>\r\n              <li class="nav-item">\r\n                <a class="nav-link" href="#">\r\n                  <i class="fa fa-user" aria-hidden="true"></i>\r\n                  <span>\r\n                    Login\r\n                  </span>\r\n                </a>\r\n              </li>\r\n              <li class="nav-item">\r\n                <a class="nav-link" href="#">\r\n                  <i class="fa fa-user" aria-hidden="true"></i>\r\n                  <span>\r\n                    Sign Up\r\n                  </span>\r\n                </a>\r\n              </li>\r\n              <form class="form-inline">\r\n                <button class="btn   nav_search-btn" type="submit">\r\n                  <i class="fa fa-search" aria-hidden="true"></i>\r\n                </button>\r\n              </form>\r\n            </ul>\r\n          </div>\r\n        </nav>\r\n      </div>\r\n    </header>\r\n    <!-- end header section -->\r\n    <div class="containerImg">\r\n      <img src="/static/images/imageIndex.jpg" class="img-responsive rounded transition">\r\n  </div>\r\n  <button id="showFormsButton">Administrateur</button>\r\n    <div id="formsContainer" class="form-container">\r\n        <h1>Insérer un nouveau joueur</h1>\r\n          <form action="/insert_joueur" method="post">\r\n              <label for="nom">Nom du joueur :</label>\r\n              <input type="text" id="nom" name="nom" required><br><br>\r\n\r\n              <label for="dateNaissance">Date de naissance :</label>\r\n              <input type="date" id="dateNaissance" name="dateNaissance" required><br><br>\r\n\r\n              <label for="poste">Poste :</label>\r\n              <select id="poste" name="poste" required>\r\n')
        for postes in poste :
            __M_writer('                  <option value="')
            __M_writer(str(postes[0]))
            __M_writer('">')
            __M_writer(str(postes[0]))
            __M_writer('</option>\r\n')
        __M_writer('              </select><br><br>\r\n\r\n              <label for="idEquipe">ID de l\'équipe :</label>\r\n              <select id="idEquipe" name="idEquipe" required>\r\n')
        for equipe in equipes :
            __M_writer('                  <option value="')
            __M_writer(str(equipe[0]))
            __M_writer('">')
            __M_writer(str(equipe[1]))
            __M_writer('</option>\r\n')
        __M_writer('              </select><br><br>\r\n            </form>\r\n\r\n              <button type="submit">Insérer</button>\r\n\r\n              <h1>Supprimer un joueur</h1>\r\n          <form action="/delete_joueur" method="post">\r\n              <label for="nom">Nom du joueur :</label>\r\n              <input type="text" id="nom" name="nom" required><br><br>\r\n\r\n              <button type="submit">Supprimer</button>\r\n          </form>\r\n    </div>\r\n  </div>\r\n\r\n        \r\n        \r\n  \r\n  <!-- info section -->\r\n  <section class="info_section ">\r\n    <div class="container">\r\n      <div class="row">\r\n        <div class="col-md-2 info_links">\r\n          <img src="images/top14.jpg"/>\r\n        </div>\r\n        <div class="col-md-3">\r\n        </div>\r\n      </div>\r\n        <div class="col-md-3">\r\n          \r\n          </div>\r\n        </div>\r\n      </div>\r\n    </div>\r\n  </section>\r\n  <!-- end info_section -->\r\n\r\n\r\n  <!-- footer section -->\r\n  <footer class="footer_section">\r\n    <div class="container">\r\n      <p>\r\n        &copy; <span id="displayYear"></span> All Rights Reserved By\r\n    </div>\r\n  </footer>\r\n  <!-- footer section -->\r\n\r\n  <!-- jQery -->\r\n  <script src="/static/js/jquery-3.4.1.min.js"></script>\r\n  <!-- bootstrap js -->\r\n  <script src="/static/js/bootstrap.js"></script>\r\n  <!-- nice select -->\r\n  <script src="/static/js/internet.js" integrity="sha256-Zr3vByTlMGQhvMfgkQ5BtWRSKBGa2QlspKYJnkjZTmo=" crossorigin="anonymous"></script>\r\n  <!-- custom js -->\r\n  <script src="/static/js/custom.js"></script>\r\n  <script src="/static/js/bouton.js"></script>\r\n\r\n</body>\r\n\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "static/templates/joueur.html", "uri": "joueur.html", "source_encoding": "utf-8", "line_map": {"16": 0, "23": 1, "24": 69, "25": 70, "26": 70, "27": 70, "28": 70, "29": 70, "30": 72, "31": 128, "32": 129, "33": 129, "34": 129, "35": 129, "36": 129, "37": 131, "38": 135, "39": 136, "40": 136, "41": 136, "42": 136, "43": 136, "44": 138, "50": 44}}
__M_END_METADATA
"""
