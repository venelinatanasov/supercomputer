import time
import random
import pickle
from multiprocessing import Process, Manager
from GenerateArray import genarr
from sort import msort, run_local
from ReadArray import readarray

local_arrs=2
arr_size=1000

def cluster():
    genarr(local_arrs,arr_size)
    arr=readarray()
    run_local(local_arrs,arr)

    print(arr)



cluster()