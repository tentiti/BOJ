a=input()
if a=='1010':
    print(20)
elif '0' in a:
    print(int(a.replace('10',''))+10)
else:
    print(int(a[0])+int(a[1]))