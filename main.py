from pathlib import Path

import openURL as Worker
import mysql_worker as MySQLWorker
import time
import os.path
import sys

file_path = "keep_running.token"

print("Launching at zero....")
for sleep_tick in range(-2, 0):
    print("Launch in... %s" % sleep_tick)
    time.sleep(1)


# create token to delete to stop program
try:
    Path(file_path).touch()
except (FileNotFoundError, IOError):
    print("Unable to create token to keep running. ( %s )" % file_path)
    sys.exit()
except Exception as err:
    print(err)
    sys.exit()

loop = 0
# while True:
while os.path.exists(file_path):
    loop += 1
    worker_result = MySQLWorker.get_full_urls()
    print("LOOP: %s" % loop)
    for x in worker_result:
        print("Hitting Endpoint: %s" % x)
        x_result = Worker.fetch_json_endpoint(x)
    print()
    # time.sleep(1)
