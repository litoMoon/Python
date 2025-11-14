# 自己构造 json 对象和 json_schema 来对数据进行校验操作
# 操作数值
import logging
from jsonschema.validators import validate
def json_Factory():
    json1 = {
        "name":"zhangsan",
        "age":120
    }
    json1_schema={
      "type": "object",
      "required": [],
      "properties": {
        "name": {
          "type": "string"
        },
        "age": {
          "type": "number"
        }
      }
    }
    # [minimum,maximum]
    json2_schema={
      "type": "object",
      "required": [],
      "properties": {
        "name": {
          "type": "string"
        },
        "age": {
          "type": "number",
          "minimum": 0,
          "maximum": 120
        }
      }
    }

    #(exclusiveMinimum,exclusiveMaximum)--前缀有exclusive的不包含这两个边界值
    json3_schema={
      "type": "object",
      "required": [],
      "properties": {
        "name": {
          "type": "string"
        },
        "age": {
          "type": "number",
          "exclusiveMinimum": 0,
          "exclusiveMaximum": 120  # 测试结果报错，这里输出是不包含 0 和 120 这两个边界值的
        }
      }
    }

    validate(instance=json1,schema=json3_schema)
    logging.basicConfig(level=logging.INFO)
    logging.info("this is a info message")

def test_data_json():
    json_Factory()