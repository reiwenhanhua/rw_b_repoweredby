# -*- coding: utf-8 -*-
from odoo import http

# class RwhhRewritePoweredby(http.Controller):
#     @http.route('/rwhh_rewrite_poweredby/rwhh_rewrite_poweredby/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rwhh_rewrite_poweredby/rwhh_rewrite_poweredby/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rwhh_rewrite_poweredby.listing', {
#             'root': '/rwhh_rewrite_poweredby/rwhh_rewrite_poweredby',
#             'objects': http.request.env['rwhh_rewrite_poweredby.rwhh_rewrite_poweredby'].search([]),
#         })

#     @http.route('/rwhh_rewrite_poweredby/rwhh_rewrite_poweredby/objects/<model("rwhh_rewrite_poweredby.rwhh_rewrite_poweredby"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rwhh_rewrite_poweredby.object', {
#             'object': obj
#         })