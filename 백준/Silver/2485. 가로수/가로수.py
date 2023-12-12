import math
trees = []
for i in range(int(input())):
    trees.append(int(input()))
trees.sort()
# print(trees)
distance = []
for i in range(len(trees)-1):
    distance.append(trees[i+1]-trees[i])
# print(distance)
print(int((trees[-1]-trees[0])/math.gcd(*distance))-len(trees)+1)