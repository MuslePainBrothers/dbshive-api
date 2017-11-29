from flask import make_response, jsonify
from flaskr import app
from flaskr.models.user import User

endpoint = '/users'


@app.route('%s' % endpoint, methods=['GET'])
def get_entrys():
    users = User.query.all()

    results = []
    for user in users:
        results.append(user.to_json())

    return make_response(jsonify(results))
