#!/usr/bin/env python
# coding: utf-8

#**********************************
# author:   h3idan
# datetime: 2013-07-19 16:26
#**********************************


'''
配置文件：
    debug，secret_key, upload_folder等

'''


import os


basedir = os.path.dirname(__file__)
DEBUG= True
SECRET_KEY = 'flaskbbs'
UPLOAD_FOLDER = os.path.join(basedir, './uploads').replace('\\', '/')

