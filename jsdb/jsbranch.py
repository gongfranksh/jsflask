# -*- coding: utf-8 -*-
from jsdb.db import result_by_query


def get_branch_all():
    sql = " SELECT * FROM branch WHERE BraType='0' AND Status='0' ORDER BY BraName,braid "
    res=result_by_query(sql)
    return res

def get_branch_by_code(branchcode):
    sql = """
         SELECT * FROM branch WHERE BraType='0' AND Status='0'  and braid='{0}'  ORDER BY BraName,braid 
    """
    sql = sql.format(branchcode)
    rst = result_by_query(sql)
    return rst
#






