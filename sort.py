import threading
import time
import random
from multiprocessing import Process, Manager


local_arrs=10
local_threads=local_arrs#za vseki slu4ai
arr_size=10



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

def run_local(local_arrs,arrs,processes):#podava se celiq dvumeren!!!








    for process in processes:
        process.start()



    for process in processes:
        process.join()
    #print("test"+str(shared_list))

    #print("test"+str(arrs))



arr=[]
arrs=[]
for i in range(local_arrs):
    for k in range(arr_size):
        arr.append(random.randint(0,1000))
    arrs.append(arr)
    arr=[]
print("FULL")

manager = Manager()
shared_list = manager.list()

for i in range(local_arrs):
    processes = []
    process = Process(target=msort, args=(arrs[i], shared_list,))
    processes.append(process)

#print(arrs)
arrs2=arrs
start=time.time()
for i in arrs2:
    i.sort()
end=time.time()
#print(arrs2)
print("Single CPU:"+str(end-start))



start=time.time()
run_local(local_arrs,arrs,processes)#podavam dvumerniq!!
end=time.time()
print(shared_list)
print("Multi proc: "+str(end-start))
print(arrs2)
#start=time.time()
#for i in range(local_arrs):
 #   arrs2[i].sort()
#end=time.time()

#print("Single: "+str(end-start))
#print(arrs)
#print(arrs2)
#print(arrs)








