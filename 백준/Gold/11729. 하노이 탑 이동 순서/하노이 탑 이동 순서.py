#하노이탑

n = int(input()) #1에 n개의 원판이 있음.

towers = [[i for i in range(n+1, 0, -1)], [], []]
ans = 0
movement = []

def move(n, f, t):
    global movement
    # print(f, t)
    movement.append([f, t])

def hanoi(n, f, t, v):
    global ans
    ans += 1
    if n == 1:
        move(n, f, t)
        return
    else:
        hanoi(n-1, f, v, t) #3개 옮기는 건, 줄이면, 2개를 a => b using c
        move(1, f, t) #base 1을 a => c
        hanoi(n-1, v, t, f) #2개를 b => c using a

hanoi(n, 1, 3, 2)
print(len(movement))
for mv in movement:
    print(*mv, sep=' ')

#hanoi 1 = 1
#hanoi 2 = 3
#hanoi 3 = 7 (3 + 3 + 1)
#hanoi 4