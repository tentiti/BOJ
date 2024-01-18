import sys
import math
input = sys.stdin.readline

X = 1000000007
ans = 0

#X-2번 거듭제곱 하는 코드
def power(n, p):
    if p == 1: #power가 1이면 바로 내보내기
        return n % X
    elif p % 2: #홀수일 경우, 짝수로 만들어서 곱셈 한번 하면 됨
        return n * power(n, p-1) % X
    else: #짝수일 경우, 그냥 두 번 곱하면 됨.
        p = power(n, p//2)
        return p*p%X

diceCount = int(input())
# dices = []
for i in range(diceCount):
    # dices.append(list(map(int, input().split())))
    bm, bj = map(int, input().split())
    
    #기약분수 만들기 -> 사실 필요하지는 않음
    # gcd = math.gcd(bm, bj)
    # bm //= gcd
    # bj //= gcd
    
    #즉, a / b 꼴로 만든 다음에, a * b^(X-2) % X를 구하면 됨.
    ans += bj * power(bm, X-2) % X
    ans %= X

print(ans)
