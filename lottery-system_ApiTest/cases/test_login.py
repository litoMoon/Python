# 针对登录接口进行测试
import os

import pytest
from jsonschema.validators import validate

from utils.IOData import write_yml
from utils.Requests import Request


class Testlogin:
    comdata=Request().host

    # 用户账号和密码信息参数化
    @pytest.mark.parametrize("loginParams", [
        {
            # 情况一：账号密码均为空
            "loginName": "",
            "password": "",
            "errMsg": "系统异常"
        }, {
            # 情况二：账号为空，密码不为空
            "loginName": "",
            "password": "555441",
            "errMsg": "系统异常"
        }, {
            # 情况三：账号不为空，密码为空---前三个返回的 msg：系统异常
            "loginName": "18111111111",
            "password": "",
            "errMsg": "系统异常"
        }, {
            # 情况四：账号不存在---应该返回的 msg：用户信息不存在
            "loginName": "13473728920",
            "password": "555555",
            "errMsg": "用户信息为空"
        }])
    def test_login_fail(self, loginParams):
        url = self.comdata + "password/login"
        data = {
            "loginName": loginParams["loginName"],
            "password": loginParams["password"]
        }
        # 参数化发起请求
        result = Request().post(url, json=data)
        login_schema = {
            "type": "object",
            "required": [],
            "properties": {
                "code": {
                    "type": "number"
                },
                "msg": {
                    "type": "string"
                },
                #  返回的 "data":"null"---与之对应的type类型也为 null
                "data": {
                    "type": "null"
                }
            }
        }
        validate(instance=result.json(), schema=login_schema)
        assert result.json()["code"] == 500
        assert result.json()["msg"] == loginParams["errMsg"]




    # 进行参数化设计
    @pytest.mark.parametrize("loginParams",[
        {
        "loginName":"18111111111",
        "password":"888888"
    },{
           "loginName":"18723555441",
            "password":"555441"
        }])
    def test_login_success(self,loginParams):
        # 请求url
        url=self.comdata+"password/login"
        data={
            "loginName":loginParams["loginName"],
            "password":loginParams["password"]
        }
        r=Request().post(url,json=data)
        # 将 token 存入到 yml 文件中
        # os.getcwd()方法用于获取当前目录路径
        data = {
            "token": r.json()["data"]["token"]
        }
        write_yml(os.getcwd() + "/data/data.yml", data)
        # 接收到响应数据后与 schema 进行匹配对比
        login_schema={
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
              "required": ["identity","token"],
              "properties": {
                "identity": {
                  "type": "string"
                },
                "token": {
                  "type": "string"
                }
              }
            }
          }
        }
        # 将返回的数据与json_schema进行比对
        validate(instance=r.json(),schema=login_schema)
        # 当数据类型什么的正确了之后，需要对返回的具体数据值做更进一步的校验
        assert r.json()["code"]==200
        assert r.json()["data"]["identity"]=='ADMIN'




