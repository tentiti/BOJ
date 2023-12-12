current = set()
for i in range(int(input())):
    command = input().split()
    if command[1] == 'enter':
        current.add(command[0])
    elif command[1] == 'leave':
        current.discard(command[0])
        
current = sorted(list(current), reverse=True)
# print(current)

for _ in current:
    print(_)