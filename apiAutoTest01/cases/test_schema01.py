# schema 是对响应的 JSON 结果进行的解析操作
# 对项目接口发起请求
import requests
from jsonschema.validators import validate
def send_request():
    url="http://8.147.235.67:8080/activity/find-list?currentPage=1&pageSize=1"
    User_token={
        "User_token":"eyJhbGciOiJIUzI1NiJ9.eyJpZGVudGl0eSI6IkFETUlOIiwiaWQiOjY0LCJpYXQiOjE3NjI4NDg1NjMsImV4cCI6MTc2Mjg1MjE2M30.TcZmh7X31PsSVqGb4NW1cQmCik0ZkXY9FnHxXmLVWdg"}

    result=requests.get(url=url,headers=User_token)
    return result.json()

def est_send():
    r=send_request()
    json_schema={
      "type": "object",
      "required": [],
      "properties": {
        "code": {
          "type": "number"
        },
        "msg": {
          "type": "string"
        },
        "data": {
          "type": "object",
          "required": [],
          "properties": {
            "total": {
              "type": "number"
            },
            "records": {
              "type": "array",
              "items": {
                "type": "object",
                "required": [],
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

    # 通过json_schema来校验 抽奖接口 返回值的格式是否正确
    validate(r,json_schema)
