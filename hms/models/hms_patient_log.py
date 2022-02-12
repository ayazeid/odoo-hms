from odoo import models, fields


class PatientLog(models.Model):
    _name = 'hms.patientlog'
    _rec_name = "description"

    createdby=fields.Char()
    createdDate=fields.Date()
    description = fields.Text()
    # createdby = fields.Many2one('hms.doctor')
    patient_id = fields.Many2one('hms.patient')

    # def create(self, vals_list):
    #     if 'description' in vals_list:
    #         self.createdDate = self.create_date
    #         self.createdby = self.create_uid
    #         super(PatientLog, self).create(vals_list)




