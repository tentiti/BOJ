def doTheMath(n):
    if n < 2:
        return 0
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return  0
    return 1

isPrime = [0 for i in range(123456*2+1)]
isPrime[2] = 1

for i in range(1, 123456*2+1, 2):
    isPrime[i] = doTheMath(i)
    
while True:
    n = int(input())
    if n== 0:
        break
    else:
        print(sum(isPrime[n+1:2*n+1]))