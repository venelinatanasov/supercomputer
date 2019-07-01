import random
import pickle
#arr = []
#barr = []
#
arr_size = 500000
local_arrs = 10

#FILE = open('masiv', "w")

def genarr(local_arrs, arr_size):
    arrs=[]
    arr=[]
    FILE = open('masiv', "wb")

    for i in range(local_arrs):
       for k in range(arr_size):
           arr.append(random.randint(0,1000))
       arrs.append(arr)
       arr=[]
    pickle.dump(arrs, FILE)
    FILE.close()
    #print(arrs)
genarr(local_arrs,arr_size)
#arr=[]
#genarr(arr)
#print(arr)
#genarr(arr, barr)
#print(arr)

#FILE.write(f)




