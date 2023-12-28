def doTheMath(n):
    if n <= 2:
        print(2)
        return
    for i in range(n, 10**10):
        finder = False
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                finder = True
                break
        if not finder:
            print(i)
            return

for i in range(int(input())):
    doTheMath(int(input()))