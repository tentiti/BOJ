num = int(input())
m = 2
while num > 1:
    if num%m == 0:
        print(m)
        num //= m
    else:
        m += 1
        
#어차피 소인수는 늘어니니가