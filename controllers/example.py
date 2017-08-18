# -*- coding: utf-8 -*-
from django.db.models import query
from odoo import http


from odoo.http import request
import json


class Example(http.Controller):
    @http.route('/example', type='http', auth='public', website=True)
    def render_example_page(self):
        return http.request.render('create_webpage_demo.example_page', {})

    @http.route('/example/detail', type='http', auth='public', website=True)
    def navigate_to_detail_page(self):
        # This will get all query details (in case of multicompany this are multiple records)
        companies = http.request.env['query.query'].sudo().search([])
        return http.request.render('create_webpage_demo.detail_page', {
          # pass company details to the webpage in a variable
          'companies': companies})

    @http.route('/example/add', auth='public', website=True)
    def render_add_page(self):
        return http.request.render('create_webpage_demo.add_query',{})

    @http.route(['/example/detailquery'], type='http', auth='public', website=True)
    def detailquery(self,redicrect=None, **post):
        self.query_process(post)

        # form =self.env['query'].sudo.search();
        # form = self.env['query']
        # values = {
        #     'form' : form
        # }
        # if post:
        #     self.query_process(post)
        #     # return request.redirect('/example')
        # # self.query_process()
        # return request.render("query",values)

    def query_process(self, post):

        # Put your backend operations here, e.g.
        query_post = query.create({
            'name' : post.get('name'),
            'contact': post.get('contact'),
            'query': post.get('query'),
        })




    # After you're done, use either request.render() or request.redirect() to show
    # a different page to the user. You can check out the website_portal module for examples.



    # @http.route('/example/detail/<string:model_name>', type='http',methods=['POST'], auth='public', website=True)
    # def add_query(self, model_name,  **kwargs):
    #     query_model=request.env['ir.model'].search([('model', '=',model_name ),('website_form_access','=',True)])
    #

        # query_model.create({
        #
        # })
        # return http.request.render('create_webpage_demo.add_query', {
        # })


    # @http.route('/page/add_query/', auth='public', methods=['POST'], website=True)
    # def index(self, **post):
    #         query_model = request.env['query']
    #         # return http.request.render('create_webpage_demo.add_query', {
    #         })

        # @http.route('/example/detail/_form', type='http', auth='public', website=True)
        # def render_example_page(self):
        #     return "<h1>heelo</h1>"
    # @http.route('/example/detail', type='http', auth='public', website=True)
    # def create(self, **post_data):
    #     form = Example(request.httprequest.form)
    #     if request.httprequest.method == 'POST' and form.validate():
    #         request.env['res.partner'].create({
    #             'name': form.name.data,
    #             'email': form.email.data
    #         })
