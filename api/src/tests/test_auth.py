from server.account.auth import AccountAuth

def test_encode_token(test_app, test_database, add_user):
    test_data = {
        "username": "test_encode_token",
        "email": "test_encode_token_email@email.com",
        "password": "test_password"
    }
    user = add_user(test_data)
    token = AccountAuth.encode_token(user_id=user.id, token_type='access')
    assert isinstance(token, str)
    
def test_decode_token(test_app, test_database, add_user):
    test_data = {
        "username": "test_decode_token",
        "email": "test_decode_token_email@email.com",
        "password": "test_password"
    }
    user = add_user(test_data)
    token = AccountAuth.encode_token(user_id=user.id, token_type='access')
    
    assert isinstance(token, str)
    assert AccountAuth.decode_token(token) == user.id
