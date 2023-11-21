grades = []
for i in range(20):
    report = input().split()
    if report[2] == 'F':
        grades.append([float(report[1]), 0.0])
    elif report[2] == 'P':
        continue
    else:
        if report[2][1] == '0':
            tempGrade = 0.0
        elif report[2][1] == '+':
            tempGrade = 0.5
        tempGrade += 69-ord(report[2][0])
        grades.append([float(report[1]), tempGrade])

gpa = 0.0
credit = 0
for _ in grades:
    gpa += _[0] * _[1]
    credit += _[0]

print(gpa/credit)