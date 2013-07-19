#!/usr/bin/env python
# coding: utf-8

#**********************************
# author:   h3idan
# datetime: 2013-07-16 09:54
#**********************************


import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:heidan@localhost/flaskbbs'
app.config['SQLALCHEMY_MIGRATE_REPO'] = os.path.join(os.path.dirname(__file__), 'db_repository')
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(100), unique=True)
    pic = db.Column(db.String(100), unique=True, nullable=True)
    password = db.Column(db.String(30))
    status = db.Column(db.Integer, default=0)
    posts = db.relationship('Post', backref='user', lazy='dynamic')
    replys = db.relationship('Reply', backref='user', lazy='dynamic')

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=True, default='')
    details = db.Column(db.Text, nullable=True, default='')
    author = db.Column(db.String(30), db.ForeignKey('user.username'))
 #   replys = db.relationship('Reply', backref='post', lazy='danamic')

    def __init__(self, title, author, details):
        self.title = title
        self.author = author
        self.details = details

    def __repr__(self):
        return '<Post %r>' % self.title


class Reply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    details = db.Column(db.String(1000), nullable=True, default='')
    author = db.Column(db.String(30), db.ForeignKey('user.username'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))


    def __init__(self, author, details, post_id):
        self.author = author
        self.details = details
        self.post_id = post_id

    def __repr__(self):
        return '<Reply %r>' % self.details[:10]



if __name__ == '__main__':

    print u'正在常见数据库表...'
    db.create_all()
    print u'数据库表已经创建完成,请查看数据库.'




