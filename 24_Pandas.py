import pandas as pd
import os

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
    f"12_metro_digital.csv 데이터프레임은 {df3.shape}으로 구성되어있고 \n컬럼명\n{df3.columns}\n{df3.columns.tolist}\n데이터프레임 구조\n{df3.dtypes}"
)

# 실습 4. 열 이름 자료형 점검
print("\n=== 실습 4. 열 이름 자료형 점검 ===")
filepath4 = os.path.join("data", "12_metro_compressor.csv")
df4 = pd.read_csv(filepath4, encoding="utf-8", sep=",")

print(
    f"12_metro_compressor.csv 데이터프레임은 {df4.shape}으로 구성되어있고 \n컬럼명\n{df4.columns}\n{df4.columns.tolist}\n데이터프레임 구조\n{df4.dtypes}"
)

# 실습 5. info로 데이터 건강검진

print("\n=== 실습 5. info로 데이터 건강검진 ===")
filepath5 = os.path.join("data", "12_metro_digital.csv")
df5 = pd.read_csv(filepath5, encoding="utf-8", sep=",")
print(df5.info())
