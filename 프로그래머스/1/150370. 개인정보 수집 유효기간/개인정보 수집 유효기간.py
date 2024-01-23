def solution(today, terms, privacies):
    answer = []
    todayDate = list(map(int, today.split('.')))
    termDate = {}
    for term in terms:
        kind = term.split()[0]
        month = int(term.split()[1])
        termDate[kind]=month
    for i in range(len(privacies)):
        temp = privacies[i].split()
        dates = list(map(int, temp[0].split('.')))
        dateElapsed = (todayDate[0]-dates[0])*12*28+(todayDate[1]-dates[1])*28+(todayDate[2]-dates[2])
        if dateElapsed >= termDate[temp[1]]*28:
            answer.append(i+1)
    return answer