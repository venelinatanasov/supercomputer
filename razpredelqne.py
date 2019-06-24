import pickle

core_count = 19

# Computer
class Computer(object):
    def __init__(self, ip, file, arrays):
        self.ip = ip
        self.file = file
        self.arrays = arrays

Computer1 = Computer('192.168.91.2', 'masi.txt', 0)

#Deviding algorithm
with open('masiv', 'rb') as FILE:
    masivlist = pickle.load(FILE)


v = len(masivlist) % core_count
t = int((len(masivlist)) / core_count)


Computer1.arrays += t
Computer1.arrays += v

print(len(masivlist))
print(v)
print(Computer1.arrays)
print(t)
