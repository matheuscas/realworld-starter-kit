from main import app
import pytest
import json

@pytest.fixture
def articles_comments_fixture():
    req, res = app.test_client.get('/articles/how-to-train-your-dragon/comments')
    return {'req': req, 'res': res, 'result': json.loads(res.body)}

def test_response_is_200(articles_comments_fixture):
    'Response code is 200 OK'
    
    assert articles_comments_fixture['res'].status == 200

def test_response_contains_comments(articles_comments_fixture):
    'Response contains "comments" property'

    assert 'comments' in articles_comments_fixture['result']

def test_comment_has_id(articles_comments_fixture):
    'Comment has "id" property'

    assert 'id' in articles_comments_fixture['result']['comments'][0]['comment']

def test_comment_has_body(articles_comments_fixture):
    'Comment has "body" property'

    assert 'body' in articles_comments_fixture['result']['comments'][0]['comment']

def test_comment_has_createdAt(articles_comments_fixture):
    'Comment has "createdAt" property'

    assert 'createdAt' in articles_comments_fixture['result']['comments'][0]['comment']

def test_comment_has_updatedAt(articles_comments_fixture):
    'Comment has "updatedAt" property'

    assert 'updatedAt' in articles_comments_fixture['result']['comments'][0]['comment']

def test_comment_has_author(articles_comments_fixture):
    'Comment has "author" property'

    assert 'author' in articles_comments_fixture['result']['comments'][0]['comment']
