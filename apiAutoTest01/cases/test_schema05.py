# 针对对象的校验
from jsonschema.validators import validate


def json_Factory():
    json={
        "name":"zhangsan",
        "age":18,
        "gender":"man"
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
      "minProperties":2,
      "maxProperties":4
    }

    validate(instance=json,schema=json_schema)

def test_jason():
    json_Factory()