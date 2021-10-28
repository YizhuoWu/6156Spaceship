from flask import request, Flask, jsonify
import os
application = Flask(__name__)

@application.route("/")
def index():
    return "The Flask App Works!"

@application.route('/discover/:username/',methods = ['POST'])
def test():
    return "This is /discover/:username/"

@application.route('/discover/post',methods = ['POST'])
def test_1():
    #s = request.form
    return "This is /discover/post"

@application.route("/discover/:username/:newsid",methods = ['GET'])
def test_2():
    return "test"

if __name__ == '__main__':
    # app.run(debug=True, host='127.0.0.1')
    application.run(port=5000, debug=True)

