from main import app
import pytest
import json
# import arrow

@pytest.fixture
def articles_slug_fixture():
    req, res = app.test_client.get('/articles/how-to-train-your-dragon')
    return {'req': req, 'res': res}

@pytest.fixture(params=['/articles/how-to-train-your-dragon', '/articles'])
def articles_fixture(request):
    req, res = app.test_client.get(request.param)
    return {'req': req, 'res': res, 'result': json.loads(res.body)}

def test_get_article_returns_200(articles_fixture):
    'Response code is 200 OK'

    assert articles_fixture['res'].status == 200

def test_response_contains_article(articles_fixture):
    'Response contains "articles" property'

    if isinstance(articles_fixture['result'], list):
        assert 'article' in articles_fixture['result'][0]
    else:
        assert 'article' in articles_fixture['result']

def test_response_contains_title(articles_fixture):
    'Article has "title" property'

    if isinstance(articles_fixture['result'], list):
        assert 'title' in articles_fixture['result'][0]['article']
    else:
        assert 'title' in articles_fixture['result']['article']

def test_response_contains_slug(articles_fixture):
    'Article has "slug" property'

    if isinstance(articles_fixture['result'], list):
        assert 'slug' in articles_fixture['result'][0]['article']
    else:
        assert 'slug' in articles_fixture['result']['article']

def test_response_contains_body(articles_fixture):
    'Article has "body" property'

    if isinstance(articles_fixture['result'], list):
        assert 'body' in articles_fixture['result'][0]['article']
    else:
        assert 'body' in articles_fixture['result']['article']

def test_response_contains_createdAt(articles_fixture):
    'Article has "createdAt" property'

    if isinstance(articles_fixture['result'], list):
        assert 'createdAt' in articles_fixture['result'][0]['article']
    else:
        assert 'createdAt' in articles_fixture['result']['article']

# def test_response_createdAt_ISO8601_timestamp(articles_slug_fixture):
#     article = json.loads(articles_slug_fixture['res'].body)
#     date = arrow.get(article['article']['createdAt'])
#     assert date.isoformat() == article['article']['createdAt']

# def test_response_updatedAt_ISO8601_timestamp(articles_slug_fixture):
#     article = json.loads(articles_slug_fixture['res'].body)
#     date = arrow.get(article['article']['updatedAt'])
#     assert date.isoformat() == article['article']['updatedAt']

def test_response_contains_description(articles_fixture):
    'Article has "description" property'

    if isinstance(articles_fixture['result'], list):
        assert 'description' in articles_fixture['result'][0]['article']
    else:
        assert 'description' in articles_fixture['result']['article']

def test_response_contains_tagList(articles_fixture):
    'Article has "tagList" property'

    if isinstance(articles_fixture['result'], list):
        assert 'tagList' in articles_fixture['result'][0]['article']
    else:
        assert 'tagList' in articles_fixture['result']['article']

def test_response_tagList_is_list(articles_fixture):
    'Article\'s "tagList" property is an Array'

    if isinstance(articles_fixture['result'], list):
        assert isinstance(articles_fixture['result'][0]['article']['tagList'], list)
    else:
        assert isinstance(articles_fixture['result']['article']['tagList'], list)

def test_response_contains_author(articles_fixture):
    'Article has "author" property'

    if isinstance(articles_fixture['result'], list):
        assert 'author' in articles_fixture['result'][0]['article']
    else:
        assert 'author' in articles_fixture['result']['article']

def test_response_contains_favorited(articles_fixture):
    'Article has "favorited" property'

    if isinstance(articles_fixture['result'], list):
        assert 'favorited' in articles_fixture['result'][0]['article']
    else:
        assert 'favorited' in articles_fixture['result']['article']

def test_response_contains_favoritesCount(articles_fixture):
    'Article has "favoritesCount" property'

    if isinstance(articles_fixture['result'], list):
        assert 'favoritesCount' in articles_fixture['result'][0]['article']
    else:
        assert 'favoritesCount' in articles_fixture['result']['article']

def test_response_favoritesCount_is_integer(articles_fixture):
    'favoritesCount is an integer'

    if isinstance(articles_fixture['result'], list):
        assert isinstance(articles_fixture['result'][0]['article']['favoritesCount'], int)
    else:
        assert isinstance(articles_fixture['result']['article']['favoritesCount'], int)

