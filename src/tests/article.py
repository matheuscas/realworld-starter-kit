from ..sanic_real_world.main import app
import pytest
import json
# import arrow

@pytest.fixture
def _app():
    req, res = app.test_client.get('/articles/how-to-train-your-dragon')
    return {'req': req, 'res': res}

def test_get_article_returns_200(_app):
    assert _app['res'].status == 200

def test_response_contains_article(_app):
    assert 'article' in json.loads(_app['res'].body)

def test_response_contains_title(_app):
    article = json.loads(_app['res'].body)
    assert 'title' in article['article']

def test_response_contains_slug(_app):
    article = json.loads(_app['res'].body)
    assert 'slug' in article['article']

def test_response_contains_body(_app):
    article = json.loads(_app['res'].body)
    assert 'body' in article['article']

def test_response_contains_createdAt(_app):
    article = json.loads(_app['res'].body)
    assert 'createdAt' in article['article']

# def test_response_createdAt_ISO8601_timestamp(_app):
#     article = json.loads(_app['res'].body)
#     date = arrow.get(article['article']['createdAt'])
#     assert date.isoformat() == article['article']['createdAt']

# def test_response_updatedAt_ISO8601_timestamp(_app):
#     article = json.loads(_app['res'].body)
#     date = arrow.get(article['article']['updatedAt'])
#     assert date.isoformat() == article['article']['updatedAt']

def test_response_contains_description(_app):
    article = json.loads(_app['res'].body)
    assert 'description' in article['article']

def test_response_contains_tagList(_app):
    article = json.loads(_app['res'].body)
    assert 'tagList' in article['article']

def test_response_tagList_is_list(_app):
    article = json.loads(_app['res'].body)
    assert type(article['article']['tagList']) == list

def test_response_contains_author(_app):
    article = json.loads(_app['res'].body)
    assert 'author' in article['article']

def test_response_contains_favorited(_app):
    article = json.loads(_app['res'].body)
    assert 'favorited' in article['article']

def test_response_contains_favoritesCount(_app):
    article = json.loads(_app['res'].body)
    assert 'favoritesCount' in article['article']

def test_response_favoritesCount_is_integer(_app):
    article = json.loads(_app['res'].body)
    assert type(article['article']['favoritesCount']) == int
