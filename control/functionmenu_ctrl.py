# -*- coding: utf-8 -*-
import json

from flask_restful import Resource, reqparse
from js.Branch import Branch
from jsdb.jsbranch import get_branch_all, get_branch_by_code
from jsdb.jssystemfunction import query_branch_section_menu


def abort_if_todo_doesnt_exist(branch_code):
    pass


#入参届解释器
parser = reqparse.RequestParser()


class Funtions(Resource):
    def __init__(self):
        pass

    def get(self,branch_code):
        abort_if_todo_doesnt_exist(branch_code)
        # branch = Branch('01001')
        # res=branch.get_branch_by_code(branch_code)
        res=get_branch_by_code(branch_code)
        if len(res)==0:
            return {}
        else:
            branch_list=[]
            for branch in res:
                dict_branch={}
                dict_branch['BraId']=branch['BraId']
                dict_branch['BraName']=branch['BraName']
                dict_branch['BraSName']=branch['BraSName']
                dict_branch['bn_dg_warehouseid']=branch['bn_dg_warehouseid']
                branch_list.append(dict_branch)
            return {'branch_list':branch_list},200


class FuntionsList(Resource):
    def __init__(self):
        pass

    def get(self):
        res=query_branch_section_menu()

        if len(res)==0:
            return {}
        else:
            function_list=[]
            for function in res:
                dict_function={}
                dict_function['BraId']=function['BraId']
                dict_function['BraName']=function['BraName']
                dict_function['BraSName']=function['BraSName']
                dict_function['bn_dg_warehouseid']=function['bn_dg_warehouseid']
                function_list.append(dict_function)
            return {'function_list':dict_function},200
