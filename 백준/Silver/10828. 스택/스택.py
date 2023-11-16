import sys

dq = []

for i in range(int(input())):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        dq.append(command[1])
    elif command[0] == 'pop':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])
            dq = dq[:-1]
    elif command[0] == 'size':
        print(len(dq))
    elif command[0] == 'empty':
        if(len(dq) < 1):
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if(len(dq) > 0):
            print(dq[-1])
        else:
            print(-1)
    # print(dq)