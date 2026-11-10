from odoo.fields import Boolean, Char, Integer, Selection
from odoo.models import Model


class Student(Model):
    _name = "school.student"
    _description = "a student from a school"

    name = Char(string="name")
    age = Integer(string="age")
    year = Integer(string="year")
    suspended = Boolean(string="suspended")
    gender = Selection(
        [("male", "Male"), ("femail", "Femail"), ("superMail", "Super Mail")],
        string="Gender",
    )
