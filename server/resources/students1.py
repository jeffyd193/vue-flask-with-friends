from models.students import Student
from flask_restful import Resource



class StudentList(Resource):
    def get(self):
        
        data = Student.find_all()
        return {'studentlist': [student.json() for student in Student.find_all()]}

