from flask import make_response, jsonify
from flaskr import app
from flaskr.models.item import Item

endpoint = '/items'


@app.route('%s' % endpoint, methods=['GET'])
def get_entrys():
    items = Item.query.all()

    results = []
    for item in items:
        results.append(item.to_json())

    return make_response(jsonify(results))
