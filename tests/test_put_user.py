import json

import requests
from jsonschema.validators import validate

from utils import load_schema


def test_put_user_schema_validate():
    response = requests.put("https://reqres.in/api/users/5", data={"name": "morpheus", "job": "zion resident"})
    body = response.json()
    schema = load_schema("put_user.json")

    assert response.status_code == 200
    with open(schema) as file:
        validate(body, schema=json.loads(file.read()))
