for i in range(int(input())):
    ans = 1.00
    nums = list(map(str, input().split()))
    for num in nums:
        ans *= float('0'+num)
    print("${:.2f}".format(round(ans,2)))