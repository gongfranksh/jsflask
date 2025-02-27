#!/usr/bin/python
# -*- coding: UTF-8 -*
"""
@author：weiliang
@file_name: resource.py
@create date: 2019-10-27 13:28 
@blog https://leezhonglin.github.io
@csdn https://blog.csdn.net/qq_33196814
@file_description：
"""
from flask_restful import Api

from api.branch.interface_branch import Branchlist
from api.department.interface_department import interfaceDepartment
from api.department.interface_department_staff import interfaceDepartmentStaff
from api.login.interface_login import interfaceLogin
from api.sku.interface_sku import SkuList, SkuItem, BranchSkuList, BranchSkuList2
from api.role.interface_permission import interfacePermission
from api.role.interface_role import interfaceRole
from api.role.interface_role_permission import interfaceRolePermission
from api.user.interface_basic import interfaceUserBasic
from api.user.interface_password import interfacePassword
from api.user.interface_user import interfaceUser
from api.user_group.interface_user_group import interfaceUserGroup
from api.user_group.interface_user_group_role import interfaceUserGroupRole
from api.user_group.interface_user_group_staff import interfaceUserGroupStaff

api = Api()

# 部门管理
api.add_resource(
    interfaceDepartment,
    '/mfjpos/<version>/department',
    '/mfjpos/<version>/department/<int:dpt_id>'
)


api.add_resource(
    interfaceDepartmentStaff,
    '/mfjpos/<version>/department/staff/<int:dpt_id>'
)

# 用户
api.add_resource(
    interfaceUser,
    '/mfjpos/<version>/user',
    '/mfjpos/<version>/user/<int:user_id>',

)

# 密码
api.add_resource(
    interfacePassword,
    '/mfjpos/<version>/user/<int:user_id>/password'
)

# 基本信息修改
api.add_resource(
    interfaceUserBasic,
    '/mfjpos/<version>/user/<int:user_id>/base/info'
)

# 角色
api.add_resource(
    interfaceRole,
    '/mfjpos/<version>/role',
    '/mfjpos/<version>/role/<int:role_id>'
)
#  角色权限
api.add_resource(
    interfaceRolePermission,
    '/mfjpos/<version>/role/<role_id>/permission'
)
# 权限
api.add_resource(
    interfacePermission,
     '/mfjpos/<version>/permission'
)

# 用户组
api.add_resource(
    interfaceUserGroup,
    '/mfjpos/<version>/user/group',
    '/mfjpos/<version>/user/group/<int:group_id>'
)


api.add_resource(
    interfaceUserGroupStaff,
    '/mfjpos/<version>/user/group/<int:group_id>/staff'
)

# 获取用户组的角色信息
api.add_resource(
    interfaceUserGroupRole,
    '/mfjpos/<version>/user/group/<int:group_id>/role'
)

api.add_resource(
    interfaceLogin,
    '/mfjpos/<version>/login'
)


# 获取门店清单
api.add_resource(
    Branchlist,
    '/mfjpos/<version>/branch'
)


# 获取商品资料
api.add_resource(
    SkuList,
    '/mfjpos/<version>/skulist'
)


# 获取商品资料
api.add_resource(
    SkuItem,
    '/mfjpos/<version>/skuitem/<proid>'
)


# 获取门店商品资料
api.add_resource(
    BranchSkuList,
    '/mfjpos/<version>/branchskulist'
)

# 获取门店商品资料
api.add_resource(
    BranchSkuList2,
    '/mfjpos/<version>/branchskulist2'
)


