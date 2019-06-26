import random
import pickle
arr = []
barr = []

arrlen = 200
arrcount = 50

FILE = open('masiv', "wb+")

def genarr(arr, barr):
    for k in range(arrlen):
        arr.append(random.randint(1, 1000))

    for j in range(arrcount):
        barr.append(k)



genarr(arr, barr)
print(arr)
pickle.dump(arr,FILE)

#FILE.write(f)
FILE.close()

print(len(arr))

print("DONE")