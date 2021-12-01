from flask import Flask, Response, request, jsonify
from flask_cors import CORS
from Comment_Application.RDBService import RDBService as RDBService
import json
import logging

application = Flask(__name__)
CORS(app)


@application.route("/")
def index():
    return "The Flask App Works!"



@app.route('/discover/<username>',methods = ['POST'])




@app.route('/discover/<username>/<query>',methods = ['GET'])
def get_news(username):
    #query = request.args.get('query', default = "", type = str)
    query = "Columbia"
    res = RDBService.get_by_name_id(username, news_id)
    print(res)
    return_res = {'username': username, 'news': { 'news_id': news_id, 'content_full': res[len(res) - 1]['full_content'], 'comments':[] } }
    for i in range(len(res)-1):
        dict = {'username': res[i]['username'], 'comment_info': res[i]['comment_info']}
        return_res['news']['comments'].append(dict)
    print(return_res)
    rsp = Response(json.dumps(return_res), status=200, content_type="application/json")
    return rsp

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

