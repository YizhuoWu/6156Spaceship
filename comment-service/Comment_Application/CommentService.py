from RDB_Application.RDBService import RDBService

class CommentService():

    def __init__(self):
        pass

    @classmethod
    def get_comment_by_id(cls, news_id):
        conn_comment = RDBService.get_db_connection("Comments")
        cur_comment = conn_comment.cursor()

        comment_sql = "select * from Comments.comment where news_id = " + news_id
        print("SQL Statement = " + cur_comment.mogrify(comment_sql, None))

        res_comment = cur_comment.execute(comment_sql)
        res_comment = cur_comment.fetchall()

        conn_comment.close()

        return res_comment

    @classmethod
    def get_news_by_id(cls, news_id):
        conn_news = RDBService.get_db_connection("news")
        cur_news = conn_news.cursor()

        news_db_name = "'db-news-schema'"
        news_table_name = "'news-fake'"

        news_sql = "select full_content from `db-news-schema`.`news-fake` where news_id = " + news_id
        print("SQL Statement = " + cur_news.mogrify(news_sql, None))

        res_news = cur_news.execute(news_sql)
        res_news = cur_news.fetchall()

        conn_news.close()

        return res_news