import random
import simplejson
import pickle
#arr = []
#barr = []
#
arr_size = 5
local_arrs = 3

#FILE = open('masiv', "w")

def genarr(local_arrs, arr_size):
    arrs=[]
    arr=[]
    FILE = open('masiv', "w")

    for i in range(local_arrs):
       for k in range(arr_size):
           arr.append(random.randint(0,1000))
       arrs.append(arr)
       arr=[]
    simplejson.dump(arrs,FILE)
    FILE.close()
    #print(arrs)
genarr(local_arrs,arr_size)
#arr=[]
#genarr(arr)
#print(arr)
#genarr(arr, barr)
#print(arr)

#FILE.write(f)




