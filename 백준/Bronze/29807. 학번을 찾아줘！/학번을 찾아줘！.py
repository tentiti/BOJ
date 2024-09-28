subCount = int(input())  # 응시한 과목 수
scores = list(map(int, input().split()))  # 과목별 점수 리스트

# 각 과목별 점수를 기본값 0으로 설정하고, 입력받은 점수로 갱신
k, m, e, s, l = 0, 0, 0, 0, 0

# 주어진 응시 과목 수에 따라 점수 할당
if subCount >= 1:
    k = scores[0]  # 국어 점수
if subCount >= 2:
    m = scores[1]  # 수학 점수
if subCount >= 3:
    e = scores[2]  # 영어 점수
if subCount >= 4:
    s = scores[3]  # 탐구 점수
if subCount == 5:
    l = scores[4]  # 제2외국어 점수

# 초기 결과값
res = 0

# 국어와 영어 비교
if k > e:
    res += (k - e) * 508
else:
    res += (e - k) * 108

# 수학과 탐구 비교
if m > s:
    res += (m - s) * 212
else:
    res += (s - m) * 305

# 제2외국어 점수 계산 (제2외국어를 응시한 경우만)
res += l * 707

# 최종 결과에 우편번호 4763을 곱함
print(res * 4763)
