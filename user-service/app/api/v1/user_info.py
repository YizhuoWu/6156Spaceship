import asyncio
from concurrent.futures.thread import ThreadPoolExecutor

from ...models import User
from app.api.v1 import api
from app import db
from .utils import *
from .decorators import *
from .error import *
from sqlalchemy.exc import IntegrityError
from .net import validate_address
import requests

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


@api.route('/users/<string:username>')
def get_user_profile_by_username(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        return resource_not_found('no user has username %s' % username)
    return jsonify(user.to_json())


async def _check_username_unique_async(username):
    return bool(db.session.query(User.username).filter_by(username=username).first())


async def _check_email_unique_async(email):
    return bool(db.session.query(User.username).filter_by(email=email).first())


def _check_username_unique_sync(username):
    return bool(db.session.query(User.username).filter_by(username=username).first())


@api.route('/users/<string:username>', methods=['POST'])
def set_user_profile_by_username(username):
    body = request.get_json()
    if not allowed_post_body(body, ['email', 'address', 'username', 'state', 'city', 'street', 'street2', 'zipcode']):
        return bad_request('invalid request body')

    method = request.args.get('create')
    if method is None:
        method = 'update'
    else:
        method = 'create'

    email = body.get('email')
    if method == 'create' and email is None:
        return bad_request('must specify the email address')
    if email is not None and _check_email_unique_async(email):
        return bad_request('this email address has been registered')

    if method == 'update':
        if email is not None:
            return bad_request("email is read-only")
        user = User.query.filter_by(username=username).first()
        new_username = body.get('username')
        if new_username is not None and _check_username_unique_async(username):
            return bad_request('username is already used')

        new_address = body.get('username')
        new_street = body.get('street')
        new_street2 = body.get('street2')
        new_state = body.get('state')
        new_city = body.get('city')

        if new_address is not None or new_state is not None or new_city is not None \
                or new_street is not None or new_street2 is not None:
            if not validate_address(
                    body.get('street'), body.get('street2'), body.get('city'), body.get('state'), body.get('zipcode')):
                return bad_request('invalid address')

        _update_user_attributes(user, body, ['address', 'username', 'state', 'city', 'street', 'street2'])

    else:
        if not valid_email(email):
            return bad_request('invalid email format')
        user = User(email=email)

        duplicate_task = loop.create_task(_check_username_unique_async(username))
        valid_task = loop.create_task(validate_address(
            body.get('street'), body.get('street2'), body.get('city'), body.get('state'), body.get('zipcode')))
        dup, valid = loop.run_until_complete(asyncio.gather(duplicate_task, valid_task))
        if dup:
            return bad_request("the username has been used")
        if not valid:
            return bad_request("the address is invalid")

        _update_user_attributes(user, body, ['address', 'username', 'state', 'city', 'street', 'street2'])
        db.session.add(user)

    # synchronous way
    # dup = _check_username_unique_sync(username)
    # if dup:
    #     return bad_request("the username has been used")
    #
    # valid = requests.get('http://addrvalidationservice-env.eba-jtfahpj7.us-east-1.elasticbeanstalk.com/validate?',
    #                      json=body)
    #
    # if valid.text.__contains__("invalid"):
    #     return bad_request("the address is invalid")

    db.session.commit()
    response = jsonify(user.to_json())
    response.status_code = 201
    return response


def _update_user_attributes(user, body, attr_list):
    for attr in attr_list:
        if body.get(attr) is not None:
            setattr(user, attr, body.get(attr))


@api.route('/users/<string:username>', methods=['DELETE'])
def delete_user_by_username(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        return resource_not_found('no user has username %s' % username)

    db.session.delete(user)
    db.session.commit()

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
