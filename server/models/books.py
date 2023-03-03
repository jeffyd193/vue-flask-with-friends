from db import db
import json

class Books(db.Model):

    __tablename__ = "books"

    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=False, nullable=False)
    author = db.Column(db.String(50), unique=False, nullable=False)
    genre = db.Column(db.String(10), unique=False, nullable=True)
    best_seller = db.Column(db.String(10), unique=False, nullable=True)
    checked_out = db.Column(db.Integer, nullable=True)

    def __init__(self, book_id, title, author, genre, best_seller, checked_out):
        self.book_id = book_id
        self.title= title
        self.author = author
        self.genre = genre
        self.best_seller = best_seller
        self.checked_out = checked_out

    def json(self):
        return{
            'book_id':self.book_id,
            'title': self.title, 
            'author': self.author, 
            'genre': self.genre, 
            'best_seller': self.best_seller,
            'checked_out': self.checked_out
            }

    @classmethod
    def find_by_book_id(cls, book_id):
        return cls.query.filter_by(book_id=book_id).all()

    @classmethod
    def find_all(cls):
        return cls.query.order_by(db.text('books.book_id desc')).limit(250).all()
