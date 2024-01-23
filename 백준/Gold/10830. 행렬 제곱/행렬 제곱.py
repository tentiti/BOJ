n, b = map(int, input().split())

matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
    
def mul_matrix(a, b):
    res = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += a[i][k] * b[k][j] % 1000
    return res

#분할정복
def pow(m, n):
    if n == 1:
        return m
    temp = pow(m, n//2)
    if n%2 == 0:
        return mul_matrix(temp, temp)
    else:
        return mul_matrix(mul_matrix(temp, temp), m)

res = pow(matrix, b)

for i in res:
    for j in i:
        print(j%1000, end=' ')
    print()