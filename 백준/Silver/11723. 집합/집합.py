import sys
input = sys.stdin.readline

commands = int(input())
mySet = set()

for i in range(commands):
    command = input().split()
    if command[0] == 'add':
        mySet.add(int(command[1]))
    elif command[0] == 'remove':
        if int(command[1]) in mySet:
            mySet.remove(int(command[1]))
    elif command[0] == 'check':
        if int(command[1]) in mySet:
            print(1)
        else:
            print(0)
    elif command[0] == 'toggle':
        if int(command[1]) in mySet:
            mySet.remove(int(command[1]))
        else:
            mySet.add(int(command[1]))
    elif command[0] == 'all':
        for i in range(1, 21):
            mySet.add(i)
    elif command[0] == 'empty':
        mySet.clear()