import math
s=int(input())
a=int(input())
b=int(input())
print(250+math.ceil((s-a)/b)*100 if s>a else 250)