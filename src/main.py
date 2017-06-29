import asyncio
import uvloop
from sanic import Sanic
from sanic.response import text
from blueprints import db, article, tags, profiles

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

app = Sanic(__name__)
app.register_blueprint(db.bp_db)
app.register_blueprint(article.bp_article)
app.register_blueprint(tags.bp_tags)
app.register_blueprint(profiles.bp_profiles)

@app.route("/")
async def test(request):
    return text('It is up and running')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)


