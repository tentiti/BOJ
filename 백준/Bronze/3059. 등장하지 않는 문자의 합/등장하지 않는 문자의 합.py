for j in range(int(input())):
    a=input()
    res=0
    for i in range(65,91):
        if chr(i) not in a:
            res += i
    print(res)