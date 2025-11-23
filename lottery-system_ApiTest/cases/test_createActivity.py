'''
创建活动页面需要传递的参数有 activityName、description、prizeList、userList，
这几个参数任缺一个响应的结果都是”系统异常“
'''
import os

from Tools.scripts.generate_opcode_h import header
from jsonschema.validators import validate

from utils.IOData import read_yml
from utils.Requests import Request


class TestActivityCreate:
    url=Request().host+"activity/create"
    schema={
      "type": "object",
      "required": ["code","msg","data"],
      "properties": {
        "code": {
          "type": "number"
        },
        "msg": {
          "type": "string"
        },
        "data": {
          "type": "object",
          "required": ["type"],
          "properties": {
            "activityId": {
              "type": "number"
            }
          }
        }
      }
    }

    # 有登录凭证
    def test_activity_create_success(self):
        # 获取token信息
        token=read_yml(os.getcwd()+"/data/data.yml","token")
        header={
            "User_token":token
        }
        #请求参数信息
        param={
            "activityName":"接口测试3",
            "description":"接口测试3的描述",
            "prizeList":[{
                "prizeId":39,
                "prizeAmount":1,
                "prizeTiers":"FIRST_PRIZE"
            }],
            "userList":[
                {
                 "userId":79,
                 "userName":"喜喜"
                },{
                    "userId":78,
                    "userName":"蹦子"
                }
            ]
        }
        r = Request().post(url=self.url,json=param,headers=header)
        validate(instance=r.json(),schema=self.schema)
        assert r.status_code==200

    #没有登录凭证
    def test_activity_create_Nologin(self):
        # 获取token信息
        #请求参数信息
        param={
            "activityName":"接口测试3",
            "description":"接口测试3的描述",
            "prizeList":[{
                "prizeId":39,
                "prizeAmount":1,
                "prizeTiers":"FIRST_PRIZE"
            }],
            "userList":[
                {
                 "userId":79,
                 "userName":"喜喜"
                },{
                    "userId":78,
                    "userName":"蹦子"
                }
            ]
        }
        r = Request().post(url=self.url,json=param)
        assert r.status_code==200
        assert r.json()["code"]==500


