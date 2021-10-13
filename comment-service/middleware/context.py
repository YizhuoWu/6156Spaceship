
import os

# This is a bad place for this import
import pymysql

def get_db_info(dbname):
    """
    This is crappy code.

    :return: A dictionary with connect info for MySQL
    """
    # db_host = os.environ.get("DBHOST", None)
    # db_user = os.environ.get("DBUSER", None)
    # db_password = os.environ.get("DBPASSWORD", None)

    if dbname == "news":
        db_info = {
            "host": "dbs-6156-demoflask.cqpd5huf91dk.us-east-1.rds.amazonaws.com",
            "user": "admin",
            "password": "19981013Anna",
            "cursorclass": pymysql.cursors.DictCursor
        }
    else:
        db_info = {
            "host": "comments-db.czclpd5rbl1a.us-east-1.rds.amazonaws.com",
            "user": "admin",
            "password": "Fall6156!",
            "cursorclass": pymysql.cursors.DictCursor
        }

    return db_info
