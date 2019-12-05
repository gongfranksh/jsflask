# -*- coding: utf-8 -*-
from jsdb.db import result_by_query


def get_sku_all():
    sql="""
                SELECT
                    a.* 
                FROM
                    ( SELECT row_number () OVER ( ORDER BY proid ) AS row_num,* FROM product ) a 
                WHERE
                    a.row_num BETWEEN 1 
                    AND 100
    """
    res=result_by_query(sql)
    return res

#






