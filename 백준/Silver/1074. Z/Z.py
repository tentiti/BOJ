import sys
sys.setrecursionlimit(10**6)

ans = 0
        
n, r, c = map(int, input().split())

while n != 0 :
    n -=1
    #top-left
    if r < 2 ** n and c < 2 ** n:
        ans += (2**(n))**2 * 0
    #top-right
    elif r >= 2 ** n and c < 2 ** n :
        ans += (2**(n))**2 * 2
        r -= 2**(n)
    #bottom-left
    elif r < 2 ** n and c >= 2 ** n :
        ans += (2**(n))**2 * 1
        c -= 2**(n)
    #bottom-right
    else:
        ans += (2**(n))**2 * 3
        r -= 2**(n)
        c -= 2**(n)

print(ans)