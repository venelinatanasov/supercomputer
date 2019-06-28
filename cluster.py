import time
import random
import pickle
from multiprocessing import Process, Manager
from GenerateArray import genarr
from sort import msort, run_local
from ReadArray import readarray

local_arrs=10
arr_size=10000

def cluster():
    genarr(local_arrs,arr_size)

    arr=readarray()

    arr2=readarray()


    start=time.time()

    for i in range(len(arr)):
        arr[i].sort()

    end=time.time()

    print("Single: "+str(end-start))




    start=time.time()
    arr=run_local(local_arrs,arr)
    end=time.time()


    print("Multi: "+str(end-start))


cluster()