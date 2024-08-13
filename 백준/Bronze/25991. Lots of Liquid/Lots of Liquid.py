a=input()
a=[a**3 for a in map(float,input().split())]
print(sum(a)**(1/3))