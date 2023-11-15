#벌집
#1: 1 -> 
#2~7: 2 -> 6개
#8~19: 3 -> 12개
#20~37: 4

room = int(input())
cnt = 1
room -= 1

while room > 0:
    room -= 6*cnt
    cnt += 1

print(cnt)