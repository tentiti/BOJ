import sys
input = sys.stdin.readline

p = 1000000007

def mul(a, b): #두 행렬 곱하기
    # n = len(a) #앞 행렬의 세로 크기
    Z = [[0]*2 for _ in range(2)] #만큼 
    
    for row in range(2):
        for col in range(2):
            e = 0
            for i in range(2):        
                e += a[row][i]*b[i][col]
            Z[row][col] =e%p
    
    return Z

def square(a, k):
    if k == 1:
        return a
    temp = square(a, k//2)
    if k%2 == 0:
        return mul(temp, temp)
    else:
        return mul(mul(temp, temp), a)

fib_matrix=[[1,1],[1,0]]
print(square(fib_matrix, int(input()))[0][1]%p)