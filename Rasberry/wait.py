#!/usr/bin/env python

import time
import thread

# found in stack over flow
def wait_result():

    def work():
        time.sleep(5)

    def lock_call(func,lock):
        lock.acquire()
        func()
        lock.release()

    lock = thread.allocate_lock()
    thread.start_new_thread( lock_call, ( work, lock, ) )
    
    while(not lock.locked()):
        time.sleep(1)
    while(lock.locked()):
        time.sleep(1)

 
