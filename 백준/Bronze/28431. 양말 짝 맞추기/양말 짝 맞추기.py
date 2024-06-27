a=list((open(0).readlines()))
for b in a:
    if a.count(b)%2:
        print(b)
        break