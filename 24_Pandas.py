import pandas as pd
import os

pd.set_option("display.unicode.east_asian_width", True)


filepath = os.path.join("data", "12_metro_small.csv")
df = pd.read_csv(
    filepath,
    encoding="utf-8",
    nrows=10,
    index_col="측정시각",
    usecols=["측정시각", "가동상태"],
)
print(df.shape)
print(df.head(3))

# 실습 2. 설비 센서 CSV 불러오기
print("=== 실습 2. 설비 센서 CSV 불러오기 ===")
filepath2 = os.path.join("data", "12_metro_compressor.csv")

df2 = pd.read_csv(filepath2, encoding="utf-8", sep=",")
print(df2.head(10))
print(df2.shape)  # 200행 7열

# 실습 3. 한글, 구분자 깨짐 옵션 다루기
print("\n=== 실습 3. 한글, 구분자 깨짐 옵션 다루기 ===")
filepath2 = os.path.join("data", "12_metro_compressor.csv")

df3 = pd.read_csv(filepath2, encoding="utf-8", sep=",")
print(df3.head(3))

# 실습 4. 필요한 열만 골라 불러오기
print("\n=== 실습 4. 필요한 열만 골라 불러오기  ===")
filepath2 = os.path.join("data", "12_metro_compressor.csv")

df4 = pd.read_csv(
    filepath2,
    encoding="utf-8",
    sep=",",
    usecols=["측정시각", "압축압력", "배출압력", "저장압력"],
)
print(df4.shape)
print(df4.head(3))


# # 실습 5. 경로·옵션 오류 고치기
# print("\n=== 실습 5. 경로·옵션 오류 고치기 ===")
# df5 = pd.read_csv("없는파일.csv")
# print(df5.shape)

# # FileNotFoundError: [Errno 2] No such file or directory: '없는파일.csv'

# 실습 6. read_csv 옵션 종합 연습
print("\n=== 실습 6. read_csv 옵션 종합 연습 ===")
filepath6 = os.path.join("data", "12_metro_compressor_semicolon.csv")
df6 = pd.read_csv(
    filepath6,
    sep=";",
    encoding="utf-8",
    usecols=["측정시각", "오일온도", "모터전류"],
    nrows=50,
)
print(df6.shape)
print(df6.head(3))


# 실습 1. head, tail로 디지털 신호 살펴보기

pd.set_option("display.unicode.east_asian_width", True)

print("\n=== 실습 1. head, tail로 디지털 신호 살펴보기 ===")
filepath1 = os.path.join("data", "12_metro_digital.csv")
df1 = pd.read_csv(filepath1, encoding="utf-8", sep=",")
print(df1.head())
print(df1.tail())

# 실습 2. head, tail 행 개수 조절
print("\n=== 실습 2. head, tail 행 개수 조절  ===")
filepath2 = os.path.join("data", "12_metro_compressor.csv")
df2 = pd.read_csv(filepath2, encoding="utf-8", sep=",")
print(df2.head(1))
print(df2.head(10))
print(df2.tail(7))
print(df2.head(500))

# 실습 3. 구조 파악 3종 도구
print("\n=== 실습 3. 구조 파악 3종 도구  ===")
filepath3 = os.path.join("data", "12_metro_digital.csv")
df3 = pd.read_csv(filepath3, encoding="utf-8", sep=",")

print(
    f"12_metro_digital.csv 데이터프레임은 {df3.shape}으로 구성되어있고 \n컬럼명\n{df3.columns}\n{df3.columns.tolist}()\n데이터프레임 구조\n{df3.dtypes}"
)

# 실습 4. 열 이름 자료형 점검
print("\n=== 실습 4. 열 이름 자료형 점검 ===")
filepath4 = os.path.join("data", "12_metro_compressor.csv")
df4 = pd.read_csv(filepath4, encoding="utf-8", sep=",")

print(
    f"12_metro_compressor.csv 데이터프레임은 {df4.shape}으로 구성되어있고 \n컬럼명\n{df4.columns}\n{df4.columns.tolist()}\n데이터프레임 구조\n{df4.dtypes}"
)

# 실습 5. info로 데이터 건강검진

print("\n=== 실습 5. info로 데이터 건강검진 ===")
filepath5 = os.path.join("data", "12_metro_digital.csv")
df5 = pd.read_csv(filepath5, encoding="utf-8", sep=",")
df5.info() # print안에 넣지 말 것 ! 


# 실습 6. describe로 이상 신호 찾기
print("\n=== 실습 6. describe로 이상 신호 찾기 ===")
filepath6 = os.path.join("data", "12_metro_compressor.csv")
df6 = pd.read_csv(filepath6, encoding="utf-8", sep=",")

print(df6.describe())

# 결과해석
# === 실습 6. describe로 이상 신호 찾기 ===
#            압축압력      배출압력      저장압력      오일온도      모터전류
# count  200.000000  200.000000  200.000000  199.000000  200.000000
# mean     9.172200   -0.016950    9.171400   63.181910    2.060850
# std      0.583699    0.047173    0.582497    6.249822    2.196505
# min      8.130000   -0.030000    8.130000   50.100000    0.030000
# 25%      8.700000   -0.020000    8.697500   58.100000    0.040000
# 50%      9.175000   -0.020000    9.175000   62.900000    0.040000
# 75%      9.665000   -0.020000    9.655000   68.100000    3.812500
# max     10.220000    0.600000   10.220000   75.000000    6.190000
# -------------------------------------------------------------
# 1 온도의 평균과 최댓값 차이를 숫자로 적었는가
# 평균 : 63.181910 / 최댓값 : 75
# 2 75%와 max 차이가 큰 열을 두 개 이상 찾았는가
# 오일온도와 모터전류 
# 3 모터전류처럼 고른 열과 비교해 차이를 설명
# 모터전류에 비해 압축압력, 배출압력, 저장압력의 표준편차가 작아 세 값들이 더욱 중앙에 몰려있을 것이다
# -------------------------------------------------------------

# 실습 7. 통계량 문장으로 묘사 
print("\n=== 실습 7. describe로 이상 신호 찾기 ===")
filepath7 = os.path.join("data", "12_metro_compressor.csv")
df7 = pd.read_csv(filepath7, encoding="utf-8", sep=",")
df7.info
print(df7["오일온도"].describe())

# 결과해석
# === 실습 7. describe로 이상 신호 찾기 ===
# count    199.000000
# mean      63.181910
# std        6.249822
# min       50.100000
# 25%       58.100000
# 50%       62.900000
# 75%       68.100000
# max       75.000000
# -------------------------------------------------------------
# 평균·min·max·중앙값을 문장에 정확히 넣었는가
# 이 값은 보통 62.9 정도이고, 가장 낮을 때 50.1, 높을 때 75 float 형식
# 2 표준편차를 보고 안정성을 판단했는가
# 표준편차가 6보다 크기 때문에 그렇게 안정성 있다고 말 할 수는 없다.
# 3 숫자를 그냥 옮기지 않고 의미로 풀어 썼는가
# 네
# -------------------------------------------------------------

# 실습 8. 압축기와 디지털 신호 구조 비교
print("\n=== 실습 8. 압축기와 디지털 신호 구조 비교 ===")
df_metro_compressor_path = os.path.join("data", "12_metro_compressor.csv")
df_metro_digital_path = os.path.join("data", "12_metro_digital.csv")
df_metro_compressor = pd.read_csv(df_metro_compressor_path, encoding="utf-8", sep=",")
df_metro_digital = pd.read_csv(df_metro_digital_path, encoding="utf-8", sep=",")

print("12_metro_compressor.csv")
print(df_metro_compressor.shape)
print(df_metro_compressor.describe())
df_metro_compressor.info()

print("12_metro_digital.csv")
print(df_metro_digital.shape)
print(df_metro_digital.describe())
df_metro_digital.info()

# 결과해석 
# === 실습 8. 압축기와 디지털 신호 구조 비교 ===
# 12_metro_compressor.csv
# (200, 7)
#          압축압력    배출압력    저장압력    오일온도    모터전류
# count  200.000000  200.000000  200.000000  199.000000  200.000000
# mean     9.172200   -0.016950    9.171400   63.181910    2.060850
# std      0.583699    0.047173    0.582497    6.249822    2.196505
# min      8.130000   -0.030000    8.130000   50.100000    0.030000
# 25%      8.700000   -0.020000    8.697500   58.100000    0.040000
# 50%      9.175000   -0.020000    9.175000   62.900000    0.040000
# 75%      9.665000   -0.020000    9.655000   68.100000    3.812500
# max     10.220000    0.600000   10.220000   75.000000    6.190000
# <class 'pandas.DataFrame'>
# RangeIndex: 200 entries, 0 to 199
# Data columns (total 7 columns):
#  #   Column  Non-Null Count  Dtype  
# ---  ------  --------------  -----  
#  0   측정시각    200 non-null    str    
#  1   압축압력    200 non-null    float64
#  2   배출압력    200 non-null    float64
#  3   저장압력    200 non-null    float64
#  4   오일온도    199 non-null    float64
#  5   모터전류    200 non-null    float64
#  6   가동상태    200 non-null    str    
# dtypes: float64(5), str(2)
# memory usage: 11.1 KB
# 12_metro_digital.csv
# (120, 4)
#            압축기        타워  저압스위치
# count  120.000000  120.000000       120.0
# mean     0.908333    0.933333         0.0
# std      0.289765    0.250490         0.0
# min      0.000000    0.000000         0.0
# 25%      1.000000    1.000000         0.0
# 50%      1.000000    1.000000         0.0
# 75%      1.000000    1.000000         0.0
# max      1.000000    1.000000         0.0
# <class 'pandas.DataFrame'>
# RangeIndex: 120 entries, 0 to 119
# Data columns (total 4 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   측정시각    120 non-null    str  
#  1   압축기     120 non-null    int64
#  2   타워      120 non-null    int64
#  3   저압스위치   120 non-null    int64
# dtypes: int64(3), str(1)
# memory usage: 3.9 KB
# -------------------------------------------------------------
# 1 변수를 df_metro_compressor, df_metro_digital으로 구분했는가
# 넹
# 데이터에 결측값이 없어서 유의미한 결과를 도출해내지 못함
# -------------------------------------------------------------

# 실습 9. 첫 탐색 종합
print("\n=== 실습 9. 첫 탐색 종합 ===")
df_metro_small_path = os.path.join("data", "12_metro_small.csv")
df_metro_small = pd.read_csv(df_metro_small_path, encoding="utf-8", sep=",")


print("종합 실습 리포트")
print("(1) metro_small head(3)")
print(df_metro_small.head(3))
print("(2) metro_small shape")
print(df_metro_small.shape)
print("(3) metro_small columns 이름")
print(df_metro_small.columns)
print("(4) metro_small dtypes")
print(df_metro_small.dtypes)
print("(5) metro_small info")
df_metro_small.info()

print("(6) metro_small describe")
print(df_metro_small.describe())

print("-"*50)
print("metro_small.csv 데이터는 30행 7열로 구성된 데이터프레임")
print("각 컬럼 별 결측값이 없어서 바로 분석 가능하다.")
print("압축압력, 배출압력, 저장압력, 오일온도, 모터전류의 컬럼이 수치화 되어있으며 모터전류 이외에는 최댓값이 이상치로 의심되는 값이 없다.")

