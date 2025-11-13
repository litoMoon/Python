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
      "required": [],
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
      "dependentRequired":{
          "age": ["name"]
          # "age":["name","bbb"] 注意这里未通过，这里表示如果age想要存在，那么 name 和 bbb 都必须要存在，有一个不存在就会报错
      }
    }
    validate(instance=json,schema=json_schema)

def est_json():
    json_Factory()