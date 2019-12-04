# #!/usr/bin/python
# # -*- coding: UTF-8 -*
# """
# @author：li-boss
# @file_name: log_helper.py
# @create date: 2019-10-27 14:19
# @blog https://leezhonglin.github.io
# @csdn https://blog.csdn.net/qq_33196814
# @file_description：调试代码日志打印
# """
#
import logging
import os
from logging.handlers import RotatingFileHandler

# 日志文件最大 100MB
from flask.logging import default_handler

LOG_FILE_MAX_BYTES = 100 * 1024 * 1024
# 轮转数量是 10 个
LOG_FILE_BACKUP_COUNT = 10

# 1.创建1个logger：
# lg = logging.getLogger("Error")
lg = logging.getLogger()
lg.setLevel(logging.INFO)

# lginfo = logging.getLogger()
# lginfo.setLevel(logging.INFO)
# lginfo = logging.getLogger("Info")


# def init_log(app):
def init_log():
    # log_path = os.getcwd() + "/var/log"
    # app.logger.removeHandler(default_handler)
    log_path = os.getcwd()
    try:
        if not os.path.exists(log_path):
            os.makedirs(log_path)
    except:
        print("创建日志目录失败")
        exit(1)
    if len(lg.handlers) == 0:  # 避免重复
        # 2.创建handler(负责输出，输出到屏幕streamhandler,输出到文件filehandler)
        filename = os.path.join(log_path, 'user_api.log')
        # fh = logging.FileHandler(filename, mode="a", encoding="utf-8")  # 默认mode 为a模式，默认编码方式为utf-8
        print(filename)
        fh = RotatingFileHandler(
            filename=filename,
            mode='a',
            maxBytes=LOG_FILE_MAX_BYTES,
            backupCount=LOG_FILE_BACKUP_COUNT,
            encoding='utf-8'
        )

        sh = logging.StreamHandler()
        # 3.创建formatter：
        formatter = logging.Formatter(
            fmt='%(asctime)s - %(levelname)s - Model:%(filename)s - Fun:%(funcName)s - Message:%(message)s - Line:%(lineno)d')

        # # ②为handler绑定formatter
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)

        # # 5.设置日志级别(日志级别两层关卡必须都通过，日志才能正常记录)
        # lg.setLevel(40)
        # fh.setLevel(40)
        # # sh.setLevel(40)
        fh.setLevel(logging.INFO)
        # lg.setLevel(logging.INFO)
        sh.setLevel(logging.INFO)


        # lg.addHandler(fh)
        # lg.addHandler(sh)


        #4.绑定关系：①logger绑定handler

        # for logger in (
        #         # 这里自己还可以添加更多的日志模块，具体请参阅Flask官方文档
        #         app.logger,
        #         logging.getLogger('sqlalchemy'),
        #         logging.getLogger('werkzeug'),
        #         logging.getLogger("Error")
        #         # logging.getLogger("INFO")
        #         # logging.getLogger("INFO")
        #
        # ):
            # lginfo.addHandler(fh)
        lg.addHandler(fh)
        lg.addHandler(sh)
        # logger.addHandler(fh)
        # logger.addHandler(sh)

