word = input()
size = len(word)

#palTable[a][b] == is word[a:b]기 회문?
palTable = [[0 for i in range(size)] for i in range(size)]

#한글자 짜리 => 다 회문 맞음
for i in range(size):
    palTable[i][i] = 1
    if i >= 1 and word[i-1] == word[i]:
        #두글자 짜리 => 같으면 회문
        palTable[i-1][i] = 1

#몇개의 회문이 나오나요?
for l in range(3, size+1): #3글자~단어길이 크기의 부분문자열 회문여부 확인 
    for j in range(size-l+1): #시작점 달라짐 => 이러면, 다음에 사이즈 늘어나도 처음, 끝만 계산하면 됨
        if word[j] == word[j+l-1] and palTable[j+1][j+l-2]: #시작, 끝 같고 사이가 회문이면, 회문이다.
            palTable[j][j+l-1] = 1

# print(*palTable, sep="\n")

# print('done')

dp = [float('inf') for i in range(size+1)]
dp[0] = 0
dp[1] = 1

for i in range(size): #시작점
    dp[i+1] = min(dp[i+1], dp[i]+1) 
    #내가 이미 건드려졌다면 몰라, 아니라면 걍 한글자 + 1
    for j in range(i+1, size): #나한테서 갈 수 있는 부분문자열 확인
        if palTable[i][j]: #만약 회문이라면
            # print(i, j, 'found')
            dp[j+1] = min(dp[i]+1, dp[j+1]) #+1 아니면 원래 값 중 작은 것
    # print(*dp, sep="-") 

print(dp[-1])