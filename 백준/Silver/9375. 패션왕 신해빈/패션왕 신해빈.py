testCase = int(input())

for i in range(testCase):
    closet = {}
    clothes = int(input())
    temp_genre = ''
    for j in range(clothes):
        cloth = input().split()
        temp_genre = cloth[1]
        if cloth[1] in closet:
            closet[cloth[1]] += 1
        else:
            closet[cloth[1]] = 1
    if len(closet) == 1:
        print(closet[temp_genre])
    else:
        temp = 1
        cloth_count = list(closet.values())
        # cloth_count.sort(reverse=True)
        for thisKind in cloth_count:
            temp *= (thisKind + 1)
        print(temp - 1)
            
    
        
    