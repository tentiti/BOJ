a=open(0).read()
def d(k):
    return a.count(k)
def c(k):
    return a.lower().count(k)
print((d('P')+d('N')*3+d('B')*3+d('R')*5+d('Q')*9)*2-(c('p')+c('n')*3+c('b')*3+c('r')*5+c('q')*9))