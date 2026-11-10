from odoo import fields, models


class Patient(models.Model):
    _name = "patient.patient"
    _description = "Patient"

    name = fields.Char(string="Name", required=True)
    test = fields.Boolean(string="is cool")
    age = fields.Integer(string="Age")
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female"), ("other", "Other")],
        string="Gender",
    )
