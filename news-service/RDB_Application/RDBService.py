import pymysql
import json
import logging

from . import context

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)


class RDBService:

    def __init__(self):
        pass

    @classmethod
    def get_db_connection(cls, dbname):

        db_info = context.get_db_info(dbname)
        print("db_info: ",db_info)
        try:
            db_connection = pymysql.connect(**db_info, autocommit=True)
        except pymysql.Error as error:
            db_connection = False
        return db_connection

    @classmethod
    def run_sql(cls, dbname, sql_statement, args, fetch=False):

        conn = RDBService.get_db_connection(dbname)

        if not conn:
            return "connection failed"

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

    @classmethod
    def delete(cls, db_schema, table_name, delete_data):
        # cols = []
        # vals = []
        # args = []
        conditions = ""
        for k,v in delete_data.items():
            # cols.append(k)
            # vals.append('%s')
            # args.append(v)
            if type(v) == str:
                add_v = "'" + v + "'"
            else:
                add_v = v
            conditions = conditions + k + " = " + str(add_v) + ' and '

        conditions = conditions[:len(conditions)-5]

        sql_stmt = "delete from " + db_schema + "." + table_name + " where " + conditions

        print(sql_stmt)
        res = RDBService.run_sql("comments",sql_stmt, None)
        return res