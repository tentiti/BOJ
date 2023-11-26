formula = input()

#기호가 없는 숫자들
calc_numbers = formula.replace('-',"+").split('+')
#signs[n] -> n번째 숫자 앞에 붙는 기호
signs = [0]*len(calc_numbers)

    
numbers = ['0', '1', '2', '3', '4', '5', '6', '7','8', '9']

if formula[0] == '-':
    signs[0] = -1
else:
    signs[0] = 1
signLocator = 1
#기호 읽기
for i in range(len(formula)):
    #기호가 나왔을 때
    if formula[i] not in numbers:
        #기본 처리
        if formula[i] == '-':
            signs[signLocator] = -1
        else:
            signs[signLocator] = 1
        signLocator += 1

#두뇌풀가동!
for i in range(1, len(signs)):
    #저번 것 마이너스, 이번 것 마이너스 -> 그냥 알아서 가면 됨.
    #저번 것 플러스, 이번 것 마이너스 -> 그냥 알아서 가면 됨.
    #저번 것 마이너스, 이번 것 플러스 -> 마이너스에 얹혀가기
    #저번 것 플러스, 이번 것 플러스 -> 할 수 있는게 없음
    if signs[i-1] == -1 and signs[i] == 1:
        signs[i] = -1

signLocator = 0
for i in range(len(signs)):
    signLocator += signs[i] * int(calc_numbers[i])

# print(signs)
# print(calc_numbers)
print(signLocator)

        