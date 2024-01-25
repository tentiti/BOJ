import math
#두 자연수 a, b,가 주어졌을때 a부터 b까지의 2진수의 1의 개수의 합

a, b = map(int, input().split())


#sum(a-1) 구하고 sum(b) 구해서 빼는게 빠를듯...
#뭔가 logn 분할정복 요함.

#f: 1의개수
#sum: 1의 개수 누적합

#f(2^n) = 1, 이건 항상 반복됨, 그 밑에것들도 반복됨.
#f(2^n-1) = n-1개 (f(7) = 111)

# sum(2^n-1): 2*sum(2^(n-1)-1)+2^n
# 7까지의 합은, 3까지의 합 *2 + 4567 해서 첫 비트 1이니까 4!!

# 그렇다면 8까지의 합은? 7까지의 합 + 1
# 그렇다면 26까지의 합은? 16까지의 합 + 1~10까지의 합 + 10

#그럼 그냥 2의 거듭제곱 해서 구해두면 되겠군

powerTable = [0 for i in range(int(math.log(10**16, 2))+2)]
for i in range(1, int(math.log(10**16, 2))+1):
    powerTable[i] = (2*powerTable[i-1]+2**(i-1))

# print(powerTable)
#powerTable[n] = 2**n-1까지의 누적합.

def bitSum(n):
    if not n: return 0;
    num = n
    ans = 0
    while num > 0:
        minSquare = int(math.log(num, 2)) #가장 큰 제곱근 찾기
        # print(minSquare)
        ans += powerTable[minSquare] #그 거듭제곱-1까지의 합 더하고
        ans += 1 #그 거듭제곱의 해당하는 개수(1)더하고
        ans += num-2**(minSquare) #그 거듭제곱을 뺀 나머지의 첫 1 개수 더하고
        num -= 2**(minSquare) #그 거듭제곱 뺀 수만큼 남은것 계산
    return ans

# print(bitSum(2))

# for i in range(10):
    # print(i, bitSum(i))

# print(bitSum(10**16)-bitSum(0))
# print(bitSum(2*4)-bitSum(1))

print(bitSum(b)-bitSum(a-1))
# print(bitSum(8)-bitSum(4))

#1, 1 => 1 => 1
#1, 2 => 1, 10 => 2
#1, 3 => 1, 10, 11 => 4
#1, 4 => 001, 010, 011, 100 => 5
#1, 5 => 1, 10, 11, 100, 101 => 7
#1, 6 => 1, 10, 11, 101, 101, 110 => 9
#1, 7 => 1, 10, 11, 101, 101, 110, 111=> 12
#1, 8 => 1, 10, 11, 101, 101, 110, 111, 1000=> 13

