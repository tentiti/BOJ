nChamp='1'
newInt = 2
key=input()
while len(nChamp) < len(key):
    nChamp += str(newInt)
    newInt += 1
if nChamp == key:
    print(newInt-1)
else:
    print(-1)