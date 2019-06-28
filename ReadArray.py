import pickle


def readarray():
    arr=[]
    with open('masiv', 'rb') as FILE:
        arr = pickle.load(FILE)

    return arr
#print(readarray())
#print(masivlist)