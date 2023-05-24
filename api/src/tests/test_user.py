# POST /users
def test_add_user(test_app, test_database):
    # Arrange
    test_data = {"username": "test_add_user", "email": "test_add_user@email.com"}
    api = test_app.test_client()

    # Act
    res = api.post("/users", json=test_data)
    data = res.json

    # Assert
    assert res.status_code == 201
    assert "test_add_user@email.com" in data["message"]


def test_add_user_empty(test_app, test_database):
    test_data = {}
    api = test_app.test_client()

    res = api.post("/users", json=test_data)
    data = res.json

    assert res.status_code == 400
    assert "Input payload validation failed" in data["message"]


def test_add_user_missing_username(test_app, test_database):
    test_data = {"email": "test_add_user_missing_username@email.com"}
    api = test_app.test_client()

    res = api.post("/users", json=test_data)
    data = res.json

    assert res.status_code == 400
    assert "Input payload validation failed" in data["message"]


def test_add_user_missing_email(test_app, test_database):
    test_data = {"username": "test_add_user_missing_email"}
    api = test_app.test_client()

    res = api.post("/users", json=test_data)
    data = res.json

    assert res.status_code == 400
    assert "Input payload validation failed" in data["message"]


def test_add_user_duplicate_email(test_app, test_database):
    test_data = {
        "username": "test_add_user_duplicate_email",
        "email": "test_add_user_duplicate_email@email.com",
    }
    api = test_app.test_client()

    api.post("/users", json=test_data)
    res = api.post("/users", json=test_data)
    data = res.json

    assert res.status_code == 409
    assert "Email already exists!" in data["message"]


# GET /users/id
def test_get_user(test_app, test_database, add_user):
    test_data = {"username": "test_get_user", "email": "test_get_user@email.com"}
    user = add_user(test_data)
    api = test_app.test_client()

    res = api.get(f"/users/{user.id}")
    data = res.json

    assert res.status_code == 200
    assert "test_get_user" in data["username"]
    assert "test_get_user@email.com" in data["email"]


def test_get_user_invalid_id(test_app, test_database):
    api = test_app.test_client()

    res = api.get("/users/5")
    data = res.json

    assert res.status_code == 404
    assert "User 5 does not exist" in data["message"]


# GET /users
def test_get_all_users(test_app, test_database, add_user, delete_users):
    test_data = {
        "username": "test_get_all_users",
        "email": "test_get_all_users@email.com",
    }
    test_data_2 = {
        "username": "test_get_all_users_2",
        "email": "test_get_all_users_2@email.com",
    }
    delete_users()
    add_user(test_data)
    add_user(test_data_2)
    api = test_app.test_client()

    res = api.get("/users")
    data = res.json

    assert res.status_code == 200
    assert len(data) == 2
    assert "test_get_all_users" in data[0]["username"]
    assert "test_get_all_users@email.com" in data[0]["email"]
    assert "test_get_all_users_2" in data[1]["username"]
    assert "test_get_all_users_2@email.com" in data[1]["email"]


# DELETE /users/id
def test_remove_user(test_app, test_database, add_user, delete_users):
    test_data = {
        "username": "test_remove_user",
        "email": "test_remove_user@email.com",
    }
    delete_users()
    user = add_user(test_data)
    api = test_app.test_client()

    # Get initial resources
    res = api.get("/users")
    data = res.json

    assert res.status_code == 200
    assert len(data) == 1

    # Delete resource
    res2 = api.delete(f"/users/{user.id}")
    data2 = res2.json

    assert res2.status_code == 200
    assert f"{test_data['email']} was removed!" in data2["message"]

    # Get resources
    res3 = api.get("/users")
    data3 = res3.json

    assert res3.status_code == 200
    assert len(data3) == 0


def test_remove_user_invalid_id(test_app, test_database):
    api = test_app.test_client()

    res = api.delete("/users/999")
    data = res.json

    assert res.status_code == 404
    assert "User 999 does not exist" in data["message"]


# PUT /users/id
def test_update_user(test_app, test_database, add_user):
    test_data = {
        "username": "test_update_user",
        "email": "test_update_user@email.com",
    }
    test_data_2 = {
        "username": "test_update_user_2",
        "email": "test_update_user_2@email.com",
    }
    user = add_user(test_data)
    api = test_app.test_client()

    res = api.put(f"/users/{user.id}", json=test_data_2)
    data = res.json

    assert res.status_code == 200
    assert f"{user.id} was updated!" in data["message"]

    res2 = api.get(f"/users/{user.id}")
    data2 = res2.json

    assert res2.status_code == 200
    assert test_data_2["username"] in data2["username"]
    assert test_data_2["email"] in data2["email"]


def test_update_user_empty(test_app, test_database, add_user):
    api = test_app.test_client()

    res = api.put("/users/1", json={})
    data = res.json

    assert res.status_code == 400
    assert "Input payload validation failed" in data["message"]


def test_update_user_missing_username(test_app, test_database, add_user):
    test_data = {
        "email": "test_update_user_missing_username@email.com",
    }
    api = test_app.test_client()

    res = api.put("/users/1", json=test_data)
    data = res.json

    assert res.status_code == 400
    assert "Input payload validation failed" in data["message"]


def test_update_user_missing_email(test_app, test_database, add_user):
    test_data = {
        "username": "test_update_user_missing_email",
    }
    api = test_app.test_client()

    res = api.put("/users/1", json=test_data)
    data = res.json

    assert res.status_code == 400
    assert "Input payload validation failed" in data["message"]


def test_update_user_invalid_id(test_app, test_database, add_user):
    test_data = {
        "username": "test_update_user",
        "email": "test_update_user@email.com",
    }
    api = test_app.test_client()

    res = api.put("/users/999", json=test_data)
    data = res.json

    assert res.status_code == 404
    assert "User 999 does not exist" in data["message"]
