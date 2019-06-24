import random
import pickle
arr = []
barr = []

arrlen = 20
arrcount = 100

FILE = open('masiv', "wb+")

def genarr(arr, barr):
    for k in range(arrcount):
        for i in range(arrlen):
            barr.append(random.randint(0, 1000))
        arr.append(barr)
        barr=[]



genarr(arr, barr)
print(arr)
pickle.dump(arr,FILE)

#FILE.write(f)
FILE.close()

print("DONE")