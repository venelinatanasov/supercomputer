import pickle

core_count = 19

# Computer
class Computer(object):
    def __init__(self, ip, file, corecount, arrays):
        self.ip = ip
        self.file = file
        self.corecount = corecount
        self.arrays = arrays

#Computerlist
Computer1 = Computer('192.168.91.1', 'masi.txt', 8, 0)
Computer2 = Computer('192.168.91.2', 'masi.txt', 4, 0)
Computer3 = Computer('192.168.91.3', 'masi.txt', 2, 0)
Computer4 = Computer('192.168.91.4', 'masi.txt', 3, 0)
Computer5 = Computer('192.168.91.5', 'masi.txt', 1, 0)
Computer6 = Computer('192.168.91.6', 'masi.txt', 1, 0)

computers = [Computer1, Computer2, Computer3, Computer4, Computer5, Computer6]

#Deviding algorithm
with open('masiv', 'rb') as FILE:
    masivlist = pickle.load(FILE)


v = len(masivlist) % core_count
t = int((len(masivlist)) / core_count)


for i in computers:
    i.arrays += t * i.corecount

for j in computers:
    j.arrays += 1
    v -= 1
    if v == 0:
        break;

print(len(masivlist))

for u in computers:
    print(u.arrays)
