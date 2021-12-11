from datetime import datetime
from flask import Flask, Response,request, jsonify, url_for
from flask_cors import CORS
import json
import logging
from datetime import datetime

from werkzeug.utils import redirect

from Comment_Application.CommentService import CommentService as CommentService
from RDB_Application.RDBService import RDBService as RDBService
from middleware.notification import notify
from security import check_security

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Flask(__name__)
CORS(app)

# @app.before_request
# def before_request_func():
#     if not check_security(request):
#         return redirect(url_for("google.login"))

@app.after_request
def after_request_func(response):
    notify(request)
    return response

@app.route('/')
def hello_world():
    return '<u>Hello World!</u>'


@app.route('/discover/<news_id>',methods = ['GET'])
def get_comment(username, news_id):
    offset = request.args.get('offset', 0, type=int)
    limit = request.args.get('limit', 0, type=int)
    user_comment = request.args.get('username', "", type=str)

    args = request.args
    if args:
        for k in args:
            if k != "offset" and k != "limit" and k != "username":
                return Response(json.dumps("The request fields are not available"), status=404, content_type="application/json")

    comment_res = CommentService.get_comment_by_id(news_id, offset, limit, user_comment)
    if not comment_res:
        return Response(json.dumps("The request fields are not available"), status=404, content_type="application/json")
    elif comment_res == "connection failed":
        return Response(json.dumps("Database connection failed"), status=500, content_type="application/json")
        
    return_res = {'news': news_id, 
                  'comments':[], 
                'links':[ {'rel': 'self', 'href': '/discover/' + username + "/" + news_id }, {'rel': 'user', 'href': '/api/v1/users/' + username} ] }
    for i in range(len(comment_res)):
        dict = {'username': comment_res[i]['username'], 'comment_info': comment_res[i]['comment_info'], 'timestamp': str(comment_res[i]['timestamp'])}
        return_res['comments'].append(dict)

    res = {'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',
                },
                'body': json.dumps(return_res),
                'isBase64Encoded': False         
    }

    rsp = Response(json.dumps(res), status=200, content_type="application/json")
    return rsp

@app.route('/discover/post',methods = ['POST'])
def create_comment():
    comment_data = request.get_json()
    if 'timestamp' in comment_data.keys():
        return Response(json.dumps("Bad Data"), status=400, content_type="application/json")
    times = datetime.now()
    timestamp = times.strftime("%Y-%m-%d %H:%M:%S")
    comment_data['timestamp'] = timestamp

    (bool, error_message) = check_valid(comment_data)
    if not bool:
        return Response(json.dumps("Bad Data: " + error_message), status=400, content_type="application/json") 
    
    res = RDBService.create("Comments", "comment", comment_data)
    if res == "connection failed":
        return Response(json.dumps("Database connection failed"), status=500, content_type="application/json")

    offset = request.args.get('offset', 0, type=int)
    limit = request.args.get('limit', 0, type=int)
    user_comment = request.args.get('username', "", type=str)

    args = request.args
    if args:
        for k in args:
            if k != "offset" and k != "limit" and k !="username":
                return Response(json.dumps("The request fields are not available"), status=404, content_type="application/json")
    
    comment_res = CommentService.get_comment_by_id(str(comment_data['news_id']), offset, limit, user_comment)
    if not comment_res:
        return Response(json.dumps("The request fields are not available"), status=404, content_type="application/json")
    elif comment_res == "connection failed":
        return Response(json.dumps("Database connection failed"), status=500, content_type="application/json")

    return_res = {'username': comment_data['username'],
                  'news': comment_data['news_id'], 
                  'comments': [], 
                  'links':[ {'rel': 'self', 'href': '/discover/post'}, 
                            {'rel': 'user', 'href': '/api/v1/users/' + comment_data['username']},
                            {'rel': 'news', 'href': '/discover/' + str(comment_data['news_id'])} ]}
    for i in range(len(comment_res)):
        dict = {'username': comment_res[i]['username'], 'comment_info': comment_res[i]['comment_info'], 'timestamp': str(comment_res[i]['timestamp'])}
        return_res['comments'].append(dict)

    rsp = Response(json.dumps(return_res), status=201, content_type="application/json")
    return rsp

@app.route('/discover/delete',methods = ['DELETE'])
def delete_comment():
    comment_data = request.get_json()
    (bool, error_message) = check_valid(comment_data)
    if not bool:
        return Response(json.dumps("Bad Data: " + error_message), status=400, content_type="application/json")  
    res = RDBService.delete("Comments", "comment", comment_data)
    if res == "connection failed":
        return Response(json.dumps("Database connection failed"), status=500, content_type="application/json")
    rsp = Response(json.dumps("delete successfully"), status=204, content_type="application/json")
    return rsp

def check_valid(data):
    key_list = ['news_id', 'username', 'comment_info', 'timestamp']
    for keys in key_list:
        if keys not in data.keys():
            return False, "Inputs format needs to have" + keys
        elif keys == 'news_id':
            if type(data[keys]) != int:
                return False, "news_id should be an integer" 
        elif keys == 'timestamp':
            format = "%Y-%m-%d %H:%M:%S"
            try:
                bool(datetime.strptime(data['timestamp'], format))
            except ValueError:
                return False, "datetime format is not correct"
    return True, "everything is ok"

if __name__ == '__main__':
    app.run()
