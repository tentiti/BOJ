message = list(map(int,input()))
message.sort(reverse=True)
print(*message, sep='')