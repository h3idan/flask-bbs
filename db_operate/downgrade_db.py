#!/usr/bin/env python
# coding: utf-8

#**********************************
# author:   h3idan
# datetime: 2013-07-19 17:12
#**********************************

'''
回滚数据库，每次向前回滚一个版本
'''

import sys
sys.path.append('../')
from migrate.versioning import api
from app.models import app


v = api.db_version(app.config['SQLALCHEMY_DATABASE_URI'],\
        app.config['SQLALCHEMY_MIGRATE_REPO'])

if v == 1:
    print 'Current database version %d , only version 2 can downgrade' % v
else:
    api.downgrade(app.config['SQLALCHEMY_DATABASE_URI'], \
            app.config.get('SQLALCHEMY_MIGRATE_REPO'), v - 1)
    print 'Current database version: ' + str(api.db_version(app.config\
            ['SQLALCHEMY_DATABASE_URI'], app.config['SQLALCHEMY_MIGRATE_REPO']))
 
