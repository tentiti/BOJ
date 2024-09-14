res=0
for i in range(int(input())):
    a=input()
    res+= ('01' in a or 'OI' in a)*1
print(res)