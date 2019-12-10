#!/usr/bin/python
# -*- coding: UTF-8 -*
"""
@author：li-boss
@file_name: start.py
@create date: 2019-10-27 10:20 
@blog https://leezhonglin.github.io
@csdn https://blog.csdn.net/qq_33196814
@file_description：
"""

import os

from celery import Celery
from flask_caching import Cache

from flask_cors import CORS

# from api import create_app, api
from api import api
from config import configuration, cache_config, config

from tools.exts import logger
import random
from datetime import time
from mailbox import Message

import celery
from django.core import mail
from flask import request, render_template, session, flash, redirect, url_for, jsonify, app, Flask

from utils.log_helper import init_log

app = Flask(__name__, template_folder='../templates')
# 验证
CORS(app, supports_credentials=True)
app.config.from_object(config['default'])
config['default'].init_app(app)
###初始化数据库
# db.init_app(app)
# 返回数据中response为中文
app.config['JSON_AS_ASCII'] = False

# app.config['CELERY_BROKER_URL'] = 'redis://127.0.0.1:6379/10'
# app.config['CELERY_RESULT_BACKEND'] = 'redis://127.0.0.1:6379/11'
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

# app.cache=Cache(app,config=cache_config)




# app = create_app(os.getenv('FLASK_CONFIG') or 'default')
# appcache=Cache()

if __name__ == '__main__':
    host, port, debug = configuration.get_start_config()
    app.run(host=host, port=port, debug=eval(debug))

    # global cache

    # cache=Cache(app,config=cache_config)

