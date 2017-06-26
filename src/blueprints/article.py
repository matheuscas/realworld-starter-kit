from sanic.response import json
from sanic import Blueprint

bp_article = Blueprint('article')

@bp_article.route("/articles/<slug>")
async def get_article_by_slug(request, slug):
    mongo_articles = await request.app.config['db'].articles.find({'article.slug': slug}).to_list(None)
    article = {'article': mongo_articles[0]['article']}
    return json(article)

@bp_article.route("/articles")
async def get_articles(request):
    mongo_articles = await request.app.config['db'].articles.find().to_list(None)
    articles = list(map(lambda a: {'article': a['article']}, mongo_articles))
    return json(articles)
