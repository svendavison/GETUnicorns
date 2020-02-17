import sys
import mysql.connector
# pip install mysql-connector-python

host_suffix = "cuoaamkhgxxd.us-east-1.rds.amazonaws.com"

# print("The script has the name %s" % (sys.argv[0]))
# print("FQDN DB-Hostname: %s.%s" % (sys.argv[1], host_suffix))
# print("Username: %s" % (sys.argv[2]))
# print("Password: %s" % (sys.argv[3]))
# print("Database: %s" % (sys.argv[4]))

host = "%s.%s" % (sys.argv[1], host_suffix)
user = sys.argv[2]
password = sys.argv[3]
database = sys.argv[4]

try:

    my_db = mysql.connector.connect(
        host=host,
        user=user,
        passwd=password,
        database=database,
    )

    my_cursor = my_db.cursor()
    my_cursor.execute("SELECT * FROM python_endpoints")
    my_result = my_cursor.fetchall()

    for x in my_result:
        print(x)
except Exception as e:
    print(e)
