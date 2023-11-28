import sys
input = sys.stdin.readline


rep = int(input())
coordinates_raw = list(map(int, input().split()))
coordinates = list(set(coordinates_raw))
coordinates.sort()
coordinates_place = {}
for i in range(len(coordinates)):
    coordinates_place[coordinates[i]] = i

for i in coordinates_raw:
    print(coordinates_place[i], end=' ')

