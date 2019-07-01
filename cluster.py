import time
import random
import pickle
from multiprocessing import Process, Manager
from GenerateArray import genarr
from sort import msort, run_local, msort_single
from ReadArray import readarray

local_arrs=10
arr_size=10000

def cluster():
    #genarr(local_arrs,arr_size)

    arr=readarray()
    print("1 read")
    arr2=readarray()
    print("2 read")


    start=time.time()

    for i in range(len(arr2)):
        msort_single(arr2[i])

    end=time.time()

    print("Single: "+str(end-start))




    start=time.time()
    arr=run_local(local_arrs,arr)
    end=time.time()


    print("Multi: "+str(end-start))


cluster()