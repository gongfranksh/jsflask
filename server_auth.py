# -*- coding: utf-8 -*-

from flask import Flask, request
from flask_restful import Api,Resource

from control.branch_ctrl import Branchlist

app = Flask(__name__)
api=Api(app)

api.add_resource(Branchlist,'/branch/')

@app.before_request
def before_request():
    ip = request.remote_addr
    url = request.url
    form = request.form # 请求的数据，可执行searchword = request.form.get('key', '')  ?????????测试（带参数的post请求）过程中form为空，不清楚原因
    args = request.args # ?key=value，可执行searchword = request.args.get('key', '')
    values = request.values # form和args的元组
    headers = request.headers
    method = request.method
    path = request.path
    base_url = request.base_url
    url_root = request.url_root
    print ("ip", ip)
    print ("url", url)


if __name__ == '__main__':
    app.debug = True
    app.config['JSON_AS_ASCII'] = False
    app.run(host='192.168.81.148',debug=True)