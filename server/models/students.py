from db import db
import json

class Student(db.Model):

    __tablename__ = "students"

    student_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), unique=False, nullable=False)
    last_name = db.Column(db.String(50), unique=False, nullable=False)
    year = db.Column(db.String(10), unique=False, nullable=True)
    books_checked = db.Column(db.Integer, nullable=True)

    def __init__(self, student_id, first_name, last_name, year, books_checked):
        self.student_id = student_id
        self.first_name= first_name
        self.last_name = last_name
        self.year = year
        self.books_checked = books_checked

    def json(self):
        return{
            'student_id':self.student_id,
            'first_name': self.first_name, 
            'last_name': self.last_name, 
            'year': self.year, 
            'books_checkeded': self.books_checked
            }

    @classmethod
    def find_by_student_id(cls, studentid):
        return cls.query.filter_by(student_id=studentid).all()

    @classmethod
    def find_all(cls):
        return cls.query.order_by(db.text('students.student_id desc')).limit(250).all()
