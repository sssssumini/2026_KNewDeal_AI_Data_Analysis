# 파이썬에서 기본 제공하는 기능들 외에
# 다양한 외부 라이브러리들을 가져오려면
# pypi.org 사이트에서 검색

# 터미널에서 바로 pip로 설치를 시도하면 (pip install numpy)
# 전체 시스템에 영향을 주는 설치로 생각되어 거절당한다
# 그래서 개별 Working Directory마다 별도의 환경을 구축해
# 그 안에 개별 프로젝트가 사용할 pip 라이브러리들을 따로 받아 쓰게 한다
# 이것이 바로 가상환경(venv)

# 1. 현재 경로에 가상환경 생성 >> conda acivate ( 이름 )

# 2 가상환경 활성화

# (이후에는 가상환경 안에서 터미널 명령 실행 가능, 예 pip install numpy)
# 3. (작업/실행 끝나고) 가상환경 종료 >> conda deactivate

import numpy as np

numbers = [1, 2, 3, 4, 5]
np_numbers = np.array(numbers)
print(np_numbers)

temp = np.array([70.5, 69.8, 73.7])
print(temp)

# 배열의 항목들마다 5를 더하려면
print(temp + 5)

# 미국식 속도(miles)를 우리가 쓰는 속도(km/h)로 변환시켜주는 예제

miles = np.array([94.7, 104.5, 105.5])
# 속도(km/h) = 속도(mph) x 1.60934
print(miles * 1.60934)

# 실습 1. 센서값 배열 만들기
temp = np.array([18.1, 38.4, 21.4, 22])
# F = (°C × 1.8) + 32
print(f"섭씨 -> 화씨 변환 {temp} -> {temp*1.8+32}")


# linspace
div_five = np.linspace(0, 1, 5)
print(div_five)

# 0으로 채우기
block_zeros = np.zeros(5)
print(block_zeros)

# 7로 채우기
block_seven = np.full(4, 7)
print(block_seven)

# 실습 2. 균등 간격 배열 만들기
zero_100 = np.linspace(0, 100, 5)
print(zero_100)

gab_Six = np.arange(0, 30, 6)
print(gab_Six)

# 실습 3. 측정 시간축 배열 만들기
gap_time = np.arange(0, 300, 10)
print(gap_time)

dim_2 = np.array(
    [[12, 3, 4, 5, 6], [1, 2, 34, 5, 6], [123, 4, 5, 3, 23], [34, 323, 44, 33, 22]]
)

print(dim_2.ndim)
print(dim_2.shape)

# 형변환
convertable = np.array([3.14, 6.7, 1.23])
print(convertable.dtype)
converted = convertable.astype(int)
print(converted)
print(converted.dtype)

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


# reshape
arr4_reshape = arr4.reshape(5, 4)  # 5행 4열로 변함
print(arr4_reshape)

# flatten
arr4_flatten = arr4.flatten()
print(arr4_flatten)

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


# 배열 인덱싱
test = np.array([80, 39, 23, 44, 22])
print(test[2])
print(test[-1])
print(test[1:4])

# 2차원 배열 인덱싱
two_dim_arr = np.array([[30, 3.4], [20, 33.4], [33, 9.8]])

print(two_dim_arr[0][1])
print(two_dim_arr[0, 1])
 
print(two_dim_arr[0]) # 행 추출
print(two_dim_arr[:,1]) # 열 추출
