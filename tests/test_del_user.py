import requests


def test_get_user_schema_validate():
    response = requests.delete("https://reqres.in/api/users/1")

    assert response.status_code == 204
