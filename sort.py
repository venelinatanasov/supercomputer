
import time
import random
import pickle
from multiprocessing import Process, Manager
from GenerateArray import genarr





def msort(arr,shared_list):
    arr.sort()
    random.shuffle(arr)
    arr.sort()
    random.shuffle(arr)
    arr.sort()
    random.shuffle(arr)
    arr.sort()
    shared_list.append(arr)

def msort_single(arr):
    arr.sort()
    random.shuffle(arr)
    arr.sort()
    random.shuffle(arr)
    arr.sort()
    random.shuffle(arr)
    arr.sort()
    #shared_list.append(arr)

def run_local(local_arrs,arrs):
    processes=[]

    manager=Manager()
    shared_list=manager.list()



    for i in range(local_arrs):
        process = Process(target=msort, args=(arrs[i],shared_list))
        processes.append(process)



    for process in processes:
        process.start()



    for process in processes:
        process.join()

    arrs=shared_list
    return arrs






#arr=[]
#arrs=[]
#for i in range(local_arrs):
#    for k in range(arr_size):
#        arr.append(random.randint(0,1000))
#    arrs.append(arr)
#    arr=[]
#print("FULL")

#print(arrs)
#arrs2=arrs
#start=time.time()
#for i in arrs2:
#    i.sort()
#end=time.time()
#print(arrs2)
#print("Single CPU:"+str(end-start))



#start=time.time()
##arrs=run_local(local_arrs,arrs)#podavam dvumerniq!!
#end=time.time()
#print(arrs)
#print("Multi proc: "+str(end-start))
#print(arrs2)
#start=time.time()
#for i in range(local_arrs):
 #   arrs2[i].sort()
#end=time.time()

#print("Single: "+str(end-start))
#print(arrs)
#print(arrs2)
#print(arrs)

