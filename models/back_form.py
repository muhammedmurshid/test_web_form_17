from odoo import fields, models, api

class BackendData(models.Model):
    _name = 'backend.data'

    name = fields.Char(string="Name")
    mail = fields.Char(string="Mail", widget='mail')
    phone = fields.Char(string="Phone", widget='phone')
    course = fields.Char(string="Course")

