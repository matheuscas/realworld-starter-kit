from sanic.response import json
from sanic import Blueprint
from motor.motor_asyncio import AsyncIOMotorClient

bp_db = Blueprint('db')

@bp_db.listener('before_server_start')
async def register_db(app, loop):
    mongo_client = AsyncIOMotorClient('localhost', 27017)
    app.config.db = mongo_client['real_world']
    app.config.mongo = mongo_client
    await populateArticles(app)
    await populateTags(app)
    await populateProfiles(app)

@bp_db.listener('after_server_stop')
async def close_db(app, loop):
    app.config.mongo.close()

async def populateArticles(app):
    articles = [
        {
            "article": {
                "slug": "how-to-train-your-dragon",
                "title": "How to train your dragon",
                "description": "Ever wonder how?",
                "body": "It takes a Jacobian",
                "tagList": ["dragons", "training"],
                "createdAt": "2016-02-18T03:22:56.637Z",
                "updatedAt": "2016-02-18T03:48:35.824Z",
                "favorited": False,
                "favoritesCount": 0,
                "author": {
                    "username": "jake",
                    "bio": "I work at statefarm",
                    "image": "https://i.stack.imgur.com/xHWG8.jpg",
                    "following": False
                }
            }
        },
        {
            "article": {
                "slug": "how-to-train-your-dragon-2",
                "title": "How to train your dragon 2",
                "description": "So toothless",
                "body": "It a dragon",
                "tagList": ["dragons", "training"],
                "createdAt": "2016-02-18T03:22:56.637Z",
                "updatedAt": "2016-02-18T03:48:35.824Z",
                "favorited": False,
                "favoritesCount": 0,
                "author": {
                    "username": "jake",
                    "bio": "I work at statefarm",
                    "image": "https://i.stack.imgur.com/xHWG8.jpg",
                    "following": False
                }
            }
        }
    ]
    await app.config.db.articles.drop()
    first_article = await app.config.db.articles.insert_one(articles[0])
    await populateComments(app, first_article.inserted_id)
    await app.config.db.articles.insert_one(articles[1])


async def populateTags(app):
    tags = [
        {'name': "reactjs"},
        {'name': "angularjs"}
    ]
    await app.config.db.tags.drop()
    app.config.db.tags.insert(tags)

async def populateProfiles(app):
    profile = {
        'profile': {
            "username": "jake",
            "bio": "I work at statefarm",
            "image": "https://static.productionready.io/images/smiley-cyrus.jpg",
            "following": False
        }
    }
    await app.config.db.profiles.drop()
    app.config.db.profiles.insert(profile)

async def populateComments(app, article_id):
    comment = {
        "comment": {
            "id": 1,
            "createdAt": "2016-02-18T03:22:56.637Z",
            "updatedAt": "2016-02-18T03:22:56.637Z",
            "body": "It takes a Jacobian",
            "author": {
                "username": "jake",
                "bio": "I work at statefarm",
                "image": "https://i.stack.imgur.com/xHWG8.jpg",
                "following": False
            },
            "article_id": article_id
        }
    }
    await app.config.db.comments.drop()
    app.config.db.comments.insert(comment)
