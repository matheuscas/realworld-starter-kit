from main import app
import pytest
import json
# import arrow

@pytest.fixture
def tags_request_fixture():
    req, res = app.test_client.get('/tags')
    return {'req': req, 'res': res, 'result': json.loads(res.body)}

def test_get_tags_returns_200(tags_request_fixture):
    'Response code is 200 OK'

    assert tags_request_fixture['res'].status == 200

def test_response_contains_tags(tags_request_fixture):
    'Response contains "tags" property'

    assert 'tags' in tags_request_fixture['result']

def test_response_tags_is_array(tags_request_fixture):
    '"tags" property returned as array'

    assert type(tags_request_fixture['result']['tags']) == list
        