words =  []
for i in range(5):
    words.append(input())
# print(words)
# print(len(word) for word in words)
for i in range(max(len(item) for item in words)):
    for word in words:
        if len(word) > i:
            print(word[i],end='')
