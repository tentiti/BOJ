consonants=['a','e','i','o','u']
res = 0
word = input()
for letter in word:
    if letter in consonants:
        res+=1
print(res)