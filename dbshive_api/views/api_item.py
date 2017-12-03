from flask import make_response, jsonify, request
from dbshive_api import app, db
from dbshive_api.models.user import User
from dbshive_api.models.item import Item
import json

endpoint = '/items'


@app.route('%s' % endpoint, methods=['GET'])
def get_item():
    items = Item.query.all()

    results = []
    for item in items:
        results.append(item.to_json())

    return make_response(jsonify(results))


@app.route('%s' % endpoint, methods=['POST'])
def post_item():
    data = json.loads(request.data.decode('utf-8'))

    new_item = Item(
        name=data.get('name'),
        description=data.get('description'),
    )

    user_list = data.get('developers')
    users = User.query.filter(User.id.in_(user_list)).all()
    for user in users:
        new_item.developer.append(user)

    db.session.add(new_item)
    db.session.commit()

    items = Item.query.all()
    results = []
    for item in items:
        results.append(item.to_json())
    return make_response(jsonify(results))
