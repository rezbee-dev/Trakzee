from server.account.auth import AccountAuth


def test_encode_token(test_app, test_database, add_account):
    test_data = {"email": "test_encode_token_email@email.com", "password": "test_password"}
    account = add_account(test_data)
    token = AccountAuth.encode_token(account_id=account.id, token_type="access")
    assert isinstance(token, str)


def test_decode_token(test_app, test_database, add_account):
    test_data = {"email": "test_decode_token_email@email.com", "password": "test_password"}
    account = add_account(test_data)
    token = AccountAuth.encode_token(account_id=account.id, token_type="access")

    assert isinstance(token, str)
    assert AccountAuth.decode_token(token) == account.id
