from flask import Flask, Response, request, jsonify
from flask_cors import CORS
# import json
# import logging
# import os

from smartystreets_python_sdk import StaticCredentials, exceptions, ClientBuilder
from smartystreets_python_sdk.us_street import Lookup as StreetLookup

application = Flask(__name__)
CORS(application)


@application.route("/")
def index():
    return "The Flask App for address validation Works!"

@application.route('/validate',methods = ['GET'])
def validate_address():
    auth_id = "5ffa745e-afd7-2c66-d086-00dd4add89a6"
    auth_token = "cUMNDx1dUBa70X0I46bQ"
    json_data = request.json

    # We recommend storing your secret keys in environment variables instead---it's safer!
    # auth_id = os.environ['SMARTY_AUTH_ID']
    # auth_token = os.environ['SMARTY_AUTH_TOKEN']

    credentials = StaticCredentials(auth_id, auth_token)

    # The appropriate license values to be used for you subscriptions
    # can be found on the Subscriptions page of the account dashboard.
    # https://www.smartystreets.com/docs/cloud/licensing
    client = ClientBuilder(credentials).with_licenses(["us-core-cloud"]).build_us_street_api_client()
    # client = ClientBuilder(credentials).with_custom_header({'User-Agent': 'smartystreets (python@0.0.0)', 'Content-Type': 'application/json'}).build_us_street_api_client()
    # client = ClientBuilder(credentials).with_proxy('localhost:8080', 'user', 'password').build_us_street_api_client()
    # Uncomment the line above to try it with a proxy instead

    # Documentation for input fields can be found at:
    # https://smartystreets.com/docs/us-street-api#input-fields

    lookup = StreetLookup()
    # lookup.input_id = "24601"  # Optional ID from your system
    # lookup.addressee = "John Doe"
    lookup.street = json_data["street"]
    lookup.street2 = json_data["street2"]
    # lookup.secondary = json_data["secondary"]
    # lookup.street2 = "closet under the stairs"
    # lookup.secondary = "APT 2"
    # lookup.urbanization = ""  # Only applies to Puerto Rico addresses
    lookup.city = json_data["city"]
    lookup.state = json_data["state"]
    lookup.zipcode = json_data["zipcode"]
    lookup.candidates = 3
    # lookup.match = "invalid"  # "invalid" is the most permissive match,
    # this will always return at least one result even if the address is invalid.
    # Refer to the documentation for additional Match Strategy options.

    try:
        client.send_lookup(lookup)
    except exceptions.SmartyException as err:
        print(err)
        return err

    result = lookup.result

    if not result:
        return "No candidates. This means the address is not valid."

    # first_candidate = result[0]
    # print("Address is valid. (There is at least one candidate)\n")
    # print("ZIP Code: " + first_candidate.components.zipcode)
    # print("County: " + first_candidate.metadata.county_name)
    # print("Latitude: {}".format(first_candidate.metadata.latitude))
    # print("Longitude: {}".format(first_candidate.metadata.longitude))
    # print("Precision: {}".format(first_candidate.metadata.precision))
    # print("Residential: {}".format(first_candidate.metadata.rdi))
    # print("Vacant: {}".format(first_candidate.analysis.dpv_vacant))
    return "Address is valid."


    # Complete list of output fields is available here:  https://smartystreets.com/docs/cloud/us-street-api#http-response-output

if __name__ == '__main__':
    application.run(host="0.0.0.0", port=5000)

