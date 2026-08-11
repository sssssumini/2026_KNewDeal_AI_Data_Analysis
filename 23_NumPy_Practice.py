import numpy as np

# 실습 1. 센서값 배열 만들기
print("=== 실습 1 : 센서값 배열 만들기 ===")

temp = np.array([18.1, 38.4, 21.4, 22])
# F = (°C × 1.8) + 32
print(f"섭씨 -> 화씨 변환 {temp} -> {temp*1.8+32}")


# 실습 2. 균등 간격 배열 만들기
print("=== 실습 2 : 균등 간격 배열 만들기 ===")

zero_100 = np.linspace(0, 100, 5)
print(zero_100)

gab_Six = np.arange(0, 30, 6)
print(gab_Six)

# 실습 3. 측정 시간축 배열 만들기
print("=== 실습 3 : 측정 시간축 배열 만들기 ===")


gap_time = np.arange(0, 300, 10)
print(gap_time)

dim_2 = np.array(
    [[12, 3, 4, 5, 6], [1, 2, 34, 5, 6], [123, 4, 5, 3, 23], [34, 323, 44, 33, 22]]
)

print()
print(dim_2.ndim)
print(dim_2.shape)


# 실습 4. 배열 구조 확인하기
print("=== 실습 4 : 배열 구조 확인하기 ===")

arr4 = np.array(
    [[12, 3, 4, 5, 6], [1, 2, 34, 5, 6], [123, 4, 5, 3, 23], [34, 323, 44, 33, 22]]
)
print(f"ndim : {arr4.ndim} \nshape : {arr4.shape} \nsize : {arr4.size}")

# 실습 5. 자료형 확인과 변환하기
print("=== 실습 5 : 자료형 확인과 변환하기 ===")
arr5 = np.array([[1.2, 3.4, 23.5], [8, 3.4, 5.6]])
arr5_tranfer = arr5.astype(int)
print(f"원래 \n{arr5} {arr5.dtype}\n바뀌고나서 \n{arr5_tranfer} {arr5_tranfer.dtype}")


# 실습 6. 배열 모양 바꾸기
print("=== 실습 6 : 배열 모양 바꾸기 ===")
arr6 = np.arange(20)
print(arr6)
arr6_reshape = arr6.reshape(4, 5)
print(f"reshape\n {arr6_reshape}")

# 실습 7. 센서 데이터 표로 정리하기
# 시점(행) = 6, 센서(열) = 4
print("=== 실습 7 : 센서 데이터 표로 정리하기 ===")
arr7 = np.arange(24)
arr7_reshape = arr7.reshape(6, 4)
print(arr7_reshape)

# 실습 8. 배열 생성부터 정리까지
print("=== 실습 8 : 배열 생성부터 정리까지 ===")
arr8 = np.array([1, 20, 2, 22.2, 3, 24.2])
print(f"shape : {arr8.shape}, dtype : {arr8.dtype}")
arr8_reshape = arr8.reshape(2, 3)
print(f"변경 후\n{arr8_reshape}\nshape : {arr8_reshape.shape}")


import numpy as np

# 실습 1. 특정 센서·구간 추출하기
print("=== 실습 1. 특정 센서·구간 추출하기 ===")

# 예시 : 회전수 배열
rpm = np.array([1551, 1408, 1498, 1443, 1425, 1558, 2861, 1410])
print(f"첫 시점 : {rpm[0]}\n마지막 시점 : {rpm[-1]}")
print(rpm[::2])

# 실습 2. 행·열 단위로 추출하기
print("=== 실습 2. 행·열 단위로 추출하기 ===")
# 예시: 회전수와 토크 배열
data = np.array([[1151, 42.8], [1408, 46.3], [2861, 4.6], [1410, 65.7]])

print(f"2번째 설비 전체 측정 값 : {data[1]}")
print(f"모든 설비의 회전수 : {data[:,0]}")
print(f"모든 설비의 토크수 : {data[:,1]}")

# 실습 4. 이상 센서값 필터링하기
print("=== 실습 4. 이상 센서값 필터링하기 ===")
rpm = np.array([1503, 1816, 1598, 1897, 1988])
print(rpm[rpm > 1900])

print(rpm[(rpm < 1900) & (rpm > 1600)])

# 실습 5. 조건별 개수와 비율 세기
print("=== 실습 5. 조건별 개수와 비율 세기 ===")

torque = np.array([19.3, 48.9, 39.8, 72.3, 99.3])
high50 = torque > 50
torque_high50 = torque[torque > 50]  # torque>50인 새 배열을 만든다.
print(high50, torque_high50)

high50_len = high50.sum()
print(f"전체에서 토크가 50이 넘는 센서의 개수 : {high50.sum()}개")
print(f"전체에서 토크가 50이 넘는 센서의 비율 : {high50.mean()}%")

# 합계와 평균
s = np.array([29, 45, 87, 76, 75])
print(s.sum())
print(s.mean())
print(np.median(s))  # 중앙값

# 실습 6. 센서별 기초 통계 구하기
print("=== 실습 6. 센서별 기초 통계 구하기 === ")

data6 = np.array(([[1552, 43.8], [3948, 38.4], [1448, 40.2], [1735, 39.1]]))

print(f"열 별 평균 {data6.mean(axis=0)}")
print(f"열 별 표준편차 {np.round(data6.std(axis=0),2)}")


# 실습 7. 파일데이터로 기초 통계 구하기
"""
실습 7. 파일 데이터로 기초 통계 구하기
목표
파일로 저장된 공정 데이터를 불러와 기초 통계 계산
단계
· np.loadtxt로 회전수 열을 파일에서 불러오기
· 불러온 배열의 평균과 표준편차 계산
· 최솟값과 최댓값으로 값의 범위 확인
예상 결과
회전수의 평균·표준편차와 최솟값·최댓값이 출력
"""
print("=== 실습 7. 파일데이터로 기초 통계 구하기 === ")

rpm7 = np.loadtxt(
    "data/10_mct_tool.csv", delimiter=",", skiprows=1, usecols=4, encoding="utf-8"
)
# usecols = 몇번째 열을 불러올 건지
print(round(rpm7.mean(), 1))
print(rpm7.max() - rpm.min())

# 실습 8. 필터링과 통계 결합하기
print("=== 실습 8. 필터링과 통계 결합하기 === ")
torque8 = np.array([49.4, 56.4, 63.2, 40.3, 44.6])

high8 = torque8[torque8 > 50]
print(high8)
print(f"50 이상인 값들의 평균 {high8.mean()} / 개수 : {high8.size}")

# 실습 9. NumPy 기초 종합 분석
print("=== 실습 9. NumPy 기초 종합 분석 === ")

sensor = np.loadtxt(
    "data/10_mct_tool.csv", delimiter=",", skiprows=1, usecols=(4, 5), encoding="utf-8"
)

print(sensor.shape, sensor.dtype)
rpm9 = sensor[:, 0]
print(rpm9)
rpm_under = rpm9[rpm9 < 3000]
print(rpm_under)
print(f"기준 아래로 떨어진 시점 개수 : {rpm_under.size}, 평균 : {rpm_under.mean()}")
