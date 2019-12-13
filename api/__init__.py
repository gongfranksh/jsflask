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
from flask_caching import Cache
from flask_cors import CORS

from api.app_celery import jsflaskcelery
from api.resource import api

from api.app_cache import cache
from utils.log_helper import init_log

from config import config, Config, cache_config


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

    app.config['CELERY_BROKER_URL'] = 'redis://127.0.0.1:6379/10'
    app.config['CELERY_RESULT_BACKEND'] = 'redis://127.0.0.1:6379/11'

    # jsflaskcelery=Celery(app.name, broker=app.config['CELERY_BROKER_URL'],backend=app.config['CELERY_RESULT_BACKEND'])
    # app=Celery(app.name, broker=app.config['CELERY_BROKER_URL'],backend=app.config['CELERY_RESULT_BACKEND'])

    # celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
    # celery.conf.update(app.config)

    # print("kkkk",app.name)
    # from api.celery.async import *
    # appcache = Cache(app, config=cache_config)
    ###初始化日志###
    # init_log(app)

    # cache=Cache(app,config=cache_config)
    init_log()
    api.init_app(app)
    cache.init_app(app,config=cache_config)
    return app





