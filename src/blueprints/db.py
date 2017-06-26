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
    app.config.db.articles.insert(articles)
