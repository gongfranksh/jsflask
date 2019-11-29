# encoding: utf-8
from flask import Flask
# from config import CONFIG
from flask_restful import Api

from control.branch_ctrl import Branchlist,  BranchItem
from tools.exts import logger


def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(Branchlist, '/branch/')
    api.add_resource(BranchItem, '/branch/<branch_code>')

    # 加载配置
    # app.config.from_object(CONFIG)

		# 初始化logger
    logger.init_app(app)

    return app
