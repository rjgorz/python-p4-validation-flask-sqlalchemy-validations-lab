from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError('Failed name validation. Name must have a value.')
        elif name in db.session.query(Author.name).all():
            raise ValueError('Failed name validation. Name must be unique.')
        return name

    @validates('phone_number')
    def validate_phone(self, key, number):
        if len(number) != 10:
            raise ValueError('Failed phone number validation. Phone number muse be exactly 10 digits.')
        return number
    
class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    summary = db.Column(db.String)
    category = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('title')
    def validate_title(self, key, title):
        if ("Won't Believe" or "Secret" or "Top" or "Guess") not in title:
            raise ValueError('Failed title validation. Title must be click-baity.')
        return title

    @validates('content')
    def validate_content(self, key, content):
        if len(content) < 250:
            raise ValueError('Failed content validation. Content must be at least 250 characters!')
        return content
    
    @validates('summary')
    def validate_content(self, key, summary):
        if len(summary) > 250:
            raise ValueError('Failed content validation. Content must be at least 250 characters!')
        return summary
    
    @validates('category')
    def validate_category(self, key, category):
        if (category != 'Fiction') or (category != 'Non-Fiction'):
            raise ValueError('Failed category validation. Category must be Fiction or Non-Fiction.')
        return category