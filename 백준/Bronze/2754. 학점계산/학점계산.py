letter = input()

if letter == "F":
    grade = 0.0
else:
    grade = 69-ord(letter[0])
    if letter[1] == "+":
        grade += 0.3
    elif letter[1] == "-":
        grade -= 0.3
    else:
        grade += 0.0
        
print((grade))