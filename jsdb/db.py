# -*- coding: utf-8 -*-
#coding=utf8
import sys
import time
import pymssql
import threading

from DBUtils.PooledDB import PooledDB, SharedDBConnection

from common.common_response_code import response_code
from tools.config import js_host, js_user, js_pwd, js_db
from utils.log_helper import lg
from api.app_cache import cache, cache_key

POOL = PooledDB(
    creator=pymssql,  # 使用链接数据库的模块
    maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
    mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
    maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
    maxshared=3,  # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
    blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
    maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
    setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
    ping=0,
    host=js_host,
    port=1433,
    user=js_user,
    password=js_pwd,
    database=js_db,
    # charset='utf8'
    # mssql设置utf8为出现乱码

    charset='GBK'
)


# def result_by_query(sql):
#         conn=POOL.connection()
#         cursor=conn.cursor(as_dict=True)
#         cursor.execute(sql)
#         res=cursor.fetchall()
#         conn.close()
#         return res

# @cache.cached(timeout=50)
# @cache.memoize(timeout=60)
def result_by_query(sql):
    try:
        conn=POOL.connection()
        cursor=conn.cursor(as_dict=True)
        cursor.execute(sql)
        res=cursor.fetchall()
        conn.close()
        return res
    except Exception as e:
        lg.error(e)
        return response_code.GET_DATA_FAIL


def get_search_data_sql(search_data=None,exact=True):
    try:
        condition_str = ''
        if search_data is None:
            return  ''
        else:
            search_condition = search_data
            i = 0
            if search_condition:
                for key in search_condition.keys():

                    if exact:

                        if i==0:
                            condition = """
                                    {0} = '{1}'
                              """
                        else:
                            condition = """
                                   and {0} = '{1}'
                                  """
                    else:
                        if i==0:
                            condition = """
                                    {0} like '%{1}%'
                              """
                        else:
                            condition = """
                                   and {0} like '%{1}%'
                                  """

                    condition = condition.format(key, search_condition[key])
                    condition_str = condition_str + condition
                    i=i+1
            return ' where ' + condition_str
    except Exception as e:
        lg.error(e)
        return response_code.GET_DATA_FAIL




# def str_cr_lf(sql):
#     return sql.replace("\n","").replace("\r","")

# pp=result_by_query("select CONVERT(nvarchar(20),braname) braname from branch")
# print("中文")
# print(pp)