myArr= []
for i in range(int(input())):
    myArr.append(int(input()))
myArr.sort()

ans = 4
for i in range(len(myArr)): #일단 바로 올바르게 만들 수 있는지 확인
    if i <= len(myArr)-6 and sum(myArr[i:i+5]) == myArr[i]*5+10: #올바르다면?
        ans=0
        break
    else: #올바르지 않다면?(1,2,4,5,6 있다면? 3을 추가해야함.)
        locator = min(i+5, len(myArr))
        ans = min(ans, len(set([j for j in range(myArr[i], myArr[i]+5)])-set(myArr[i:locator])))
        # print(set([j for j in range(myArr[i], myArr[i]+5)]), set(myArr[i:locator]), ans)
       
print(ans)