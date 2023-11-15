import sys

n = int(input())
mems = []
for i in range(n):
    mems.append([i] + sys.stdin.readline().split())


mems.sort(key= lambda x: (int(x[1]), int(x[0])))

for mem in mems:
    print(mem[1], mem[2])