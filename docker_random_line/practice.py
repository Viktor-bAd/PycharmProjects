import time
import random

symbol: str = "-"
min_len: int = 7
max_len: int = 10
delay: float = 2.0
while True:
    length = random.randint(min_len, max_len)
    print(symbol * length)
    time.sleep(delay)
