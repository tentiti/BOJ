while True:
    try:
        sentence = input()
        parents = []
        if sentence == '.': break
        isBalanced = True
        sk = 0
        dk = 0
        #이렇게는 너무 간단한데, 안에서 끝나야 한다
        for _ in sentence:
            if _ == '(':
                parents.append('(')
                sk += 1
            elif _ ==')':
                result = parents.pop()
                if result != '(':
                    isBalanced = False
                    break
                sk -= 1
            elif _ =='[':
                parents.append('[')
                dk += 1
            elif _ == ']':            
                result = parents.pop()
                if result != '[':
                    isBalanced = False
                    break
                dk -= 1
            if sk <0 or dk <0:
                isBalanced = False
                break
        if sk != 0 or dk != 0:
            isBalanced = False
        if(isBalanced): print('yes')
        else:print('no')
    except:
        print("no")
        continue