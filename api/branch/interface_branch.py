# -*- coding: utf-8 -*-
import json

from flask import request
from flask_restful import Resource, reqparse

from common.common_login_helper import login_required
from common.common_model_enum import modelEnum
from common.common_request_process import req
from common.common_response_code import response_code
from common.common_response_process import response_result_process
from core.user_singleton import user_singleton
from js.Branch import Branch
from jsdb.jsbranch import get_branch_all, get_branch_by_code
from tools.Utils import return_json_result
from tools.config import rt_ok
from utils.api_version_verify import api_version
from utils.log_helper import lg


class BranchItem(Resource):
    @api_version
    @login_required
    def get(self,branch_code):
        res=get_branch_by_code(branch_code)
        if len(res)==0:

            return return_json_result(rt_ok,{})
        else:
            branch_list=[]
            for branch in res:
                dict_branch={}
                dict_branch['BraId']=branch['BraId']
                dict_branch['BraName']=branch['BraName'].encode('latin1').decode('gbk')
                dict_branch['BraSName']=branch['BraSName'].encode('latin1').decode('gbk')
                dict_branch['bn_dg_warehouseid']=branch['bn_dg_warehouseid']
                branch_list.append(dict_branch)
            return return_json_result(rt_ok, {'branch_list':branch_list})


class Branchlist(Resource):
    @api_version
    @login_required
    def get(self, version, user_id=None):
        xml = request.args.get('format')
        try:
            body = modelEnum.user.value.get('body')
            if user_id is None:
                request_data = req.request_process(request, xml, modelEnum.user.value)
                if isinstance(request_data, bool):
                    request_data = response_code.REQUEST_PARAM_FORMAT_ERROR
                    return response_result_process(request_data, xml=xml)
                if not request_data:
                    res = get_branch_all()
                    data = response_code.SUCCESS
                    data['data'] = res



                    # data = user_singleton.get_users_info()
                    # data = UserSingleton.get_all_users(self)
                # else:
                #     fields = ['current_page', 'page_size']
                #     must = req.verify_all_param_must(request_data, fields)
                #     if must:
                #         return response_result_process(must, xml=xml)
                #     par_type = {'page_size': int, 'current_page': int, 'search_data': dict}
                #     param_type = req.verify_all_param_type(request_data, par_type)
                #     if param_type:
                #         return response_result_process(param_type, xml=xml)
                #
                #     current_page, page_size = int(request_data.get('current_page')), int(request_data.get('page_size'))
                #     search_data = request_data.get('search_data') if request_data.get('search_data') else {}
                #     data = user_singleton.get_users_info(current_page, page_size, search_data)
            else:
                data = user_singleton.get_user_info_by_id(user_id)

            return response_result_process(data, xml_structure_str=body, xml=xml)
        except Exception as e:
            lg.error(e)
            error_data = response_code.GET_DATA_FAIL
            return response_result_process(error_data, xml=xml)



    # def get(self):
    #     res=get_branch_all()
    #
    #     if len(res)==0:
    #         return {}
    #     else:
    #         branch_list=[]
    #         for branch in res:
    #             dict_branch={}
    #             dict_branch['BraId']=branch['BraId']
    #             dict_branch['BraName']=branch['BraName']
    #             dict_branch['BraSName']=branch['BraSName']
    #             dict_branch['bn_dg_warehouseid']=branch['bn_dg_warehouseid']
    #             branch_list.append(dict_branch)
    #         return return_json_result(200, {'branch_list': branch_list})
