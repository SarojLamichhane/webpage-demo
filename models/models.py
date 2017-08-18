from odoo import models, fields, api

class query(models.Model):
    _name='query.query'

    name=fields.Char(required="True",string="Name")
    contact=fields.Char(required="True",string="Contact")
    addresss=fields.Char(string="Address")
    occupation=fields.Char(string="Ocupation")
    nature_of_query=fields.Selection([('storage','Storage'),('crops','Crops'),('market','Market'),('price','Price'),('support','Support')])
    query=fields.Text(required="True",string='Query')
