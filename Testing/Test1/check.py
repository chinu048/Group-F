import time

start = time.time()
print(time.time())
curr = time.time()
print(curr-start)
print(type(start))
if ((curr-start)>=0):
    print("OK")
