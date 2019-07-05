import time
import random
import pickle
from multiprocessing import Process, Manager
from GenerateArray import genarr
from sort import msort, run_local_sort, msort_single
from ReadArray import readarray
import  simplejson
local_arrs=3
arr_size=5

def run_local():
    genarr(local_arrs,arr_size)

    arr=readarray()
    #print("1 read")
    #arr2=readarray()
    #print("2 read")
    #print(arr)

    #start=time.time()

    #for i in range(len(arr2)):
    #    msort_single(arr2[i])

    #end=time.time()

    #print("Single: "+str(end-start))




    #start=time.time()

    arr=run_local_sort(local_arrs,arr)
    file=open('out','w')
    #simplejson.dump(arr,file)
    file.close()
    #end=time.time()


    #print("Multi: "+str(end-start))
    #print(arr)
    #print(arr2)

run_local()