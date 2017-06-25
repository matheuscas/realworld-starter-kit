from ..sanic_real_world.main import app
import pytest
import json
# import arrow

@pytest.fixture
def articles_slug_fixture():
    req, res = app.test_client.get('/articles/how-to-train-your-dragon')
    return {'req': req, 'res': res}

@pytest.fixture
def articles_fixture():
    req, res = app.test_client.get('/articles')
    return {'req': req, 'res': res}

def test_get_article_returns_200(articles_slug_fixture, articles_fixture):
    assert articles_slug_fixture['res'].status == 200

def test_response_contains_article(articles_slug_fixture):
    assert 'article' in json.loads(articles_slug_fixture['res'].body)

def test_response_contains_title(articles_slug_fixture):
    article = json.loads(articles_slug_fixture['res'].body)
    assert 'title' in article['article']

def test_response_contains_slug(articles_slug_fixture):
    article = json.loads(articles_slug_fixture['res'].body)
    assert 'slug' in article['article']

def test_response_contains_body(articles_slug_fixture):
    article = json.loads(articles_slug_fixture['res'].body)
    assert 'body' in article['article']

def test_response_contains_createdAt(articles_slug_fixture):
    article = json.loads(articles_slug_fixture['res'].body)
    assert 'createdAt' in article['article']

# def test_response_createdAt_ISO8601_timestamp(articles_slug_fixture):
#     article = json.loads(articles_slug_fixture['res'].body)
#     date = arrow.get(article['article']['createdAt'])
#     assert date.isoformat() == article['article']['createdAt']

# def test_response_updatedAt_ISO8601_timestamp(articles_slug_fixture):
#     article = json.loads(articles_slug_fixture['res'].body)
#     date = arrow.get(article['article']['updatedAt'])
#     assert date.isoformat() == article['article']['updatedAt']

def test_response_contains_description(articles_slug_fixture):
    article = json.loads(articles_slug_fixture['res'].body)
    assert 'description' in article['article']

def test_response_contains_tagList(articles_slug_fixture):
    article = json.loads(articles_slug_fixture['res'].body)
    assert 'tagList' in article['article']

def test_response_tagList_is_list(articles_slug_fixture):
    article = json.loads(articles_slug_fixture['res'].body)
    assert type(article['article']['tagList']) == list

def test_response_contains_author(articles_slug_fixture):
    article = json.loads(articles_slug_fixture['res'].body)
    assert 'author' in article['article']

def test_response_contains_favorited(articles_slug_fixture):
    article = json.loads(articles_slug_fixture['res'].body)
    assert 'favorited' in article['article']

def test_response_contains_favoritesCount(articles_slug_fixture):
    article = json.loads(articles_slug_fixture['res'].body)
    assert 'favoritesCount' in article['article']

def test_response_favoritesCount_is_integer(articles_slug_fixture):
    article = json.loads(articles_slug_fixture['res'].body)
    assert type(article['article']['favoritesCount']) == int
