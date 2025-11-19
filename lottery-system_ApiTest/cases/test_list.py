# 活动列表展示页测试
import os

from utils.IOData import read_yml
from utils.Requests import Request
from jsonschema.validators import validate

class TestList:
    # http://8.147.235.67:8080/activity/find-list?currentPage=1&pageSize=3
    url = Request().host + "activity/find-list"
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
                "required": ["total", "records"],
                "properties": {
                    "total": {
                        "type": "number"
                    },
                    "records": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "required": ["activityId", "activityName", "description", "valid"],
                            "properties": {
                                "activityId": {
                                    "type": "number"
                                },
                                "activityName": {
                                    "type": "string"
                                },
                                "description": {
                                    "type": "string"
                                },
                                "valid": {
                                    "type": "boolean"
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    def test_list_login(self):
        param = {
            "currentPage": 1,
            "pageSize": 3
        }

        # 读取yml中的登陆凭证
        token = read_yml(os.getcwd() + "/data/data.yml", "token")
        header = {
            "user_token": token
        }

        r = Request().get(url=self.url, params=param, headers=header)
        validate(instance=r.json(), schema=self.schema)

    # 没有登录凭证
    def test_list_notlogin(self):
        param = {
            "currentPage" : 1,
            "pageSize" : 3
        }
        r = Request().get(self.url, params=param)
        assert r.json()["msg"]=="token不存在"
