for k in range(int(input())):
    m = input()
    for i in range(len(m)):
        if m[i] != m[i-1] or i==0:
            print(m[i], end="")
    print()