def test_users_list_status_code(client):
    response = client.get(f'/list/')
    assert response.status_code == 200
