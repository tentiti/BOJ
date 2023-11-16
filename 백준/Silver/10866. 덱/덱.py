import sys

dq = []

for i in range(int(input())):
    command = sys.stdin.readline().split()
    if command[0] == 'push_back':
        dq.append(command[1])
    elif command[0] == 'push_front':
        dq = [command[1]] + dq
    elif command[0] == 'pop_back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])
            dq = dq[:-1]
    elif command[0] == 'pop_front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
            dq = dq[1:]
    elif command[0] == 'size':
        print(len(dq))
    elif command[0] == 'empty':
        if(len(dq) < 1):
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if(len(dq) > 0):
            print(dq[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if(len(dq) > 0):
            print(dq[-1])
        else:
            print(-1)
    # print(dq)