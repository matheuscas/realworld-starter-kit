from ..sanic_real_world.main import app

def test_get_article_returns_200():
    params = {'slug': 'how-to-train-your-dragon'}
    req, res = app.test_client.get('/articles', params=params)
    assert res.status == 200