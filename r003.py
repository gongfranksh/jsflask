#!/usr/bin/python
# -*- coding: UTF-8 -*
import datetime
import json
from decimal import Decimal

from pip._vendor import chardet
from redis import ConnectionPool, Redis, StrictRedis

from jsdb.jsbranch import get_branch_all
from tools.Utils import dict_2_redis, dict_b_2_string

POOL=ConnectionPool(host='127.0.0.1',port=6379,max_connections=100)

# conn = Redis(connection_pool=POOL,decode_responses=True)
conn = StrictRedis(connection_pool=POOL,decode_responses=True)
# conn.set('name', 'LinWOW')
# print(conn.get('name'))

pipe=conn.pipeline()

#
# branches=get_branch_all()
#
# for branch in branches:
#     res=dict_2_redis(branch)
#     pipe.hmset('branch'+branch['BraId'],res)
#
# pipe.execute()


# print(branch)

# pipe.hgetall('branch01001','BraName')
# pipe.hget('branch01001','OpenDate')
# pipe.hget('branch01001','BraName')
pipe.hgetall('branch01001')
ii=pipe.execute()
#
pp=ii[0]

rest=dict_b_2_string(pp)

json_l=json.dumps(rest)
json_t=json.loads(json_l)
print(json_t)
# pp=json.loads(ii[0])
# pp=json.dumps(ii[0])

# print(pp )
# print(pp[b'BraSName'] )
# i9=str(pp[b'BraSName'], encoding="utf-8")
#
# rt={}
#
# str_dict={}
# for key,value in pp.items():
#     itemkey=str(key, encoding="utf-8")
#     itemvalue=str(value, encoding="utf-8")
#     rt[itemkey]=itemvalue
#
    # rt.update(itemkey=itemvalue)

    # print(itemkey)
    # print(itemvalue)
    # str_temp= " '%s': %s" % (itemkey,itemvalue)

    # print(str_temp)






# print(rt)
# print('\n')
# print(ii[0]['BraSName'])
# print(chardet.detect(ii))