length = int(input())
timeArr = [1] * (length+1)

if length == 1:
    print(1)
elif length == 2:
    print(3) #가로 두개, 새로 두개 or 통으로 하나 추가됨
# elif length == 3:
#     #ㅣㅣㅣ, =ㅣ, ㅣ=, 미,ㅣㅁ 의 5개
#     print(5)
else:
    timeArr[2] = 3
    for i in range(3, len(timeArr)):
        #생각해보기:
        #하나 짧은거 뒤에 | 더하기
        #두개 짧은거 뒤에 =나 ㅁ 더하기
        timeArr[i] = timeArr[i-1] + 2*timeArr[i-2]
        # timeArr[i] 

    print(timeArr[length]% 10007)