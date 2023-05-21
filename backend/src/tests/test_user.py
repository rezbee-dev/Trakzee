import json

def test_add_user(test_app, test_database):
    test_data = {
        'username': 'test',
        'email': 'test@email.com'
    }
    
    api =  test_app.test_client()
    res = api.post('/users', json=test_data)
    print(res)
    data = res.json
    assert res.status_code == 201
    assert 'test@email.com' in data['message']