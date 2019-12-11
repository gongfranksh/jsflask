import datetime
from decimal import Decimal

from redis import ConnectionPool, Redis

from jsdb.jsbranch import get_branch_all
from tools.Utils import dict_2_redis

POOL=ConnectionPool(host='127.0.0.1',port=6379,max_connections=100)

conn = Redis(connection_pool=POOL)
conn.set('name', 'LinWOW')
print(conn.get('name'))

branches=get_branch_all()

for branch in branches:
    res=dict_2_redis(branch)
    # for key,value in branch.items():
    #     if value is None:
    #         branch[key]=''
    #
    #     if isinstance(value, Decimal):
    #         branch[key] =float(value)
    #
    #     if isinstance(value, datetime.datetime):
    #             branch[key] =value.strftime('%Y-%m-%d %H:%M:%S')

    conn.hmset('branch'+branch['BraId'],res)
    # print(branch)