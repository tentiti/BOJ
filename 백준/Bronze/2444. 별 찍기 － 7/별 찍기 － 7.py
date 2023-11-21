rep = int(input())
for i in range(1, rep):
    msg = '*'*(2*i-1)
    print(msg.rjust(rep-1+i))
for i in range(rep, 0, -1):
    msg = '*'*(2*i-1)
    if i <= 1:
        print(msg.rjust(rep-1+i), sep='')
    else:
        print(msg.rjust(rep-1+i))