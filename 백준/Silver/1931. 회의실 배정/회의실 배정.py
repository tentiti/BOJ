import sys
input = sys.stdin.readline

#회의실 시간 배정 -> 끝나는 시간이 빠르고, 같다면 시작 시간이 늦은 것 부터

plans = int(input())
agenda = []
# selected = []

for i in range(plans):
    start, end = map(int, input().split())
    agenda.append((start, end))

agenda.sort(key= lambda x: (x[1], x[0]))

temp = agenda[0]
count = 1

for i in range(1, plans):
    if agenda[i][0] >= temp[1]:
        count += 1
        temp = agenda[i]

print(count)
        