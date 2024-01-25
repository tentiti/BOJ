# 1 -> 1
# 2 -> 1 1
# 3 -> 1 1 1
# 4 -> 1 2 1 
# 5 -> 1 2 1 1
# 6 -> 1 2 2 1
# 7 -> 1 2 1 1 1
# 8 -> 1 2 2 2 1
# 9 -> 1 2 3 2 1
# 10 -> 1 2 3 2 1 1

# 1, 2, 3, 3, 4, 4, 5, 5, 5, 6

# 1, 2, 4, 6, 9... -> 숫자가 하나씩 늘어남

# 1, 3, 9, 
# 1 = 1
# 2 = 3
# 3 = 6
# 4 = 9
# 5 = 13
# 6 = 17
# 7 = 22
# 8 = 27

import math

def finder(n):
    k = 1
    while k**2+k < n:
        k += 1 
    if n > k**2:
        print(2*k)
    else:
        print(2*k-1)
    
    # temp = int(math.sqrt(n))
    # if True:
    #     if n < temp**2+temp:
    #         if n <= temp**2: print(2*temp-1)
    #         else: print(2*temp)
    #     else:
    #         temp += 1
    #         if n <= temp**2: print(2*temp-1)
    #         else: print(2*temp)
    # # k = n//2+1
    

for i in range(int(input())):
    a, b = map(int, input().split())
    finder(b -a)
    # for i in range(1, 11):
    #     finder(i)