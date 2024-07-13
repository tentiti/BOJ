sectionCount = 0
lastSub = ''
currentloc = '1'

res = []

for i in range(int(input())):
    command = input().split('section ', 1)
    # print(command)

    # subsection
    if 'sub' in command[0]:
        # same level
        if len(lastSub) == len(command[0]):
            a = currentloc.split('.')
            currentloc = '.'.join(a[:-1])+'.'+str(int(a[-1])+1)
        # higher level
        elif len(lastSub) > len(command[0]):
            a = currentloc.split('.')
            currentloc = '.'.join(a[:-2])+'.'+str(int(a[-2])+1)
        # lower level4
        elif len(lastSub) < len(command[0]):
            currentloc = currentloc + ".1"

        lastSub = command[0]

    else:
        sectionCount += 1
        currentloc = str(sectionCount)
        lastSub = ''

    res.append(str(currentloc+' '+command[1]))

for i in res:
    print(i)
