'''
两大参数
currentPage：表示当前访问那个页面
pageSize：访问当前page页的几条内容
eg: currentPage=1 & pageSize=2,表示当前访问第一页的两条数据
随着 pageSize 数据的变化查询返回的数据信息也应该随着变化
'''
import os

import pytest

from utils.IOData import read_yml
from utils.Requests import Request
from jsonschema.validators import validate

class TestPrizeList:
    url=Request().host+"prize/find-list"
    prizeList_login_schema={
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
          "required": ["total","records"],
          "properties": {
            "total": {
              "type": "number"
            },
            "records": {
              "type": "array",
              "items": {
                "type": "object",
                "required": ["prizeId","description","imageUrl","price","name"],
                "properties": {
                  "prizeId": {
                    "type": "number"
                  },
                  "description": {
                    "type": "string"
                  },
                  "imageUrl": {
                    "type": "string"
                  },
                  "price": {
                    "type": "number"
                  },
                  "name": {
                    "type": "string"
                  }
                }
              }
            }
          }
        }
      }
    }
    # 没有登陆下访问奖品列表页
    def test_prizeList_noLogin(self):
        param = {
            "currentPage": 1,
            "pageSize": 3
        }
        r = Request().get(url=self.url,params=param)
        assert r.json()["msg"]=="token不存在"


    # 登录状态下访问奖品列表页
    @pytest.mark.parametrize("num1,num2",[(1,2),(1,3)])
    def test_prizeList_login(self,num1,num2):
        token=read_yml(os.getcwd()+"/data/data.yml","token")
        header={
            "user_token":token
        }
        param = {
            "currentPage": num1,
            "pageSize": num2
        }
        r = Request().get(url=self.url,params=param,headers=header)
        # 对返回值进行 jsonschema 校验
        validate(instance=r.json(),schema=self.prizeList_login_schema)
        # 验证状态码信息
        assert r.json()["code"]==200
        # .json()返回的是字典数据，从字典数据中获取字段需要使用 ["字段名"]
        # jsonData=r.json()["data"]["records"]
        jsonData=r.json().get("data",{}).get("records",{})   # 和上面等效
        # 检查返回的奖品列表信息是否为倒序
        for i in range(0,num2-1):
            assert jsonData[i]["prizeId"] > jsonData[i+1]["prizeId"]