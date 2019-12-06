#!/usr/bin/python
# -*- coding: UTF-8 -*
"""
@author：li-boss
@file_name: __init__.py.py
@create date: 2019-10-27 13:26 
@blog https://leezhonglin.github.io
@csdn https://blog.csdn.net/qq_33196814
@file_description：
"""
from celery import Celery
from flask import Flask
from flask_cors import CORS


from api.resource import api
from utils.log_helper import init_log

from config import config, Config

import random
from datetime import time
from mailbox import Message

import celery
from django.core import mail
from flask import request, render_template, session, flash, redirect, url_for, jsonify

def create_app(config_name):
    app = Flask(__name__, template_folder='../templates')
    # 验证
    CORS(app,supports_credentials=True)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    ###初始化数据库
    # db.init_app(app)
    # 返回数据中response为中文
    app.config['JSON_AS_ASCII'] = False

    app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
    app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
    celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)

    # from api.celery.async import *

    ###初始化日志###
    # init_log(app)
    init_log()
    api.init_app(app)




    return app


