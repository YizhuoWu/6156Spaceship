from flask import Flask, Response, request, jsonify
from flask_cors import CORS
from RDB_Application.RDBService import RDBService as RDBService
import json
import logging

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return "The Flask App Works!"

'''
Get a list of corresponding news with specific label via querying news RDS
'''
@app.route('/news',methods = ['GET'])
def get_news():
    total_result = 10 # -->TBD
    labels = request.args.get('labels')
    labels = eval(labels)
    news_per_cate = (total_result // len(labels)) + 1 # to evenly get different news by categories
    result = []

    #fetch news from RDS based on labels
    for i in range(len(labels)):
        cur_news_connection = RDBService.get_db_connection("news")
        label = labels[i]
        with cur_news_connection:
            with cur_news_connection.cursor() as cursor:
                query_sql = "select * from `db-news-schema`.`news_table` where category = " + label
                query_sql += "LIMIT "
                query_sql += str(news_per_cate)

                res_news = cursor.execute(query_sql)
                res_news = cursor.fetchall()
                result += res_news

    #make result to return
    json_result = {"totalResults": 10,
                   "news": result
                   }
    rsp = Response(json.dumps(json_result), status=200, content_type="application/json")
    return rsp

'''
Given an specific news id, return the news with detailed information.
Used for extract labels from news.
'''
@app.route('/news/<news_id>',methods = ['GET'])
def get_label(news_id):
    cur_news_connection = RDBService.get_db_connection("news")

    with cur_news_connection:
        with cur_news_connection.cursor() as cursor:
            query_sql = "select * from `db-news-schema`.`news_table` where news_id = " + news_id

            res_news = cursor.execute(query_sql)
            res_news = cursor.fetchall()

            result_dict = {"newsid": news_id,
                           "label": res_news[0]['category'],
                           "title": res_news[0]['title'],
                           "url": res_news[0]['url'],
                           "description": res_news[0]['description']
                           }

            rsp = Response(json.dumps(result_dict), status=200, content_type="application/json")
            return rsp

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
    #app.run(host="0.0.0.0", port=5000)
    app.run()

