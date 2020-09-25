import os
import MySQLdb
from colorama import Fore


def get_connection():
    """
     connection with mysql
    """
    connection = MySQLdb.connect(host="db",  # your host, usually localhost
                                 port=int(3306),
                                 user=os.getenv("DB_USER"),  # your username
                                 passwd=os.getenv("DB_PASSWORD"),  # your password
                                 db=os.getenv("DB_NAME"))  #
    return connection


def get_full(tiny_url):
    query = "SELECT url_mapping.full FROM url_mapping WHERE url_mapping.tiny = '{}'".format(tiny_url)
    with get_connection().cursor() as cursor:
        cursor.execute(query)
        try:
            result = cursor.fetchone()[0]
            status = True
        except:
            status = False
    if status:
        return True, result
    else:
        return False, ""


def add_link_db(tiny_url, full_url):
    query = "INSERT INTO url_short.url_mapping (tiny,`full`) VALUES ('{}','{}');".format(tiny_url, full_url)
    with get_connection() as conn:
        print(query)
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
        except Exception as e:
            print(Fore.RED + str(e) + Fore.RESET)
