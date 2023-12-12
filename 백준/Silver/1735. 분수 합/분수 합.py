import math
a, b = map(int, input().split())
c, d = map(int, input().split())
print(int((a*d+b*c)/math.gcd(a*d+b*c, b*d)), int(b*d/math.gcd(a*d+b*c, b*d)))