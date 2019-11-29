# -*- coding: utf-8 -*-
from js.jsEntity import JsEntity


class Branch(JsEntity):

    def __init__(self,branchcode):
        JsEntity.__init__(self, "BRANCH",branchcode)



    def get_branch_all(self):
        sql= " SELECT * FROM branch WHERE BraType='0' AND Status='0' ORDER BY BraName,braid "
        rst = self.get_remote_result_by_sql(sql)
        return rst

    def get_branch_list(self):
        sql= " SELECT * FROM branch WHERE BraType='0' AND Status='0' ORDER BY BraName,braid "
        rst = self.get_remote_list_by_sql(sql)
        return rst

    def get_branch_by_code(self,branchcode):
        sql= """
             SELECT * FROM branch WHERE BraType='0' AND Status='0'  and braid='{0}'  ORDER BY BraName,braid 
        """
        sql=sql.format(branchcode)
        rst = self.get_remote_list_by_sql(sql)
        return rst
