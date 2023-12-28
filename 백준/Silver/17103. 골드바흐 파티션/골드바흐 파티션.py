def doTheMath(n):
    if n < 2:
        return 0
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return  0
    return 1

primeArray = [0 for i in range(1000001)]

for i in range(1, 1000001, 2):
    primeArray[i] = doTheMath(i)
primeArray[2] = 1


for i in range(int(input())):
    target = int(input())
    partition = 0
    for j in range(2, target//2+1):
        if primeArray[j] and primeArray[target-j]:
            partition+=1
    print(partition)