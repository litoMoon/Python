#测试必须属性
from jsonschema.validators import validate
def json_Factory():
    json={
        "name":"zhangsan",
        "age":18,
        "gender":"man",
        "height":1.67
    }

    json_schema={
      "type": "object",
      "required": ["name","height"],
      "properties": {
        "name": {
          "type": "string"
        },
        "age": {
          "type": "number"
        },
        "gender": {
          "type": "string"
        }
      },
      "minProperties":2,
      "maxProperties":4,
      #当 additionalProperties 设置为 false 时，表示 json 中不允许出现 schema 中不存在的值
      # additionalProperties 默认值为 True,表示允许出现
      # "additionalProperties":False
    }

    validate(instance=json, schema=json_schema)

def est_json():
    json_Factory()

