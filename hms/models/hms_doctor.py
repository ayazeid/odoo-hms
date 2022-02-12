from odoo import models, fields


class Doctor(models.Model):
    _name = "hms.doctor"
    _description = "Hospital Doctors"
    _rec_name = "firstname"

    firstname = fields.Char()
    lastname = fields.Char()
    image = fields.Image()

