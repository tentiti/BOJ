i=input
n=int(i())
s=i()
t=i()
r=0
for j in range(n):
    r += 1*(ord(s[j])!=ord(t[j]))
print(r)