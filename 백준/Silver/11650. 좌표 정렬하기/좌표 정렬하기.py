import sys
coordinates = []
for i in range(int(input())):
    coordinates.append(sys.stdin.readline().split())

coordinates.sort(key = lambda x :(int(x[0]), int(x[1])))

for _ in coordinates:
    print("{} {}".format(_[0], _[1]))