import asyncio
import uvloop
from . import db
from . import article
from sanic import Sanic
from sanic.response import text

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

app = Sanic(__name__)
app.register_blueprint(db.bp_db)
app.register_blueprint(article.bp_article)

@app.route("/")
async def test(request):
    return text('It is up and running')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)


