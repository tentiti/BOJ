import sys

people = []

#사람 입력하기
for i in range(int(input())):
    person = list(map(int, sys.stdin.readline().split()))
    people.append(person)
rank = [1 for i in range(len(people))]

for i in range(len(people)):
    for j in range(0,len(people)):
        if (people[j][0] > people[i][0]) and (people[j][1] > people[i][1]):
            rank[i] += 1

print(*rank, sep=" ")