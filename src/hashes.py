import time
import hashlib

n = 1000000

key = b"STR"

for _ in range(10):
    print(hashlib.sha256(key).hexdigest())
