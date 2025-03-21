def solution(s1):
    answer = True
    
    tokens = []
    
    for s in s1:
        if s == '(':
            tokens.append(s)
        elif s == ')':
            if tokens:
                tokens.pop()
            else:
                return False

    return len(tokens) == 0