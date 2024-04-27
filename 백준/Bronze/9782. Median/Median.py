cnt=0
while True:
    cnt += 1
    a=list(map(int,input().split()))
    if a[0]==0:
        break
    elif int(a[0])%2==1:
        median = a[int((len(a)+1) / 2)]
        print("Case {}: {:.1f}".format(cnt, median))
    else:
        mid_index = int(len(a) / 2)
        median = (a[mid_index + 1] + a[mid_index]) / 2
        print("Case {}: {:.1f}".format(cnt, median))