from flask import Flask, Response,request, jsonify
from flask_cors import CORS
import json
import logging

# from application_services.imdb_artists_resource import IMDBArtistResource
# from application_services.UsersResource.user_service import UserResource
from Comment_Application.RDBService import RDBService as RDBService

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return '<u>Hello World!</u>'


@app.route('/discover/<username>/<news_id>',methods = ['GET'])
def get_comment(username, news_id):
    res = RDBService.get_by_name_id(username, news_id)
    print(res)
    return_res = {'username': username, 'news': { 'news_id': news_id, 'content_full': res[len(res) - 1]['full_content'], 'comments':[] } }
    for i in range(len(res)-1):
        dict = {'username': res[i]['username'], 'comment_info': res[i]['comment_info']}
        return_res['news']['comments'].append(dict)
    print(return_res)
    rsp = Response(json.dumps(return_res), status=200, content_type="application/json")
    return rsp

@app.route('/discover/post',methods = ['POST'])
def create_comment():
    comment_data = request.get_json()
    print(comment_data)
    res = RDBService.create("Comments", "comment", comment_data)
    rsp = Response(json.dumps(res), status=200, content_type="application/json")
    return rsp

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
