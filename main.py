import openURL as Worker
import mysql_worker as MySQLTest
import time

print("Launching at zero....")
for sleep_tick in range(-4, 0):
    print("Launch in... %s" % sleep_tick)
    time.sleep(1)


# get list of endpoints
worker_result = MySQLTest.get_full_urls()

# hit all endpoints found... a bunch...
i = 0
max_loops = 500
for loop in range(max_loops):
    print("LOOP: %s" % loop)
    for x in worker_result:
        i = i + 1
        print("%s) Result: %s" % (i, x))
        x_result = Worker.fetch_json_endpoint(x)
    time.sleep(5)

