import socket
import threading
#import requests
from queue import Queue
lines = ["NOOB_SEC_TOOLKIT",
         "*Local Network Port Scanner*"]
print('-------------------------------------------------------------')
         

from time import sleep
import sys

for line in lines:          # for each line of text (or each message)
    for c in line:          # for each character in each line
        print(c, end='')    # print a single character, and keep the cursor there.
        sys.stdout.flush()  # flush the buffer
        sleep(0.1)          # wait a little to make the effect look good.
    print('')               # line break (optional, could also be part of the message)
print('-------------------------------------------------------------')

host = '127.0.0.1'
lock = threading.Lock()


def port_scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        lock.acquire()
        print(("Port ") + str(port) + (" is open!"))
        lock.release()
        s.close()
    except:
        return False


q = Queue()


# Work that thread will do
def worker():
    while True:
        port = q.get()
        port_scan(port)
        q.task_done()


# Add port numbers to queue to check
for i in range(10000):
    q.put(i)
# Threads
for i in range(100):
    t = threading.Thread(target=worker)
    # t.daemon = True
    t.start()
sys.exit()