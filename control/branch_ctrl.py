# -*- coding: utf-8 -*-
import json

from flask_restful import Resource, reqparse
from js.Branch import Branch


def abort_if_todo_doesnt_exist(branch_code):
    pass


#入参届解释器
parser = reqparse.RequestParser()


class BranchItem(Resource):
    def __init__(self):
        pass


    def get(self,branch_code):
        abort_if_todo_doesnt_exist(branch_code)
        branch = Branch('01001')
        res=branch.get_branch_by_code(branch_code)
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




class Branchlist(Resource):
    def __init__(self):
        pass

    def get(self):
        branch=Branch('01001')
        # res=branch.get_branch_all()
        res=branch.get_branch_list()

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
