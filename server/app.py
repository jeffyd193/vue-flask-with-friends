from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from resources.students1 import StudentList
from resources.books import BookList
from db import db
import os


# configuration
DEBUG = True


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://jme:clank123@localhost:8080/mhs'
app.config.from_object(__name__)

CORS(app)
api = Api(app)




#api.add_resource(Books, '/books')
api.add_resource(StudentList, '/students')
api.add_resource(BookList, '/booklist')

if __name__ == '__main__':
    db.init_app(app)
    app.run()
