import re
from .error import bad_request


def pagination(req, query):
    _offset = req.args.get('offset', 0, type=int)
    _limit = req.args.get('limit', 0, type=int)
    query = query.offset(_offset)
    if _limit > 0:
        query = query.limit(_limit)
    return query


def filter(req, query):
    username_filter = req.args.get('username', '', type=str)
    email_filter = req.args.get('email', '', type=str)
    state_filter = req.args.get('state', '', type=str)
    print(state_filter)
    city_filter = req.args.get('city', '', type=str)
    if username_filter != '':
        query = query.filter_by(username=username_filter)
    if email_filter != '':
        query = query.filter_by(email=email_filter)
    if state_filter != '':
        query = query.filter_by(state=state_filter)
    if city_filter != '':
        query = query.filter_by(city=city_filter)
    return query


def valid_email(email):
    if re.match(r'(.+)@(.+).(.+)', email) is None:
        return False
    return True
