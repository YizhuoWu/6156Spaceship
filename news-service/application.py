from flask import Flask, Response, request, jsonify
from flask_cors import CORS
from RDB_Application.RDBService import RDBService as RDBService
import json
import random
#import logging

application = Flask(__name__)
CORS(application)


@application.route("/")
def index():
    return "The Flask App Works!"




'''
Get a list of corresponding news with specific label via querying news RDS
'''
@application.route('/news',methods = ['GET'])
def get_news():
    total_result = 10 # -->TBD
    labels = request.args.get('labels')
    l = eval(labels)
    l = eval(l)
    news_per_cate = (total_result // len(l)) + 1 # to evenly get different news by categories
    result = []

    #fetch news from RDS based on labels
    for i in range(len(l)):
        cur_news_connection = RDBService.get_db_connection("news")
        label = l[i]
        #print(1)
        with cur_news_connection:
            with cur_news_connection.cursor() as cursor:
                #print(2)
                query_sql = "select * from `db-news-schema`.`news_table` where `category` = " + "'"+label+"'"
                #query_sql += " LIMIT "
                #query_sql += str(news_per_cate)
                #print(query_sql)

                res_news = cursor.execute(query_sql)
                res_news = cursor.fetchall()

                #generate random index of news of current_labels
                random_result_index = []
                random_result = []
                total_result = len(res_news)
                cnt = 0
                while cnt < news_per_cate:
                    random_index = random.randint(0, total_result)
                    if random_index not in random_result_index:
                        random_result_index.append(random_index)
                        cnt += 1
                random_result = [res_news[i] for i in random_result_index]
                result += random_result

    #make result to return
    json_result = {"totalResults": len(result),
                   "news": result
                   }
    rsp = Response(json.dumps(json_result), status=200, content_type="application/json")
    return rsp

'''
Given an specific news id, return the news with detailed information.
Used for extract labels from news.
'''
@application.route('/news/<news_id>',methods = ['GET'])
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



if __name__ == '__main__':
    #app.run(host="0.0.0.0", port=5000)
    application.run()

