import time
import pydantic
import sys
import datetime


start_time = datetime.datetime.now()

while True:
    time.sleep(2)
    print(sys.version)
    print(pydantic.__version__)
    print(start_time)
