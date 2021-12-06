import json

secure_paths = [
    "/",
    "/login/google",
    "/login/google/authorized"
]


def check_security(request, google, blueprint):
    path = request.path
    result = False

    if path not in secure_paths:
        google_data = None

        user_info_endpoint = '/oauth2/v2/userinfo'

        if google.authorized:
            google_data = google.get(user_info_endpoint).json()

            print(json.dumps(google_data, indent=2))

            session = blueprint.session
            token = session.token
            print("Token = \n", json.dumps(token, indent=2))

            result = True
    else:
        result = True
    return result
