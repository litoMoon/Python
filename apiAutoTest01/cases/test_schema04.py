# 对字符串进行校验
from jsonschema.validators import validate


def json_Factory():
    json={
        "str1":"hello",
        "str2":"abc123dfghji99"
    }

    json_schema={
      "type": "object",
      "required": [],
      "properties": {
        "str1": {
          "type": "string",
          "pattern":r"\S+"
        },
        "str2": {
          "type": "string"
        }
      }
    }

    validate(instance=json,schema=json_schema)

def test_json():
    json_Factory()