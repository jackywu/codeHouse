#!/usr/bin/env python
# encoding: utf-8
#
# a threadpool implementation
#
__authors__  = ['jacky wu <jacky.wucheng@gmail.com>', ]
__version__  = 1.0
__date__     = "Feb 28, 2011 11:23:42 AM"
__license__  = "GPL license"


import Queue
import threading
import time

class ThreadPool:
    def __init__(self, thread_num, q_size , callback):
        self._workers = []
        self._q = Queue.Queue(q_size)
        self._callback = callback
        self._thread_num = thread_num
 
    
    def worker(self):
        while True:
            try:
                req = self._q.get()
            except Queue.Empty:
                time.sleep(0.2)
                continue
            self._callback(req)
            
    
    def run(self):
        for i in range(self._thread_num):
            tname = "worker_%d" % i
            self._workers.append(threading.Thread(target=self.worker, name=tname))
            
        for w in self._workers:
            w.setDaemon(True)
    
        for w in self._workers:
            w.start()
    
    def put_request(self,req):
        self._q.put(req,True)
    
        