for i in range(int(input())):
    msg = input()
    ans = 0
    temp = 0
    for i in msg:
        if i == "O":
            temp += 1
        else:
            temp = 0
        ans += temp
    print(ans)