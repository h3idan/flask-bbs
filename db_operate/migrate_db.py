#!/usr/bin/env python
# coding: utf-8

#**********************************
# author:   h3idan
# datetime: 2013-07-19 17:05
#**********************************

'''
当您修改models之后，执行该文件，就会更新到数据库，而不破坏数据
'''

import imp
import sys
sys.path.append('../')
from migrate.versioning import api
from app.models import db, app


migration = app.config['SQLALCHEMY_MIGRATE_REPO'] + \
        '/versions/%03d_migration.py' % (api.db_version(app.config\
        ['SQLALCHEMY_DATABASE_URI'], app.config['SQLALCHEMY_MIGRATE_REPO']) + 1)

tmp_module = imp.new_module('old_model')
old_model = api.create_model(app.config\
        ['SQLALCHEMY_DATABASE_URI'], app.config['SQLALCHEMY_MIGRATE_REPO'])

exec old_model in tmp_module.__dict__
script = api.make_update_script_for_model(app.config\
        ['SQLALCHEMY_DATABASE_URI'], app.config['SQLALCHEMY_MIGRATE_REPO'], \
        tmp_module.meta, db.metadata)

open(migration, "wt").write(script)
a = api.upgrade(app.config['SQLALCHEMY_DATABASE_URI'], \
        app.config['SQLALCHEMY_MIGRATE_REPO'])

print 'New migration saved as ' + migration
print 'Current database version: ' + str(api.db_version(\
        app.config['SQLALCHEMY_DATABASE_URI'], \
        app.config['SQLALCHEMY_MIGRATE_REPO']))
 
