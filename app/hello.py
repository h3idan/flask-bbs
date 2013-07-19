#!/usr/bin/env python
# coding: utf-8

#**********************************
# author:   h3idan
# datetime: 2013-07-15 15:59
#**********************************


from flask import Blueprint, render_template, abort

hello = Blueprint('hello', __name__)

@hello.route('/hello')
def hello_world():
    hello = {
            'hello': 'hello world'
            
            }
    return render_template('hello.html', hello=hello)
