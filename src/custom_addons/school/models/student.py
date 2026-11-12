from odoo.fields import Boolean, Char, Integer, Many2many, Selection
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
    friends_ids = Many2many(
        "school.student",
        "student_friend_relation",
        "student_id",
        "friend_id",
        string="Friends",
    )
