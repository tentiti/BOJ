nowtime = input().split()

answer = 0.0

#월일 계산
#윤년? -> day = 366
if (int(nowtime[2]) % 4 == 0 and int(nowtime[2])%100 != 0) or int(nowtime[2]) % 400 == 0:
    monthName = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    monthCount = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    daySpent = 0
    myMonthIndex = monthName.index(nowtime[0])
    for i in range(myMonthIndex):
        daySpent += monthCount[i]
    daySpent += int(nowtime[1].removesuffix(','))
    answer += (daySpent -1) / 366
    #시간 계산
    hrElapse = int(nowtime[3].split(':')[0])
    minElapse = int(nowtime[3].split(':')[1])
    answer += ((hrElapse / 24)+minElapse/1440)/366

#윤년 아님 -> day = 365
else:
    monthName = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    monthCount = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]   
    daySpent = 0
    myMonthIndex = monthName.index(nowtime[0])
    for i in range(myMonthIndex):
        daySpent += monthCount[i]
    daySpent += int(nowtime[1].removesuffix(','))
    answer += (daySpent-1) / 365
    #시간 계산
    hrElapse = int(nowtime[3].split(':')[0])
    minElapse = int(nowtime[3].split(':')[1])
    answer += ((hrElapse / 24)+minElapse/1440)/365
    
print(answer*100)