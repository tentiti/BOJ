#123의 분해합  = 129 / 근데 이게 여러개 있을 수도 있음

n = int(input())

gotBHH = False
for i in range(1, n-1): #n보다 작은 수 역순 탐색
    #i에 대해서, 
    temp = i #temp = i
    #i의 분해합 구하는 과정
    m = str(i) #문자로 바꾼 뒤
    for _ in m: #각 자리를
        temp += int(_) #정수로 바꿔서 더한 다음에
    # print(i, temp)
    if temp == n: #이 분해합이 n과 같다면
        print(i)
        gotBHH = True
        break
    
if not gotBHH:
    print(0)