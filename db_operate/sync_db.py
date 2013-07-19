#!/usr/bin/env python
# coding: utf-8

#**********************************
# author:   h3idan
# datetime: 2013-07-19 16:34
#**********************************

'''
创建好一个数据库之后，执行该文件，
同步所有的数据表
'''

import os.path
import sys
sys.path.append('../')
from migrate.versioning import api
from app.models import app, db

db.create_all()
if not os.path.exists(app.config['SQLALCHEMY_MIGRATE_REPO']):
    api.create(app.config['SQLALCHEMY_MIGRATE_REPO'], 'database repository')
    api.version_control(app.config['SQLALCHEMY_DATABASE_URI'], \
            app.config['SQLALCHEMY_MIGRATE_REPO'])
else:
    api.version_control(app.config['SQLALCHEMY_DATABASE_URI'], app.config\
            ['SQLALCHEMY_MIGRATE_REPO'], api.version(app.config['SQLALCHEMY_MIGRATE_REPO']))
