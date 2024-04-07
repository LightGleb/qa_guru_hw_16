import json

import requests
from jsonschema.validators import validate

from utils import load_schema


def test_get_user_schema_validate():
    response = requests.get("https://reqres.in/api/users/1")
    body = response.json()
    schema = load_schema("get_user.json")

    assert response.status_code == 200
    with open(schema) as file:
        validate(body, schema=json.loads(file.read()))


def test_user_not_found():
    response = requests.get("https://reqres.in/api/users/10000")

    assert response.status_code == 404
