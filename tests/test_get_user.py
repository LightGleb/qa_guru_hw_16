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


def test_objects_from_request_returns_in_response():
    id = 1
    email = "george.bluth@reqres.in"
    first_name = "George"
    last_name = "Bluth"
    avatar = "https://reqres.in/img/faces/1-image.jpg"
    url = "https://reqres.in/#support-heading"
    text = "To keep ReqRes free, contributions towards server costs are appreciated!"

    response = requests.get("https://reqres.in/api/users/1")
    body = response.json()

    assert body["data"]["id"] == id
    assert body["data"]["email"] == email
    assert body["data"]["first_name"] == first_name
    assert body["data"]["last_name"] == last_name
    assert body["data"]["avatar"] == avatar
    assert body["support"]["url"] == url
    assert body["support"]["text"] == text


def test_user_not_found():
    response = requests.get("https://reqres.in/api/users/10000")

    assert response.status_code == 404
