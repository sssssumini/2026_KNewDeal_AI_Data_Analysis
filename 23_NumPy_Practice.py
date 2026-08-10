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



# 실습 1. 특정 센서·구간 추출하기
print("=== 실습 1. 특정 센서·구간 추출하기 ===")

# 예시 : 회전수 배열
rpm = np.array([1551, 1408, 1498, 1443, 1425, 1558, 2861, 1410])
print(f"첫 시점 : {rpm[0]}\n마지막 시점 : {rpm[-1]}")
print(rpm[::2])

# 실습 2. 행·열 단위로 추출하기
import numpy as np

# 예시: 회전수와 토크 배열
data = np.array([
    [1151, 42.8],
    [1408, 46.3],
    [2861, 4.6],
    [1410, 65.7]
])

print(f"2번째 설비 전체 측정 값 : {data[1]}")
print(f"모든 설비의 회전수 : {data[:,0]}")
print(f"모든 설비의 토크수 : {data[:,1]}")