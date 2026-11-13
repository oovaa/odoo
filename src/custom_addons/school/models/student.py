from odoo import api
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
    friends_count = Integer(
        string="Friends Count",
        compute="_compute_friends",
        store=False,
    )

    @api.onchange("name")
    def on_change_name(self):
        print("name changed to:", self.name)

    @api.depends("friends_ids")
    def _compute_friends(self):
        for student in self:
            student.friends_count = len(student.friends_ids)
