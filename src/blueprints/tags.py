from sanic.response import json
from sanic import Blueprint

bp_tags = Blueprint('tags')

@bp_tags.route('/tags')
async def tags(request):
    mongo_tags = await request.app.config['db'].tags.find().to_list(None)
    tags = list(map(lambda a: a['name'], mongo_tags))
    return json({'tags': tags})
