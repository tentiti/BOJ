for i in range(int(input())):
    t,a,b=input().split()
    a,b=int(a),int(b)
    print(t[:a]+t[b:])