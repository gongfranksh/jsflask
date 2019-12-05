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
