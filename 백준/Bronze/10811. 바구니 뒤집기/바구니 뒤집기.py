n, m = map(int, input().split())
arr = [i+1 for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    temp = arr[a-1:b]
    arr = arr[:a-1]+temp[::-1]+arr[b:]
    # print(arr[:a-1], temp[::-1], arr[b:])
    # print(arr[:a-1]+temp[::-1]+arr[b:])
    
    # arr = arr[:a-1] + arr[b:a] + arr[b:]
    # print(arr)
    
print(*arr, sep=' ')