
import time
import random
import pickle
from multiprocessing import Process, Manager
from GenerateArray import genarr



#local_arrs=2
#local_threads=local_arrs#za vseki slu4ai
#arr_size=10


def msort(arr,shared_list):
    arr.sort()
    #print(arr)
    shared_list.append(arr)




#def run_local(local_arrs,arr):#podava se celiq dvumeren!!!
#    threads=[]
#    for i in range(local_arrs):
#        thread = myThread(i,"Thread-"+str(i),i,arr[i])
#        threads.append(thread)
#        thread.start()
#    for i in range(local_arrs):
#        threads[i].join()
#
def run_local(local_arrs,arrs):#podava se celiq dvumeren!!!
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
    #print("test"+str(shared_list))
    arrs=[]
<<<<<<< HEAD
    for i in range(len(shared_list)):
        arrs.append([])
        for k in range(len(shared_list[i])):
            arrs[i].append(shared_list[i][k])
    return arrs

=======

    #########CONVERT!!!!!!!!!###########
>>>>>>> Merge remote-tracking branch 'origin/master'

    #print("test"+str(arrs))



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

