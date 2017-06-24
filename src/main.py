import asyncio
import uvloop
import db
from sanic import Sanic
from sanic.response import text, json

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

app = Sanic(__name__)
app.register_blueprint(db.bp_db)

@app.route("/")
async def test(request):
    return text('It is up and running')

@app.route("/articles")
async def get_articles(request):
    articles = await app.config.db.articles.find().to_list(None)
    return json(articles)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)


