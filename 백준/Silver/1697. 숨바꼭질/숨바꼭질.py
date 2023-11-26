sb, sis = map(int, input().split())
# sb, sis = 5, 17
queue = []

def timeWalker(pos):
    if sbtime[pos + 1] == -1:
        sbtime[pos + 1] = sbtime[pos]+1
    if sbtime[pos - 1] == -1:
        sbtime[pos - 1] = sbtime[pos]+1
    if sbtime[pos *2] == -1:
        sbtime[pos *2] = sbtime[pos]+1

#+1, -1, *2
sbtime = [-1 for i in range(1000001)]
sbtime[sb] = 0
# sbtime[sb+1] = 1
# sbtime[sb-1] = 1
# sbtime[sb*2] = 1

temploc = sb
queue.append(temploc)
while sbtime[sis] == -1 and len(queue) != 0:
    temploc = queue.pop(0)
    #print(temploc)
    if temploc > 100000 or temploc < 0:
        continue
    if sbtime[temploc + 1] == -1:
        queue.append(temploc+1)
    if sbtime[temploc - 1] == -1:
        queue.append(temploc-1)
    if sbtime[temploc *2] == -1:
        queue.append(temploc*2)
    timeWalker(temploc)
    
print(sbtime[sis])