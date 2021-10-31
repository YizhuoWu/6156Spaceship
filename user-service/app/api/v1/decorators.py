from flask import request
from functools import wraps
from .error import bad_request


def valid_args(valid_args_list):
    def decorator(f):
        @wraps(f)
        def decorated_func(*args, **kwargs):
            for arg in request.args:
                if arg not in valid_args_list:
                    return bad_request('invalid args')
            return f(*args, **kwargs)
        return decorated_func
    return decorator

