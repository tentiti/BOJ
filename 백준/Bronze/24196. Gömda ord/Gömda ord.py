t=input()
res=t[0]
i = ord(t[0])-64
while i < len(t)-1:
    res += t[i]
    i += ord(t[i])-64
        
print(res+t[-1])