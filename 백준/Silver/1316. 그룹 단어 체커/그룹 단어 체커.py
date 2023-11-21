rep = int(input())
count = 0

for i in range(rep):
    word = input()
    considered = []
    usable = True
    for i in range(len(word)):
        letter =  word[i]
        if letter not in considered:
            considered.append(letter)
            groupGoal = word.count(letter)
            # print(word.split(letter)) #일단 제거완료
            checker = word.split(letter,1)[1]
            if letter in checker: #근데 연속이면?
               if not checker[:groupGoal-1] == (letter*(groupGoal-1)):
                    usable = False
                    # print('no')
                    break
        else:
            continue
    if usable: count += 1
print(count)