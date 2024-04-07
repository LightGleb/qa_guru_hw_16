import json

import requests
from jsonschema.validators import validate

from utils import load_schema


def test_post_user_schema_validate():
    response = requests.post("https://reqres.in/api/users",
                             data={"name": "morpheus", "job": "zion resident"})
    body = response.json()
    schema = load_schema("post_user.json")

    assert response.status_code == 201
    with open(schema) as file:
        validate(body, schema=json.loads(file.read()))
