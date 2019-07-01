import simplejson

def readarray():
    arr=[]
    with open('masiv', 'r') as FILE:
        arr = simplejson.load(FILE)

    return arr
#arr2=readarray()
#print(arr2)
#print(arr2[0])
#print(masivlist)