import threading
import time
import random

local_threads=8
local_arrs=8


def msort(arr):
    arr.sort()


def run_local(local_threads,arr):
    threads=[]
    for i in range(local_threads):
        thread = threading.Thread(target=msort, args=(arr[i],))
        threads.append(thread)
        thread.start()
    for i in range(local_threads):
        threads[i].join()



arr=[]
arrs=[]
for i in range(local_arrs):
    for i in range(5000):
        arr.append(random.randint(0,1000))
    arrs.append(arr)



for i in range(local_arrs):
    arrs.append(arr)
    for k in range(5000):
        arrs[i].append(random.randint)

run_local(local_threads,arrs)









