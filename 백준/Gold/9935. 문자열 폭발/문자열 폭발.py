from collections import deque

text = input()
bomb = input()

stack = []

for i in range(len(text)):
    stack.append(text[i])
    if text[i]==bomb[-1] and ''.join(stack[-len(bomb):]) == bomb:
        for j in range(len(bomb)):
            stack.pop()

if not len(stack):
    print('FRULA')
else:
    print(''.join(stack))