formula = list(input())
stack = []
temp=''

for i in formula:
    # print(i)
    if not i.isalpha():
        if i ==')': #오른쪽 괄호라면
            while stack and stack[-1] != '(': #왼쪽 괄호 나올때까지 뽑기
                temp = stack.pop()
                print(temp, end='')
            stack.pop()
        elif i =='(':
            stack.append(i)
        elif i == '*' or i =='/':
            while stack and (stack[-1] == '/' or stack[-1] == '*'):
                temp = stack.pop()
                print(temp, end='')
            stack.append(i)
        elif i == '+' or i =='-':
            while stack and (stack[-1] != '('):
                temp = stack.pop()
                print(temp, end='')
            stack.append(i)
    else: #알파벳 문서라면?
        print(i, end='')

while stack:
    print(stack.pop(), end='')