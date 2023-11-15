e, s, m = map(int, input().split())

i = 1
while True:
    if i % 15 == e % 15 and i % 28 == s % 28 and i % 19 ==m % 19:
        break
    else:
        i += 1
        
print(i)