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


def test_name_job_from_request_returns_in_response():
    name = "morpheus"
    job = "leader"

    response = requests.put("https://reqres.in/api/users/5",
                            data={"name": {name}, "job": {job}})
    body = response.json()

    assert body["name"] == name
    assert body["job"] == job
