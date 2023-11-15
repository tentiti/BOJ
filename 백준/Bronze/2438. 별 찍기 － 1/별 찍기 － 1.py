rep = int(input())
for i in range(rep):
    for j in range(i+1):
        print('*', end='')
    if i != rep-1:
        print('')