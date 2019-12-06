# -*- coding: utf-8 -*-
from jsdb.db import result_by_query, get_search_data_sql


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


def get_sku_list(current_page, page_size, search_data=None,exact=True):
    start_num = (current_page - 1) * page_size
    end_num =start_num+page_size-1
    condition = get_search_data_sql(search_data,exact)

    sql="""
                SELECT
                    a.* 
                FROM
                    ( SELECT row_number () OVER ( ORDER BY proid ) AS row_num,* FROM product {2} ) a 
                WHERE
                    a.row_num BETWEEN {0} 
                    AND {1}  
    """

    sql=sql.format(start_num,end_num,condition)
    # print(sql)
    res=result_by_query(sql)
    return res







