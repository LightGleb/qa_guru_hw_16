import json

import requests
from jsonschema.validators import validate

from utils import load_schema


def test_post_register_user_successful_schema_validate():
    response = requests.post("https://reqres.in/api/register",
                             data={"email": "eve.holt@reqres.in", "password": "pistol"})
    body = response.json()
    schema = load_schema("post_register_user_successful.json")

    assert response.status_code == 200
    with open(schema) as file:
        validate(body, schema=json.loads(file.read()))


def test_post_register_user_unsuccessful_schema_validate():
    response = requests.post("https://reqres.in/api/register",
                             data={"email": "eve.holt@reqres.in"})
    body = response.json()
    schema = load_schema("post_register_user_unsuccessful.json")

    assert response.status_code == 400
    with open(schema) as file:
        validate(body, schema=json.loads(file.read()))
