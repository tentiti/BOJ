def solution(clothes):
    wardrobe = dict()
    for c in clothes:
        wardrobe[c[1]] = wardrobe.get(c[1], []) + [c[0]]
    answer = 1
    for t in wardrobe.keys():
        answer *= len(wardrobe[t])+1
    return answer-1