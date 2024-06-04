# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1715684985.660713
_enable_loop = True
_template_filename = 'static/templates/about.html'
_template_uri = 'about.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n\r\n<head>\r\n  <!-- Basic -->\r\n  <meta charset="utf-8" />\r\n  <meta http-equiv="X-UA-Compatible" content="IE=edge" />\r\n  <!-- Mobile Metas -->\r\n  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />\r\n  <!-- Site Metas -->\r\n  <meta name="keywords" content="" />\r\n  <meta name="description" content="" />\r\n  <meta name="author" content="" />\r\n\r\n  <title>TouchRugby</title>\r\n\r\n\r\n  <!-- bootstrap core css -->\r\n  <link rel="stylesheet" type="text/css" href="./static/css/bootstrap.css" />\r\n\r\n  <!-- fonts style -->\r\n  <link href="https://fonts.googleapis.com/css?family=Poppins:400,600,700&display=swap" rel="stylesheet">\r\n\r\n  <!-- font awesome style -->\r\n  <link href="./static/css/font-awesome.min.css" rel="stylesheet" />\r\n  <!-- nice select -->\r\n  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/jquery-nice-select/1.1.0/css/nice-select.min.css" integrity="sha256-mLBIhmBvigTFWPSCtvdu6a76T+3Xyt+K571hupeFLg4=" crossorigin="anonymous" />\r\n\r\n  <!-- Custom styles for this template -->\r\n  <link href="./static/css/style.css" rel="stylesheet" />\r\n  <!-- responsive style -->\r\n  <link href="./static/css/responsive.css" rel="stylesheet" />\r\n\r\n</head>\r\n\r\n<body class="sub_page">\r\n\r\n  <div class="hero_area">\r\n    <!-- header section strats -->\r\n    <header class="header_section">\r\n      <div class="container-fluid">\r\n        <nav class="navbar navbar-expand-lg custom_nav-container ">\r\n          <a class="navbar-brand" href="index">\r\n            <span>\r\n              TouchRugby\r\n            </span>\r\n          </a>\r\n          </a>\r\n\r\n          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">\r\n            <span class=""> </span>\r\n          </button>\r\n\r\n          <div class="collapse navbar-collapse" id="navbarSupportedContent">\r\n            <ul class="navbar-nav  ml-auto">\r\n              <li class="nav-item active">\r\n                <a class="nav-link" href="index">Home</a>\r\n              </li>\r\n              <li class="nav-item">\r\n                <a class="nav-link" href="equipe"> Equipes</a>\r\n              </li>\r\n              <li class="nav-item">\r\n                <a class="nav-link" href="joueur">Joueurs</a>\r\n              </li>\r\n              <li class="nav-item">\r\n                <a class="nav-link" href="matchs">Matchs</a>\r\n              </li>\r\n              <li class="nav-item">\r\n                <a class="nav-link" href="#">\r\n                  <i class="fa fa-user" aria-hidden="true"></i>\r\n                  <span>\r\n                    Login\r\n                  </span>\r\n                </a>\r\n              </li>\r\n              <li class="nav-item">\r\n                <a class="nav-link" href="#">\r\n                  <i class="fa fa-user" aria-hidden="true"></i>\r\n                  <span>\r\n                    Sign Up\r\n                  </span>\r\n                </a>\r\n              </li>\r\n              <form class="form-inline">\r\n                <button class="btn   nav_search-btn" type="submit">\r\n                  <i class="fa fa-search" aria-hidden="true"></i>\r\n                </button>\r\n              </form>\r\n            </ul>\r\n          </div>\r\n        </nav>\r\n      </div>\r\n    </header>\r\n    <!-- end header section -->\r\n  </div>\r\n\r\n  <!-- about section -->\r\n\r\n  <section class="about_section layout_padding">\r\n    <div class="container">\r\n      <div class="row">\r\n        <div class="col-md-6">\r\n          <div class="detail-box">\r\n            <div class="heading_container">\r\n              <h2>\r\n                About Us\r\n              </h2>\r\n            </div>\r\n            <p>\r\n              Normal distribution of letters, as opposed to using \'Content here, content here\', making it look like\r\n              readable English. Many desktop publishing packages and web page editors has a more-or-less normal\r\n              distribution of letters, as opposed to using \'Content here, content here\', making it look like readable\r\n              English. Many desktop publishing packages and web page editors\r\n            </p>\r\n            <a href="">\r\n              Read More\r\n            </a>\r\n          </div>\r\n        </div>\r\n        <div class="col-md-6">\r\n          <div class="img-box">\r\n            <img src="images/about-img.jpg" alt="">\r\n          </div>\r\n        </div>\r\n      </div>\r\n    </div>\r\n  </section>\r\n\r\n  <!-- end about section -->\r\n\r\n  <!-- info section -->\r\n  <section class="info_section ">\r\n    <div class="container">\r\n      <div class="row">\r\n        <div class="col-md-2 info_links">\r\n          <h4>\r\n            Menu\r\n          </h4>\r\n          <ul>\r\n            <li>\r\n              <a href="index">\r\n                Home\r\n              </a>\r\n            </li>\r\n            <li class="active">\r\n              <a href="equipe">\r\n                About\r\n              </a>\r\n            </li>\r\n            <li>\r\n              <a href="joueur">\r\n                Jobs\r\n              </a>\r\n            </li>\r\n            <li>\r\n              <a href="matchs">\r\n                Freelancers\r\n              </a>\r\n            </li>\r\n          </ul>\r\n        </div>\r\n        <div class="col-md-3">\r\n          <h4>\r\n            Jobs\r\n          </h4>\r\n          <p>\r\n            Established fact that a reader will be distracted by the readable content of a page when looking at its\r\n            layout. The point of using Lorem Ipsum\r\n          </p>\r\n        </div>\r\n        <div class="col-md-3">\r\n          <div class="info_social">\r\n            <h4>\r\n              Social Link\r\n            </h4>\r\n            <div class="social_container">\r\n              <div>\r\n                <a href="">\r\n                  <i class="fa fa-facebook" aria-hidden="true"></i>\r\n                </a>\r\n              </div>\r\n              <div>\r\n                <a href="">\r\n                  <i class="fa fa-twitter" aria-hidden="true"></i>\r\n                </a>\r\n              </div>\r\n              <div>\r\n                <a href="">\r\n                  <i class="fa fa-linkedin" aria-hidden="true"></i>\r\n                </a>\r\n              </div>\r\n              <div>\r\n                <a href="">\r\n                  <i class="fa fa-instagram" aria-hidden="true"></i>\r\n                </a>\r\n              </div>\r\n            </div>\r\n          </div>\r\n        </div>\r\n        <div class="col-md-4">\r\n          <div class="info_form">\r\n            <h4>\r\n              Newsletter\r\n            </h4>\r\n            <form action="">\r\n              <input type="text" placeholder="Enter Your Email" />\r\n              <button type="submit">\r\n                Subscribe\r\n              </button>\r\n            </form>\r\n          </div>\r\n        </div>\r\n      </div>\r\n    </div>\r\n  </section>\r\n  <!-- end info_section -->\r\n\r\n\r\n  <!-- footer section -->\r\n  <footer class="footer_section">\r\n    <div class="container">\r\n      <p>\r\n        &copy; <span id="displayYear"></span> All Rights Reserved By\r\n        <a href="https://html.design/">Free Html Templates</a>\r\n      </p>\r\n    </div>\r\n  </footer>\r\n  <!-- footer section -->\r\n\r\n  <!-- jQery -->\r\n  <script src="js/jquery-3.4.1.min.js"></script>\r\n  <!-- bootstrap js -->\r\n  <script src="js/bootstrap.js"></script>\r\n  <!-- nice select -->\r\n  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-nice-select/1.1.0/js/jquery.nice-select.min.js" integrity="sha256-Zr3vByTlMGQhvMfgkQ5BtWRSKBGa2QlspKYJnkjZTmo=" crossorigin="anonymous"></script>\r\n  <!-- custom js -->\r\n  <script src="js/custom.js"></script>\r\n\r\n</body>\r\n\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "static/templates/about.html", "uri": "about.html", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 1, "27": 21}}
__M_END_METADATA
"""