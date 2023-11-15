import math

x1, y1, x2, y2, x3, y3 = map(int, input().split())

#일단 평행사변형이 성립할 수 있는가?
#일단 일직선상에 있는지를 확인해 보아야함
phPossible = True
#둘 중에 하나라도 같거나
if (x1 == x2 and y1 == y2) or (x2 == x3 and y2 == y3) or (x1 == x3 and y1 == y3):
    phPossible = False
#일직선 상에 있다면 -> 근데 같으면 일직선 상에 있는 것이므로 위 조건 없애도 됨
elif ((x1-x2)*(y2-y3) == (x2-x3)*(y1-y2)) or ((x2-x3)*(y3-y1) == (x3-x1)*(y2-y3)): #분모 0 가능성 -> 곱해버림
    phPossible = False
# -1 출력하고 끝

#적절히 점 D를 찾기
if phPossible:
    #12 / 34일 경우
    #엥 찾을 필요가 없음
    #12 / 34일 경우
    dul1 = math.sqrt((x1-x2)**2+(y1-y2)**2)*2
    #13 / 24인 경우
    dul2 = math.sqrt((x1-x3)**2+(y1-y3)**2)*2
    #14 / 23인 경우
    dul3 = math.sqrt((x3-x2)**2+(y3-y2)**2)*2
#출력
if phPossible:
    print(max(dul1, max(dul2, dul3))-min(dul1, min(dul2, dul3)))
else:
    print(-1.0)