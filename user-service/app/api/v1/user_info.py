from ...models import User
from app.api.v1 import api
from flask import jsonify, request
from app import db


@api.route('/users/<string:username>')
def get_user_info(username):
    user = User.query.get(username)
    return jsonify(user.to_json())


@api.route('/users/<string:username>', methods=['PUT'])
def set_user_info(username):
    user = User.query.get(username)
    address = request.args.get('address')
    user.address = address
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_json())
