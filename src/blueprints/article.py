from sanic.response import json
from sanic import Blueprint
from sanic.exceptions import ServerError
from bson.objectid import ObjectId

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
    return json({'articles': articles, 'articlesCount': len(articles)})

@bp_article.route("/articles/<slug>/comments")
async def get_article_comments(request, slug):
    mongo_articles = await request.app.config['db'].articles.find(
        {'article.slug': slug}
    ).to_list(None)
    if len(mongo_articles) > 0:
        _id = mongo_articles[0]['_id']
        mongo_comments = await request.app.config['db'].comments.find(
            {'comment.article_id': ObjectId(_id)}
        ).to_list(None)
        if len(mongo_comments) > 0:
            comments = []
            for comment in mongo_comments:
                new_comment = {'comment': comment['comment']}
                new_comment['comment']['article_id'] = str(new_comment['comment']['article_id'])
                comments.append(new_comment)
            return json({'comments': comments})
        return json([])
    else:
        raise ServerError("Article not found", status_code=404)
