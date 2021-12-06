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