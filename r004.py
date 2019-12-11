#!/usr/bin/python
# -*- coding: UTF-8 -*
import datetime
import hashlib
import json
from _md5 import md5
from decimal import Decimal

from pip._vendor import chardet
from redis import ConnectionPool, Redis, StrictRedis

from jsdb.jsbranch import get_branch_all
from tools.Utils import dict_2_redis, dict_b_2_string, MsSqlResultDataEncoder

POOL=ConnectionPool(host='127.0.0.1',port=6379,max_connections=100)
#
# # conn = Redis(connection_pool=POOL,decode_responses=True)
conn = StrictRedis(connection_pool=POOL,decode_responses=True)
# # conn.set('name', 'LinWOW')
# # print(conn.get('name'))
#
pipe=conn.pipeline()
#
#
branches=get_branch_all()

str_json=json.dumps(branches['result'], cls=MsSqlResultDataEncoder,ensure_ascii=False)
# pipe.hmset(,res)
print(branches['sqlmd5'])
print(branches['result'])
pipe.set(branches['sqlmd5'],str_json)

# pipe.hmset(branches['sqlmd5'],str_json)
# for branch in branches:
#     res=dict_2_redis(branch)
#     # pipe.hmset('branch'+branch['BraId'],res)
pipe.execute()



# str="""
# select * from branch
# """
#
# str_md5=hashlib.md5(str.encode("utf8"))
# print(str_md5.hexdigest())