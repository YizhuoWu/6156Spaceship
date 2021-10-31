from RDB_Application.RDBService import RDBService

class CommentService():

    def __init__(self):
        pass

    @classmethod
    def get_comment_by_id(cls, news_id, offset, limit, user_comment):
        conn_comment = RDBService.get_db_connection("Comments")

        if not conn_comment:
            return "connection failed"

        cur_comment = conn_comment.cursor()

        comment_sql = "select * from Comments.comment where news_id = " + news_id
        
        if user_comment:
            comment_sql = comment_sql + " and username = '" + user_comment + "'"
            print("SQL Statement = " + cur_comment.mogrify(comment_sql, None))

        if limit:
            comment_sql = comment_sql + " limit " + str(limit)
        
        if offset:
            comment_sql = comment_sql + " offset " + str(offset)

        

        res_comment = cur_comment.execute(comment_sql)
        res_comment = cur_comment.fetchall()

        conn_comment.close()

        return res_comment

    @classmethod
    def get_news_by_id(cls, news_id):
        conn_news = RDBService.get_db_connection("news")

        if not conn_news:
            return "connection failed"

        cur_news = conn_news.cursor()

        news_sql = "select full_content from `db-news-schema`.`news_table` where news_id = " + news_id
        print("SQL Statement = " + cur_news.mogrify(news_sql, None))

        res_news = cur_news.execute(news_sql)
        res_news = cur_news.fetchall()

        conn_news.close()

        return res_news