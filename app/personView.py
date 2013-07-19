#!/usr/bin/env python
# coding: utf-8

#**********************************
# author:   h3idan
# datetime: 2013-07-17 11:31
#**********************************


import os
from flask import Blueprint, session, request, \
        url_for, render_template, redirect, \
        send_from_directory
from werkzeug import secure_filename
from models import User, Post, db

personView = Blueprint('personView', __name__)

upload_folder = os.path.join(os.path.dirname(__file__), \
        '../uploads').replace('\\', '/')

@personView.route('/person/<name>')
def personCenter(name):
    user = User.query.filter_by(username=name).first()
    posts = Post.query.filter_by(author=name).all()
    
    return render_template('personcenter.html', datas=locals())

@personView.route('/editpic/<name>', methods=['get', 'post'])
def editPic(name):
    if request.method == 'POST':
        pic = request.files['pic']
        if pic:
            filename = pic.filename
            path = os.path.join(upload_folder, filename)
            pic.save(path)
            pic_url = url_for('personView.uploaded_file', filename=filename)
            user = User.query.filter_by(username=name).first()
            user.pic = pic_url
            db.session.commit()

    return redirect('/person/'+name)

@personView.route('/images/<filename>')
def uploaded_file(filename):
    return send_from_directory(upload_folder, filename)

