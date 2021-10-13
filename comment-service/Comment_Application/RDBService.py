import pymysql
import json
import logging

import middleware.context as context

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)


class RDBService:

    def __init__(self):
        pass

    @classmethod
    def get_db_connection(cls, dbname):

        db_info = context.get_db_info(dbname)

        db_connection = pymysql.connect(**db_info, autocommit=True)
        return db_connection

    @classmethod
    def run_sql(cls, dbname, sql_statement, args, fetch=False):

        conn = RDBService.get_db_connection(dbname)

        try:
            cur = conn.cursor()
            res = cur.execute(sql_statement, args=args)
            if fetch:
                res = cur.fetchall()
        except Exception as e:
            conn.close()
            raise e

        return res

    @classmethod
    def get_by_name_id(cls, username, news_id):

        conn_comment = RDBService.get_db_connection("Comments")
        cur_comment = conn_comment.cursor()

        comment_sql = "select * from Comments.comment where news_id = " + news_id
        print("SQL Statement = " + cur_comment.mogrify(comment_sql, None))

        res_comment = cur_comment.execute(comment_sql)
        res_comment = cur_comment.fetchall()

        conn_comment.close()

        # conn_news = RDBService.get_db_connection("Comments")
        # cur_news = conn_news.cursor()
        #
        # news_sql = "select full_content from db-news-schema.news" + " where news_id = " + news_id
        # print("SQL Statement = " + cur_news.mogrify(news_sql, None))
        #
        # res_news = cur_news.execute(news_sql)
        # res_news = cur_news.fetchall()
        #
        # conn_news.close()

        return res_comment

    @classmethod
    def create(cls, db_schema, table_name, create_data):

        cols = []
        vals = []
        args = []

        for k,v in create_data.items():
            cols.append(k)
            vals.append('%s')
            args.append(v)

        cols_clause = "(" + ",".join(cols) + ")"
        vals_clause = "values (" + ",".join(vals) + ")"

        sql_stmt = "insert into " + db_schema + "." + table_name + " " + cols_clause + \
            " " + vals_clause

        print(sql_stmt)
        res = RDBService.run_sql("comments",sql_stmt, args)
        return res