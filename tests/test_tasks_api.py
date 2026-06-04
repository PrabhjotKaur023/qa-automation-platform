import requests

def test_get_tasks():
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    assert response.status_code == 200