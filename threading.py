import threading
import Queue
import time

def f(q):
    while True:
        q.get()() #block thread until something shows up

def randomize():
    for x in xrange(10):
        print x
    
q = Queue.Queue()
t = threading.Thread(target=f,args=[q])
t.start()
q.put(randomize)
for x in xrange(10,20):
    print x

