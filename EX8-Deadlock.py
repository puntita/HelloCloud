import threading

l = threading.Lock()
print("before first acuire")
l.acquire()
print("before second acquire")
l.acquire()
print("acquired lock twice")