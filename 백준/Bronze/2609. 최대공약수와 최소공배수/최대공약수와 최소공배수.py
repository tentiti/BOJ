a, b = map(int, input().split())
e = a*b
c = 0
d = 0

#최대공약수
while b > 0:
    a, b = b, a%b
    c = a

d = e//c

print(c)
print(d)