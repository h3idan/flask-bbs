#!/usr/bin/env python
# coding: utf-8


from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

from app.loginView import userBehavior
from app.postView import postView
from app.replyView import replyView
from app.personView import personView


app = Flask(__name__)
app.config.from_object('config')


# blueprint register
app.register_blueprint(userBehavior)
app.register_blueprint(postView)
app.register_blueprint(replyView)
app.register_blueprint(personView)



if __name__ == '__main__':

    app.run(host='0.0.0.0')


