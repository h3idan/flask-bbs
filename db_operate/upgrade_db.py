#!/usr/bin/env python
# coding: utf-8

#**********************************
# author:   h3idan
# datetime: 2013-07-19 17:09
#**********************************

'''
数据库回滚之后，执行该文件。
更新回最新版本的数据库
'''

import sys
sys.path.append('../')
from migrate.versioning import api
from app.models import app

api.upgrade(app.config['SQLALCHEMY_DATABASE_URI'], \
        app.config['SQLALCHEMY_MIGRATE_REPO'])
print 'Current database version: ' + str(api.db_version(\
        app.config['SQLALCHEMY_DATABASE_URI'], app.config['SQLALCHEMY_MIGRATE_REPO']))
