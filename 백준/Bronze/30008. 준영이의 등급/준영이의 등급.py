n, k = map(int, input().split())
scores = list(map(int, input().split()))
grades_percentile=[4,11,23,40,60,77,89,96,100]
for score in scores:
    print(1+grades_percentile.index(min([x for x in grades_percentile if x >= (score * 100 // n )])), end=' ')