import sys

def round2(num): # 사사오입
    return int(num) + (1 if num - int(num) >= 0.5 else 0)

n = int(input())
if n == 0:
    print(0)
else: 
    margin = round2(float(n*0.15))
    level = []
    
    for i in range(n):
        level.append(int(sys.stdin.readline()))
        
    # print(level)
    if margin > 0:
        level = sorted(level)[margin:n-margin]
    avg = round2(sum(level)/len(level))
    
    print(avg)