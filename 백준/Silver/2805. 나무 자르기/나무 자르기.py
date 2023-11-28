trees, target = map(int, input().split())

forest = list(map(int, input().split()))
# forest.sort(reverse=True)
# forest = tuple(forest)
# print(forest)

#bst를 해 봅시다
height_low = 1
height_high = max(forest)

while height_low <= height_high:
    height_mid = (height_high+height_low)//2
    temp = 0
    for tree in forest:
        if tree > height_mid:
            temp += tree-height_mid
    if temp >= target:
        height_low = height_mid + 1
    elif temp < target:
        height_high = height_mid - 1

print(height_high)