from flask import request, Flask, jsonify
import os
app = Flask(__name__)

@app.route('/discover/:username/',methods = ['POST'])
def test():
    return "This is /discover/:username/"

@app.route('/discover/post',methods = ['POST'])
def test_1():
    #s = request.form
    return "This is /discover/post"

@app.route("/discover/:username/:newsid",methods = ['GET'])

def test_2():
    
    return "test"

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
