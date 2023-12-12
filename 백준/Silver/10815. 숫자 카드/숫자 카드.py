cards = int(input())
inventory = set(map(int, input().split()))
quiz =  int(input())
questionnair = list(map(int, input().split()))

for _ in questionnair:
    if _ in inventory: print(1, end=' ')
    else: print(0, end=' ')