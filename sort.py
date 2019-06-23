import threading
import time
import random



local_arrs=10
local_threads=local_arrs#za vseki slu4ai
arr_size=100000


class myThread (threading.Thread):
    def __init__(self, threadID, name, counter,arr):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.arr=arr
    def run(self):
        print ("Starting " + self.name)
        self.arr.sort()
        print ("Exiting " + self.name)








def run_local(local_arrs,arr):#podava se celiq dvumeren!!!
    threads=[]
    for i in range(local_arrs):
        thread = myThread(i,"Thread-"+str(i),i,arr[i])
        threads.append(thread)
        thread.start()
    for i in range(local_arrs):
        threads[i].join()



arr=[]
arrs=[]
for i in range(local_arrs):
    for k in range(arr_size):
        arr.append(random.randint(0,1000))
    arrs.append(arr)
    arr=[]


#print(arrs)
arrs2=arrs

start=time.time()
run_local(local_arrs,arrs)#podavam dvumerniq!!
end=time.time()

print("Multi: "+str(end-start))

start=time.time()
for i in range(local_arrs):
    arrs2[i].sort()
end=time.time()

print("Single: "+str(end-start))

#print(arrs)








