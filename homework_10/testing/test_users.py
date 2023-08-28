import functools

# Декоратор для вывода успешного выполнения теста
def print_success(test_func):
    @functools.wraps(test_func)
    def wrapper(*args, **kwargs):
        result = test_func(*args, **kwargs)
        print(f'Test "{test_func.__name__}" выполнен успешно. Ошибок не обнаружено.')
        return result
    return wrapper

def test_get_users(client):
    response = client.get("/users/")
    assert response.status_code == 200


@print_success
def test_get_user_details(client):
    response = client.get(f"/users/1/")
    assert response.status_code == 200


@print_success
def test_get_user_details_not_found(client):
    response = client.get("/users/9999/")
    assert response.status_code == 404

@print_success
def test_create_user(client):
    data = {
        "user-name": "New User"
    }
    response = client.post("/users/create/", data=data, follow_redirects=True)
    assert response.status_code == 200


@print_success
def test_delete_user(client):
    response = client.post(f"/users/1/delete/", follow_redirects=True)
    assert response.status_code == 200
