from sanic.response import json
from sanic import Blueprint
from sanic.exceptions import ServerError

bp_profiles = Blueprint('profiles')

@bp_profiles.route('/profiles/<username>', methods=["GET"])
async def profile(request, username):
    mongo_profile = await request.app.config['db'].profiles.find({'profile.username': username}).to_list(None)
    if (len(mongo_profile) == 0):
        raise ServerError("There is no profile with username like {}".format(username) , status_code=404)
    return json({'profile': mongo_profile[0]['profile']})

@bp_profiles.route('/profiles/<username>/follow', methods=["POST", "DELETE"])
async def follow_profile(request, username):

    try:
        follow = True if request.method == 'POST' else False
        await request.app.config['db'].profiles.update_one(
            {'profile.username': username},
            {'$set': {"profile.following":follow}}
        )
        mongo_profile = await request.app.config['db'].profiles.find({'profile.username': username}).to_list(None)
        return json({'profile': mongo_profile[0]['profile']})
    except Exception as e:
        print(e)
        raise ServerError("There is no profile with username like {}".format(username) , status_code=404)
 