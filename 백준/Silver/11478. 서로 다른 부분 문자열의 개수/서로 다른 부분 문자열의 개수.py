subSequences = []

s = input()

for i in range(len(s)+1):
    for j in range(i+1, len(s)+1):
        subSequences.append(s[i:j])
# print(subSequences)
subSequences = set(subSequences)
print(len(subSequences))