import server.user.service
from server.user.schema import UserSchema

# TODO - Add unit tests for all endpoints


def test_add_user(test_app, monkeypatch):
    def mock_create(data):
        return UserSchema(username=data["username"], email=data["email"])

    monkeypatch.setattr(server.user.service.UserService, "create", mock_create)
    test_data = {"username": "test_add_user", "email": "test_add_user@email.com"}
    api = test_app.test_client()

    res = api.post("/users", json=test_data)
    data = res.json

    assert res.status_code == 201
    assert "test_add_user@email.com" in data["message"]
