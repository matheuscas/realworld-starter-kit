from main import app
import pytest
import json
# import arrow

@pytest.fixture
def profile_request_fixture():
    req, res = app.test_client.get('/profiles/jake')
    return {'req': req, 'res': res, 'result': json.loads(res.body)}

@pytest.fixture
def post_profile_request_fixture():
    req, res = app.test_client.post('/profiles/jake/follow')
    return {'req': req, 'res': res, 'result': json.loads(res.body)}

@pytest.fixture
def delete_profile_request_fixture():
    req, res = app.test_client.delete('/profiles/jake/follow')
    return {'req': req, 'res': res, 'result': json.loads(res.body)}

def test_get_profile_returns_200(profile_request_fixture):
    'Response code is 200 OK'

    assert profile_request_fixture['res'].status == 200

def test_get_profile_returns_404():
    'Response code is 404'

    req, res = app.test_client.get('/profiles/rake')

    assert res.status == 404

def test_response_contains_profile(profile_request_fixture):
    'Response contains "profile" property'

    assert 'profile' in profile_request_fixture['result']

def test_profile_contains_username(profile_request_fixture):
    'Profile has "username" property'

    assert 'username' in profile_request_fixture['result']['profile']

def test_profile_contains_bio(profile_request_fixture):
    'Profile has "bio" property'

    assert 'bio' in profile_request_fixture['result']['profile']

def test_profile_contains_image(profile_request_fixture):
    'Profile has "image" property'

    assert 'image' in profile_request_fixture['result']['profile']

def test_profile_contains_following(profile_request_fixture):
    'Profile has "following" property'

    assert 'following' in profile_request_fixture['result']['profile']

def test_profile_following_true(post_profile_request_fixture):
    'Profile\'s "following" property is true'

    assert post_profile_request_fixture['result']['profile']['following']

def test_profile_following_false(delete_profile_request_fixture):
    'Profile\'s "following" property is false'

    assert not delete_profile_request_fixture['result']['profile']['following']
