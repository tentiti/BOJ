import sys
n = int(sys.stdin.readline())
cards = {}

nums = list(map(int, sys.stdin.readline().split()))

for n in nums:
    if cards.get(n) == None:
        cards.update({n: 1})
    else:
        temp = cards.get(n)
        cards.update({n: temp+1})
# print(cards)

m = int(sys.stdin.readline())

keys = list(map(int, sys.stdin.readline().split()))

for key in keys:
    if cards.get(key) == None:
        print("0", end= " ")
    else:
        print(cards.get(key), end= " ")