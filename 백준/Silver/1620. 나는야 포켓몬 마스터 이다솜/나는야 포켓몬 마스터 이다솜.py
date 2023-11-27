import sys
input = sys.stdin.readline

species, questions = map(int, input().split())
dogam = {}
for i in range(species):
    name = input().replace('\n','')
    dogam[str(i+1)] = name
    dogam[name] = str(i+1)

# print(dogam)
for i in range(questions):
    print(dogam[input().replace('\n','')])