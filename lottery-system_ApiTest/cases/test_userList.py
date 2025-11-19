import os

import pytest
from jsonschema.validators import validate

from utils.IOData import read_yml
from utils.Requests import Request


class TestUserList:

    url=Request().host+"base-user/find-list"
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
          "type": "array",
          "items": {
            "type": "object",
            "required": ["userId","userName","identity"],
            "properties": {
              "userId": {
                "type": "number"
              },
              "userName": {
                "type": "string"
              },
              "identity": {
                "type": "string"
              }
            }
          }
        }
      }
    }

    def test_userList_noLogin(self):
        r = Request().get(url=self.url)
        assert r.json()["msg"]=="token不存在"


    def test_userList_login(self):
        user_token=read_yml(os.getcwd()+"/data/data.yml","token")
        header={
            "user_token":user_token
        }
        r = Request().get(url=self.url,headers=header)
        assert r.json()["code"]==200
        assert r.json()["msg"]==""

    # 设置请求参数
    @pytest.mark.parametrize("identity",["ADMIN","NORMAL"])
    def test_userList_params(self,identity):
        token=read_yml(os.getcwd()+"/data/data.yml","token")
        header={
            "user_token":token
        }
        param={
            "identity":identity
        }

        r = Request().get(url=self.url,params=param,headers=header)

        validate(instance=r.json(),schema=self.schema)

        assert r.json()["code"]==200
        count=len(r.json()["data"])
        jsonData=r.json()["data"]

        # 判断返回数据的排列是否为倒序
        for i in range(0,count-1):
            assert jsonData[i]["userId"]>jsonData[i+1]["userId"]

        # 判断返回数据的身份是否符合预期
        for i in range(0,count):
            assert jsonData[i]["identity"]==identity