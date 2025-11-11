# 自己构造 json 对象和 json_schema 来对数据进行校验操作
# 操作数组
from jsonschema.validators import validate


def json_Factory():
    json1={
        "data":[1,2,3,4,5,6],
        "str":"hello"
    }
    json2 = {
        "data": [1, 2, 3, 4, 5, 5],
        "str": "hello"
    }
    json3 = {
        "data": ["h", "e","l", "l","o"],
        "str": "hello"
    }

    # 针对数组长度进行验证
    json_schema1={
      "type": "object",
      "required": [],
      "properties": {
        "data": {
          "type": "array",
          "items": {
            "type": "number",  # 针对数组中每个元素的数据类型
          },
          "minItems": 1,  # 表示数组长度最短为 1
          "maxItems": 6, # 表示数组长度最长为 6--Passed
          # "maxItems": 5  # 表示数组长度最长为 5--failed
        },
        "str": {
          "type": "string"
        }
      }
    }

    # 针对数组中元素是否唯一进行验证
    json_schema2 = {
        "type": "object",
        "required": [],
        "properties": {
            "data": {
                "type": "array",
                "items": {
                    "type": "number",  # 针对数组中每个元素的数据类型
                },
                "uniqueItems":True  # 默认 uniqueItems 字段的值为 False，表示在数组中元素可以重复
                                    # 若将 uniqueItems 字段值修改为 True，表示在数组中元素唯一，不可以重复，上述例子中数组有两个 5
            },
            "str": {
                "type": "string"
            }
        }
    }

    # 针对数组中元素类型进行验证
    json_schema3 = {
        "type": "object",
        "required": [],
        "properties": {
            "data": {
                "type": "array",
                "items": {
                    "type": "string",  # 针对数组中每个元素的数据类型
                },
                "uniqueItems": False  # 默认 uniqueItems 字段的值为 False，表示在数组中元素可以重复
                # 若将 uniqueItems 字段值修改为 True，表示在数组中元素唯一，不可以重复，上述例子中数组有两个 5
            },
            "str": {
                "type": "string"
            }
        }
    }

    validate(instance=json1, schema=json_schema1)
    # validate(instance=json2,schema=json_schema2)
    # validate(instance=json3,schema=json_schema3)


def est_json():
    json_Factory()