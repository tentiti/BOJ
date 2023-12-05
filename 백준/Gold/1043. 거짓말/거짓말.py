n, m = map(int, input().split())
truth = input()
if truth == '0':
    print(m)
    exit(0)
else:
    truthKnower = set(truth.split()[1:])
# print(truthKnower, truthKnown)
parties = []
for i in range(m):
    parties.append(set(input().split()[1:]))

#만약 한 사람이 n-1번째 파티에만 있었다면? 이 사람한테 영향받는 사람이 처음에 있을수도 있으니 n번 반복
for i in range(m):
    for party in parties:
        if truthKnower & party:
            truthKnower = truthKnower.union(party)

count = 0 
for party in parties:
    if truthKnower & party:
        continue
    else:
        count += 1

print(count)