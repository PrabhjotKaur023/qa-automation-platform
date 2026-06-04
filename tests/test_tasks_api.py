import requests

BASE_URL = "http://127.0.0.1:8000/api/tasks/"

def test_get_tasks():
    response = requests.get(BASE_URL)

    # Check response is successful
    assert response.status_code == 200

    # Check response is a list (important QA check)
    assert isinstance(response.json(), list)