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
                    AND 50
    """
    res=result_by_query(sql)
    return res


def get_sku_list(current_page, page_size, search_data=None):
    sql="""
                SELECT
                    a.* 
                FROM
                    ( SELECT row_number () OVER ( ORDER BY proid ) AS row_num,* FROM product ) a 
                WHERE
                    a.row_num BETWEEN {0} 
                    AND {1}
    """
    start_num = (current_page - 1) * page_size
    end_num =start_num+page_size

    sql=sql.format(start_num,end_num)
    res=result_by_query(sql)
    return res
#






