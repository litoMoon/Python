import pytest
from jsonschema.validators import validate

from utils.Requests import Request


class TestRegisterUser:

    url = Request().host + "register"
    schema = {
        "type": "object",
        "required": ["code", "msg", "data"],
        "properties": {
            "code": {
                "type": "number"
            },
            "msg": {
                "type": "string"
            },
            "data": {
                "type": "object",
                "required": ["userId"],
                "properties": {
                    "userId": {
                        "type": "number"
                    }
                }
            }
        }
    }

    # 注册普通用户成功
    def test_registerUser_success(self):
        params = {
            "email": "22112222@qq.com",
            "identity": "NORMAL",
            "name": "喜喜",
            "password": "",
            "phoneNumber": "15556984232"
        }
        r = Request().post(url=self.url, json=params)
        validate(instance=r.json(), schema=self.schema)
        assert r.json()["code"]==200

    # 当邮箱信息注册相同时，提示“邮箱信息不唯一”----多个用例实现参数化来实现！！！！
    @pytest.mark.parametrize("param", [{
        "email": "22112222@qq.com",
        "identity": "NORMAL",
        "name": "美美",
        "password": "",
        "phoneNumber": "15556984231",
        "msg": "邮箱信息不唯一"
    }, {
        "email": "22221123@qq.com",
        "identity": "NORMAL",
        "name": "美美",
        "password": "",
        "phoneNumber": "15556984232",
        "msg": "电话信息不唯一"
    }])

    # 注册普通用户失败
    def test_registerUser_fail(self, param):
        params = {
            "email": param["email"],
            "identity": param["identity"],
            "name": param["name"],
            "password": param["password"],
            "phoneNumber": param["phoneNumber"]
        }
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
              "type": "null"
            }
          }
        }
        r = Request().post(url=self.url, json=params)
        validate(instance=r.json(), schema=schema)
        assert r.json()["code"] == 500
        assert r.json()["msg"] == param["msg"]
