#1181 단어 정렬
#1011 수요일

words = []
length = int(input())
for i in range(length):
  words.append(input())
words = set(words)
words = list(words)
words = sorted(words, key= lambda x: (len(x), x)) #길이가 짧은 것 부터, 
for word in words:
  print(word)