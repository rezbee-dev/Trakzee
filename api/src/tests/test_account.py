import pytest


################
# REGISTRATION
################
def test_registration(test_app, test_database):
    test_data = {"email": "test_registration@email.com", "password": "test_password"}
    api = test_app.test_client()

    res = api.post("/api/account/register", json=test_data)
    data = res.json

    assert res.status_code == 201
    assert data["id"]
    assert data["verified"]
    assert test_data["email"] in data["email"]
    assert "password" not in data


def test_registration_duplicate(test_app, test_database):
    test_data = {"email": "test_registration_duplicate@email.com", "password": "test_password"}
    api = test_app.test_client()

    api.post("/api/account/register", json=test_data)
    res = api.post("/api/account/register", json=test_data)
    data = res.json

    assert res.status_code == 409
    assert "Email already taken!" in data["message"]


@pytest.mark.parametrize(
    "payload", [{}, {"email": "test_registration_invalid@email.com"}, {"password": "test_password"}]
)
def test_registration_invalid(test_app, test_database, payload):
    api = test_app.test_client()

    res = api.post("/api/account/register", json=payload)
    data = res.json

    assert res.status_code == 400
    assert res.content_type == "application/json"
    assert "Input payload validation failed" in data["message"]


################
# Login
################
def test_login(test_app, test_database, add_account):
    test_data = {"email": "test_login@email.com", "password": "test_password"}
    add_account(test_data)
    api = test_app.test_client()

    res = api.post("/api/account/login", json=test_data)
    data = res.json
    # src: https://stackoverflow.com/a/66825563
    cookies = res.headers.getlist("Set-Cookie")
    refresh_tokens = [cookie for cookie in cookies if "refresh_token" in cookie]

    assert res.status_code == 200
    assert data["access_token"]
    assert len(refresh_tokens) == 2


def test_login_unregistered(test_app, test_database):
    test_data = {"email": "test_login_unregistered@email.com", "password": "test_password"}
    api = test_app.test_client()

    res = api.post("/api/account/login", json=test_data)
    data = res.json

    assert res.status_code == 404
    assert "Account not found. Please register or login again" in data["message"]


@pytest.mark.parametrize(
    "payload", [{}, {"email": "test_registration_invalid@email.com"}, {"password": "test_password"}]
)
def test_login_invalid(test_app, test_database, payload):
    api = test_app.test_client()

    res = api.post("/api/account/login", json=payload)
    data = res.json

    assert res.status_code == 400
    assert res.content_type == "application/json"
    assert "Input payload validation failed" in data["message"]
