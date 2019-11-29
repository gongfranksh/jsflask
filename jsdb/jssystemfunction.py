# -*- coding: utf-8 -*-
from jsdb.db import result_by_query

def query_branch_section_menu():
    sql = """
    SELECT cast (id as int) AS centid, cast(id_child as int) AS sectionid ,menutext AS sectionname  
    FROM system_function_mobile  
    WHERE id_child_child=0 and isnull(Flag,'0')='1'
     ORDER BY id,id_child
     """
    rst = result_by_query(sql)
    return rst

def query_branch_function_menu(centid,sectionid):
        sql = """
            SELECT CAST (id*1000+id_child*100+id_child_child AS INT) AS functionid
            ,menutext AS functionname  
            ,isnull(iconname,'') as iconname
            ,isnull(methodname,'') as methodname  
            FROM system_function_mobile 
            WHERE id_child_child NOT IN (0,-1) 
            and id={0} AND id_child={1}
            and  isnull(Flag,'0')='1' 
            """
        sql=sql.format(centid,sectionid)
        rst = result_by_query(sql)
        return rst





