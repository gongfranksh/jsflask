# -*- coding: utf-8 -*-
from _md5 import md5

from jsdb.db import result_by_query, get_search_data_sql
from api.app_cache import cache


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



def get_sku_by_proid(proid):
    sql="""
               SELECT row_number () OVER ( ORDER BY proid ) AS row_num,* 
               FROM product
    """

    #判断店内码还是国际码
    if proid[0]=='2':
        condtion="""
               where proid ='{0}'
        """
    else:
        condtion="""
               where barcode ='{0}'
        """
    sql=sql+condtion
    sql=sql.format(proid)
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

@cache.cached(timeout=60 * 3)
def get_branch_sku_list(current_page, page_size, search_data=None,exact=True):
    start_num = (current_page - 1) * page_size
    end_num =start_num+page_size-1
    condition = get_search_data_sql(search_data,exact)
    sql="""
                SELECT
                    a.* 
                FROM
                    ( 
                    
                    SELECT
                        row_number () OVER ( ORDER BY proid ) AS row_num,
                        pcb.ClassName AS big_class_name,
                        pc.ClassName,
                        pd.BrandName,
                        vbp.* 
                    FROM
                        v_branch_product vbp
                        LEFT JOIN product_class pcb ON vbp.bigclass= pcb.ClassId
                        LEFT JOIN product_class pc ON vbp.classid= pc.ClassId
                        LEFT JOIN product_brand pd ON vbp.BrandId= pd.BrandId
                        {2} 
                        
                      
                    ) a 
                WHERE
                    a.row_num BETWEEN {0} 
                    AND {1}  
    """

    sql=sql.format(start_num,end_num,condition)
    # print(sql)
    res=result_by_query(sql)

    return res





