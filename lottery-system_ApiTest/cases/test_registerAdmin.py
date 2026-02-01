import pytest
from jsonschema.validators import validate

from utils.Requests import Request


class TestRegisterAdmin:
    def test_register_admin(self):
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

        def test_regitserAdmin_success(self):
            params = {
                "email": "77889@qq.com",
                "identity": "ADMIN",
                "name": "羊羊",
                "password": "889999",
                "phoneNumber": "17777777777"
            }
            r = Request().post(url=self.url, json=params)
            validate(instance=r.json(),schema=self.schema)
            assert r.json()["code"]==200

        # 当邮箱信息注册相同时，提示“邮箱信息不唯一”----多个用例实现参数化来实现！！！！
        @pytest.mark.parametrize("param",[{
            "email": "77889@qq.com",  #邮箱信息一致
            "identity": "ADMIN",
            "name": "羊羊",
            "password": "889999",
            "phoneNumber": "15555555555",
            "msg":"邮箱信息不唯一"
        },{
            "email": "4445555@qq.com",
            "identity": "ADMIN",
            "name": "羊羊",
            "password": "666666",
            "phoneNumber": "17777777777" ,#电话号码一致
            "msg" :"电话信息不唯一"
        }])
        def test_registerAdmin_fail(self,param):
            params = {
                "email": param["email"],
                "identity": param["identity"],
                "name": param["name"],
                "password": param["password"],
                "phoneNumber": param["phoneNumber"]
            }

            r = Request().post(url=self.url, json=params)
            validate(instance=r.json(), schema=self.schema)
            assert r.json()["code"] == 500
            assert r.json()["msg"] == param["msg"]