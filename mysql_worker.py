import sys
import mysql.connector
# pip install mysql-connector-python


host_suffix = "cuoaamkhgxxd.us-east-1.rds.amazonaws.com"
host = "%s.%s" % (sys.argv[1], host_suffix)
user = sys.argv[2]
password = sys.argv[3]
database = sys.argv[4]


def get_full_urls():
    results = []
    try:
        my_db = mysql.connector.connect(
            host=host,
            user=user,
            passwd=password,
            database=database,
        )

        my_cursor = my_db.cursor()
        # my_cursor.execute("SELECT fullURL FROM python_endpoints order by id DESC")
        my_cursor.execute("SELECT fullURL FROM python_endpoints ORDER BY id")
        my_result = my_cursor.fetchall()

        for x in my_result:
            results.append(x[0])
    except Exception as e:
        print(e)

    return results
