import sys
input = sys.stdin.readline
testCase = int(input())
for i in range(testCase):
    failed = False
    command = input().strip()
    thisSize = int(input())
    thisArr = []
    direction = 1
    if thisSize != 0:
        arrText = input().strip().replace('[',']').replace(']','')
        thisArr = list(map(int, arrText.split(',')))
        # print(thisArr)
        for l in command:
            if l == 'R':
                direction *= -1
            elif l=='D':
                if thisArr:
                    if direction == 1:
                        thisArr.pop(0)
                    else:
                        thisArr.pop(-1)
                else:
                    print('error')
                    failed = True
                    break
        if failed:
            continue
        elif thisArr:
            thisArr = list(map(str, thisArr))
            if direction == 1:
                 print('[' + ",".join(thisArr) + ']')
            else:
                 thisArr.reverse()
                 print('[' + ",".join(thisArr) + ']')
        else:
            print('[]')
    else:
        thisArr = input()
        if 'D' in command:
            print('error')
        else:
            print('[]')