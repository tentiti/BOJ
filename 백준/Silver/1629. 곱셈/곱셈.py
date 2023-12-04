a, b, c = map(int, input().split())

def pow(m, n):
    if n == 1:
        return m%c
    temp = pow(m, n//2)
    if n%2 == 0:
        return (temp * temp) % c
    else:
        return ((temp**2)*m) % c

print(pow(a, b))