n = int(input())

for i in range(n):
    msg = input()

    while "()" in msg:
        msg = msg.replace('()','')
    
    if len(msg) == 0:
        print("YES")
    else:
        print("NO")