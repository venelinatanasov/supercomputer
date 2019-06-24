import pickle

with open('masiv', 'rb') as FILE:
    masivlist = pickle.load(FILE)

print(masivlist)