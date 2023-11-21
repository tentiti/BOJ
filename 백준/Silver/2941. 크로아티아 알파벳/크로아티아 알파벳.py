croatianLetter = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj','s=','z=']
word = input()
sum = 0
for a in croatianLetter:
    sum += word.count(a)
    word = word.replace(a, '_')
word = word.replace('_', '')
sum += len(word)
print(sum)