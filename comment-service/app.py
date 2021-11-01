from datetime import datetime
from flask import Flask, Response,request, jsonify
from flask_cors import CORS
import json
import logging
from datetime import datetime

from Comment_Application.CommentService import CommentService as CommentService
from RDB_Application.RDBService import RDBService as RDBService
from middleware.notification import notify

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Flask(__name__)
CORS(app)

@app.before_request
def before_request_func():
    print("here is the before request!")

@app.after_request
def after_request_func(response):
    notify(request)

@app.route('/')
def hello_world():
    return '<u>Hello World!</u>'


@app.route('/discover/<username>/<news_id>',methods = ['GET'])
def get_comment(username, news_id):
    offset = request.args.get('offset', 0, type=int)
    limit = request.args.get('limit', 0, type=int)
    user_comment = request.args.get('username', "", type=str)

    args = request.args
    if args:
        for k in args:
            if k != "offset" and k != "limit" and k !="user_comment":
                return Response(json.dumps("The request fields are not available"), status=404, content_type="application/json")

    comment_res = CommentService.get_comment_by_id(news_id, offset, limit, user_comment)
    if not comment_res:
        return Response(json.dumps("The request fields are not available"), status=404, content_type="application/json")
    elif comment_res == "connection failed":
        return Response(json.dumps("Database connection failed"), status=500, content_type="application/json")

    news_res = CommentService.get_news_by_id(news_id)
    if not news_res:
        return Response(json.dumps("The request fields are not available"), status=404, content_type="application/json")
    elif news_res == "connection failed":
        return Response(json.dumps("Database connection failed"), status=500, content_type="application/json")
        
    return_res = {'username': username, 'news': { 'news_id': news_id, 'content_full': news_res[0]['full_content'], 'comments':[] }, 
                'links':[ {'rel': 'self', 'href': '/discover/' + username + news_id }, {'rel': 'user', 'href': '/api/v1/users/' + username} ] }
    for i in range(len(comment_res)):
        dict = {'username': comment_res[i]['username'], 'comment_info': comment_res[i]['comment_info'], 'timestamp': str(comment_res[i]['timestamp'])}
        return_res['news']['comments'].append(dict)

    rsp = Response(json.dumps(return_res), status=200, content_type="application/json")
    return rsp

@app.route('/discover/post',methods = ['POST'])
def create_comment():
    comment_data = request.get_json()
    times = datetime.now()
    timestamp = times.strftime("%Y-%m-%d %H:%M:%S")
    comment_data['timestamp'] = timestamp

    if not check_valid(comment_data):
        return Response(json.dumps("Bad Data"), status=400, content_type="application/json") 
    
    res = RDBService.create("Comments", "comment", comment_data)
    if res == "connection failed":
        return Response(json.dumps("Database connection failed"), status=500, content_type="application/json")

    offset = request.args.get('offset', 0, type=int)
    limit = request.args.get('limit', 0, type=int)
    user_comment = request.args.get('username', "", type=str)

    args = request.args
    if args:
        for k in args:
            if k != "offset" and k != "limit" and k !="user_comment":
                return Response(json.dumps("The request fields are not available"), status=404, content_type="application/json")
    
    comment_res = CommentService.get_comment_by_id(str(comment_data['news_id']), offset, limit, user_comment)
    if not comment_res:
        return Response(json.dumps("The request fields are not available"), status=404, content_type="application/json")
    elif comment_res == "connection failed":
        return Response(json.dumps("Database connection failed"), status=500, content_type="application/json")

    news_res = CommentService.get_news_by_id(str(comment_data['news_id']))
    if not news_res:
        return Response(json.dumps("The request fields are not available"), status=404, content_type="application/json")
    elif news_res == "connection failed":
        return Response(json.dumps("Database connection failed"), status=500, content_type="application/json")

    return_res = {'username': comment_data['username'],
                  'news': {'news_id': comment_data['news_id'], 'content_full': news_res[0]['full_content'], 'comments': []}}
    for i in range(len(comment_res)):
        dict = {'username': comment_res[i]['username'], 'comment_info': comment_res[i]['comment_info'], 'timestamp': str(comment_res[i]['timestamp'])}
        return_res['news']['comments'].append(dict)
    print(return_res)
    rsp = Response(json.dumps(return_res), status=201, content_type="application/json")
    return rsp

@app.route('/discover/delete',methods = ['DELETE'])
def delete_comment():
    comment_data = request.get_json()
    if not check_valid(comment_data):
        return Response(json.dumps("Bad Data"), status=400, content_type="application/json") 
    res = RDBService.delete("Comments", "comment", comment_data)
    if res == "connection failed":
        return Response(json.dumps("Database connection failed"), status=500, content_type="application/json")
    rsp = Response(json.dumps("delete successfully"), status=204, content_type="application/json")
    return rsp

def check_valid(data):
    key_list = ['news_id', 'username', 'comment_info', 'timestamp']
    for keys in key_list:
        if keys not in data.keys():
            return False
        elif keys == 'news_id':
            if type(data[keys]) != int:
                return False 
        elif keys == 'timestamp':
            format = "%Y-%m-%d %H:%M:%S"
            try:
                print("here")
                return bool(datetime.strptime(data['timestamp'], format))
            except ValueError:
                return False
    return True

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
