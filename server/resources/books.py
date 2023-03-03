from models.books import Books
from flask_restful import Resource



class BookList(Resource):
    def get(self):
        
        data = Books.find_all()
        return {'BookList': [books.json() for books in Books.find_all()]}

