import math
a, b, c = map(float, input().split())
print(math.ceil(a/c)*math.ceil(b/c))