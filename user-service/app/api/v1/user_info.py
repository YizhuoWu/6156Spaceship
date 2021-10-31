from ...models import User
from app.api.v1 import api
from app import db
from .utils import *
from .decorators import *
from .error import *
from sqlalchemy.exc import IntegrityError


@api.route('/users/<string:username>')
def get_user_profile_by_username(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        return resource_not_found('no user has username %s' % username)
    return jsonify(user.to_json())


@api.route('/users/<string:email>', methods=['PUT'])
@valid_args(['state', 'city', 'address', 'username', 'email'])
def set_user_profile_by_email(email):
    if not valid_email(email):
        return bad_request('invalid email format')

    user = User.query.get(email)
    existed = True
    if user is None:
        existed = False
        user = User(email=email)

    _update_user_attributes(user, request.args, ['address', 'username', 'email', 'state', 'city'])

    try:
        if not existed:
            db.session.add(user)
        db.session.commit()
    except IntegrityError as e:
        return database_error(e.__str__())

    response = jsonify(user.to_json())
    response.status_code = 201
    return response


def _update_user_attributes(user, args, attr_list):
    for attr in attr_list:
        if request.args.get(attr) is not None and request.args.get(attr) != '':
            setattr(user, attr, args.get(attr))


@api.route('/users/<string:email>', methods=['DELETE'])
def delete_user_by_email(email):
    user = User.query.get(email)
    if user is None:
        return resource_not_found('no user has email %s' % email)
    response = jsonify({'result': 'ok'})
    response.status_code = 204
    return response


@api.route('/users')
@valid_args(['state', 'city', 'username', 'email', 'offset', 'limit'])
def get_all_user_info():
    user_query = User.query
    user_query = filter(request, user_query)
    user_query = pagination(request, user_query)
    return jsonify([u.to_json() for u in user_query.all()])


