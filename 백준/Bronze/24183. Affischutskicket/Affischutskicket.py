a,b,c=map(float,input().split())
a = a * 0.229 * 0.324 * 2
b = b * 0.297 * 0.420 * 2
c = c * 0.210 * 0.297
print("%.3f"%(a+b+c))