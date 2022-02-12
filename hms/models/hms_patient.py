from odoo import models, fields, api
from datetime import date
import re

from odoo.exceptions import UserError


class Patient(models.Model):
    _name = 'hms.patient'
    _description = "Patient Model"
    _rec_name = "firstname"

    firstname = fields.Char()
    lastname = fields.Char()
    birthdate = fields.Date()
    history = fields.Html()
    cr = fields.Float()
    bloodtype = fields.Selection(
        [('+a', '+A'), ('+b', '+B'), ('+o', '+O'), ('+ab', '+AB'), ('-a', '-A'), ('-b', '-B'), ('-o', '-O'),
         ('-ab', '-AB')])
    pcr = fields.Boolean()
    image = fields.Image()
    address = fields.Text()
    # age=fields.Integer()
    age = fields.Integer(compute='_calc_birthdate_age')
    department_id = fields.Many2one('hms.department')
    doctor = fields.Many2many('hms.doctor')
    state = fields.Selection(
        [('undetermined', 'Undetermined'), ('good', 'Good'), ('fair', 'Fair'), ('serious', 'Serious')])
    capacity = fields.Integer(related='department_id.capacity')
    email = fields.Text()
    customer_id = fields.Many2one('res.partner')
    log = fields.One2many('hms.patientlog', 'patient_id')

    _sql_constraints = {
        ('emai_constraint', 'UNIQUE(email)', 'Email already exists.'),
    }

    def _calc_birthdate_age(self):
        for rec in self:
            rec.age = date.today().year - rec.birthdate.year

    @api.onchange('birthdate')
    def _onchange_birthdate(self):
        if self.birthdate:
            age = date.today().year - self.birthdate.year
            if age < 30:
                self.pcr = True
                return {
                    'warning': {
                        'title': 'Alert',
                        'message': ' PCR have been checked!'
                    }
                }

    @api.onchange('state')
    def _onchange_state(self):
        if self.state:
            self.env['hms.patientlog'].create({
                'description': self.state,
                'createdby':self.write_uid,
                'createdDate': date.today(),
                'patient_id':self.id
                                              })

    @api.onchange('email')
    def validate_email(self):
        if self.email:
            email_valid = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
            if email_valid is None:
                return {
                    'warning': {
                        'title': 'Alert',
                        'message': ' Invalid email, please try again'
                    }}



    @api.onchange('customer_id')
    def _onchange_customer(self):
        if self.customer_id:
            if self.customer_id.email == self.email:
                raise UserError('Customer cannot be linked with a patient with same email')

