from sanic.response import json
from sanic import Blueprint

bp_article = Blueprint('article')

@bp_article.route("/articles")
async def get_articles(request):
    mongo_articles = await request.app.config['db'].articles.find().to_list(None)
    articles = list(map(lambda a: {'article': a['article']}, mongo_articles))
    return json(articles)
