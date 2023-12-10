a = input()
b = input()

#일단 LCS
c=[[0 for i in range(len(b)+1)] for j in range(len(a)+1)]

#c[i][j]
for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            c[i][j] = c[i-1][j-1]+1
        else:
            c[i][j] = max(c[i-1][j], c[i][j-1])

# for _ in c:
#     print(_)
print(c[len(a)][len(b)])