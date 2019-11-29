# -*- coding: utf-8 -*-
import json

from flask_restful import Resource, reqparse
from js.Branch import Branch
from jsdb.jsbranch import get_branch_all, get_branch_by_code
from jsdb.jssystemfunction import query_branch_section_menu, query_branch_function_menu
from tools.Utils import return_json_result
from tools.config import rt_ok, rt_error_01


def abort_if_todo_doesnt_exist(code):
    return return_json_result(rt_error_01, {"msg":"参数为空"})



#入参届解释器
parser = reqparse.RequestParser()


class FuntionsItem(Resource):
    def __init__(self):
        pass

    def get(self,centid,sectionid):
        abort_if_todo_doesnt_exist(centid)
        abort_if_todo_doesnt_exist(sectionid)
        # branch = Branch('01001')
        # res=branch.get_branch_by_code(branch_code)
        res=query_branch_function_menu(centid,sectionid)
        if len(res)==0:
            return return_json_result(rt_ok, {})
        else:
            function_list=[]
            for fun in res:
                dict_function={}
                dict_function['functionid']=fun['functionid']
                dict_function['functionname']=fun['functionname']
                dict_function['iconname']=fun['iconname']
                dict_function['methodname']=fun['methodname']
                function_list.append(dict_function)
            return return_json_result(rt_ok, {"menu_list":function_list})



class FuntionsList(Resource):
    def __init__(self):
        pass

    def get(self):
        res=query_branch_section_menu()
        if len(res)==0:
            return return_json_result(rt_ok, {})
        else:
            function_list=[]
            for function in res:
                dict_function={}
                dict_function['centid']=function['centid']
                dict_function['sectionid']=function['sectionid']
                dict_function['sectionname']=function['sectionname']
                function_list.append(dict_function)
            return return_json_result(rt_ok, {'function_list':function_list})
