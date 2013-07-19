#!/usr/bin/env python
# coding: utf-8

#**********************************
# author:   h3idan
# datetime: 2013-07-16 14:24
#**********************************


from flask import Flask, Blueprint, url_for, g 
from flask import request, session, render_template, redirect
from models import User, Post, Reply, db


userBehavior = Blueprint('userBehavior', __name__) 

@userBehavior.route('/registerpage')
def register_page():
    return render_template('register.html', data=locals())

@userBehavior.route('/register', methods=['get', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        
        db.session.add(User(username, password, email))
        db.session.commit()
        return render_template('success_reg.html', data=locals())
    else:
        return render_template('fail_reg.html', data=locals())



@userBehavior.route('/login', methods=['get', 'POST'])
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and user.username == username and user.password == password:
            session['username'] = username
            return redirect('/')

        else:
            return render_template('fail_login.html', data=locals())

    return render_template('login.html', data=locals())


@userBehavior.route('/logout')
def logout():
    session.clear()
    return render_template('logout.html', data=locals())












            
