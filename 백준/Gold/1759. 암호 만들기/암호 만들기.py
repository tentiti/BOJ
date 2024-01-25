from itertools import combinations
l, c = map(int, input().split())
words = sorted(list(input().split()))
perms = (combinations(words, l))
vowels = {'a', 'e', 'i', 'o', 'u'}

for _ in perms:
    temp = set(_)
    if temp&vowels and len(temp - vowels) >= 2:
        print(''.join(_))