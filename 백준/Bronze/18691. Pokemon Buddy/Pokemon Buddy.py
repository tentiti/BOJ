for i in range(int(input())):
    s=list(map(int,input().split()))
    print(max(0,(2*s[0]-1)*(s[2]-s[1])))