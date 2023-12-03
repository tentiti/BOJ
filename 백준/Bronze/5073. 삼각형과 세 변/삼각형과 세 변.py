while True:
    tri = list(map(int, input().split()))
    if sum(tri) == 0:
        break
    tri.sort()
    if tri[2] >= tri[0] + tri[1]:
        print('Invalid')
    elif tri[0] == tri[2]:
        print('Equilateral')
    elif tri[0] == tri[1] or  tri[2] == tri[1]:
        print('Isosceles')
    else:
        print('Scalene')