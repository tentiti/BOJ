n, b = map(int, input().split())
letters='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans=[]
while n != 0:
    ans.append(letters[n%b])
    # temp = n % b
    n = n//b
print(*ans[::-1],sep='')