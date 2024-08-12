s=input()
t = [a for a in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if a not in s]
print(''.join(t))