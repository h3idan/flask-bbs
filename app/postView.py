#!/usr/bin/env python
# coding: utf-8

#**********************************
# author:   h3idan
# datetime: 2013-07-16 11:24
#**********************************


from flask import Blueprint, render_template, abort, redirect
from flask import request, session
from models import Post, User, Reply, db

postView = Blueprint('postView', __name__)


@postView.route('/')    
def postAll():
    
    posts = Post.query.all()
    return render_template('postview.html', datas=locals())


@postView.route('/publishpage')
def publishPage():
    return render_template('publish.html', datas=locals())

@postView.route('/publish', methods=['get', 'post'])
def publish():
    
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        details = request.form['details']
    
        db.session.add(Post(title, author, details))
        db.session.commit()
        return redirect('/')
    else:
        return render_template('publish.html', datas=locals())


@postView.route('/delpost/<ID>')
def delpost(ID):
    post = Post.query.get(ID)
    replys = Reply.query.filter_by(post_id=Id).all()
    db.session.delete(post)
    db.session.delete(replys)
    db.session.commit()
    return render_template('success_del.html', datas=locals())


@postView.route('/editpost/<ID>')
def editpage(ID):
    post = Post.query.get(ID)
    return render_template('editpage.html', datas=locals())

@postView.route('/edit/<ID>', methods=['get', 'post'])
def edit(ID):
    post = Post.query.get(ID)
    title = request.form['title']
    details = request.form['details']
    post.title = title
    post.details = details
    return redirect('/')

@postView.route('/post/<ID>')
def postOne(ID):
    post = Post.query.get(ID)
    replys = Reply.query.filter_by(post_id=ID).all()
    return render_template('post.html', datas=locals())





