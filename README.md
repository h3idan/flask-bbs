flask-bbs
============



版本：
    flask == 0.10
    sqlalchemy = 0.8
    flask_sqlalchemy = 0.16
    sqlalchemy-migrate = 0.7.2

    使用easy_install安装即可


使用：
    
    一、创建表
        1) 在数据库中创建数据库（默认是MySQL） 
        2) 在models中修改数据库模式、用户名、密码、数据库地址、数据库名称
        3) create database flaskbbs default character set utf8;
        4) cd db_operate  
        5) python sync_db.py
        6) python runserver.py


Ps：纯属为了学习flask所写
