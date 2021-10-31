from flask import jsonify


def bad_request(err_message):
    response = jsonify({'error': 'bad request', 'message': err_message})
    response.status_code = 400
    return response


def resource_not_found(err_message):
    response = jsonify({'error': '404 not found', 'message': err_message})
    response.status_code = 404
    return response


def internal_error(err_message):
    response = jsonify({'error': 'server internal error', 'message': err_message})
    response.status_code = 500
    return response


# should not return to normal users
def database_error(err_message):
    response = jsonify({'error': 'database integrity error', 'message': err_message})
    response.status_code = 422
    return response
