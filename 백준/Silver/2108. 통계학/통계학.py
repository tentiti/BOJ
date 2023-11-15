#통계학
import sys
stats = []
freq = {}

nums = int(sys.stdin.readline())
for i in range(nums):
    stats.append(int(sys.stdin.readline()))
stats = sorted(stats)
stats.append(4001)

# print("answer")

#산술평균
print(round(sum(stats[:len(stats)-1])/(len(stats)-1)))

#중앙값
if len(stats)==2:
    print(stats[0])
else:
    print(stats[int((len(stats)-1)/2)])

#최빈값 -> 여기서 시간초과
maxVal = 0
#일단 하나밖에 없다면 그냥 걔 뽑으면 됨
if len(stats)==2:
    print(stats[0])
#아니면
else:
    #다 freq을 세어볼것임
    for n in range(len(stats)-1):
        if stats[n] in freq:
            freq[stats[n]] += 1
        else:
            freq[stats[n]] = 1
        
    #가장 큰 것 불러와서
    maxVal = max(freq.values())
    # print(freq)
    # print('maxVal', maxVal)
    freqDict = [k for k, v in freq.items() if maxVal == v]
    freqDict.sort()
    # print(freqDict)
            
    #하나만 찾았다면, 첫 번째 뽑고    
    if len(freqDict) == 1:
        print(freqDict[0])
    else:
        print(freqDict[1])

#범위
print(stats[-2]-stats[0])