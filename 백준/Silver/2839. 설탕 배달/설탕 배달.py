w = int(input())

ans = 0

while w >= 0:
    if w % 5 == 0:
        ans += int (w//5)
        print(ans)
        break
    
    w -= 3
    ans += 1
else:
    print(-1)