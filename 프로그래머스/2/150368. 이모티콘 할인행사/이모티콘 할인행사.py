from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    combis = product([10,20,30,40] ,repeat=(len(emoticons)))
    for combi in combis:
        subs = 0
        sales = 0
        for user in users:
            tempPrice = 0
            for i in range(len(emoticons)):
                if combi[i] >= user[0]:
                    tempPrice += emoticons[i] * (100-combi[i])/100
            if tempPrice >= user[1]:
                subs += 1
            else:
                sales += tempPrice
        if subs > answer[0]:
            answer[0] = subs
            answer[1] = sales
        elif subs == answer[0]:
            answer[0] = subs
            answer[1] = max(sales,  answer[1])
    return answer