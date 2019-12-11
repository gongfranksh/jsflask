import json
from decimal import Decimal
import datetime


class MsSqlResultDataEncoder(json.JSONEncoder):
    def default(self, obj):

        if isinstance(obj, Decimal):
            return float(obj)

        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')

        if isinstance(obj, bytes):
            return str(obj);

        return super(MsSqlResultDataEncoder, self).default(obj)


def return_json_result(rt_id, msg):
    rst = {
        # 'state',
        'result':msg
    }
    if rt_id==200:
        rst['state']='ok'
    else:
        rst['state']='error'
    return  rst

def dict_2_redis(obj):
    if isinstance(obj,dict):
        for key,value in obj.items():
            if value is None:
                obj[key]=''

            if isinstance(value, Decimal):
                obj[key] = float(value)

            if isinstance(value, datetime.datetime):
                obj[key] = value.strftime('%Y-%m-%d %H:%M:%S')
    return obj



def dict_b_2_string(obj):
    rt={}
    for key, value in obj.items():
        itemkey = str(key, encoding="utf-8")
        itemvalue = str(value, encoding="utf-8")
        rt[itemkey] = itemvalue
    return rt
