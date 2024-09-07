d,p=0,0
for i in range(int(input())):
    if input()=='D':
        d+=1
    else:
        p+=1
    if abs(d-p)>1:
        break
print("{}:{}".format(d,p))