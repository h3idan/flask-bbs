#!/usr/bin/env python
# coding: utf-8

#**********************************
# author:   h3idan
# datetime: 2013-07-17 10:29
#**********************************


from flask import Blueprint, redirect, request, session
from models import Reply, User, db

replyView = Blueprint('reply', __name__)

@replyView.route('/reply/<ID>', methods=['get', 'post'])
def addReply(ID):
    author = session['username']
    details = request.form['details']
    post_id = ID

    db.session.add(Reply(author, details, post_id))
    db.session.commit()

    return redirect('/post/'+ID)


