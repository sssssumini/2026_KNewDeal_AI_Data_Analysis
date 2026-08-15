import pandas as pd
import os

pd.set_option("display.unicode.east_asian_width", True)

df = pd.read_csv("data/13_diecasting_small.csv")
df.info()

df["형체력"].info()  # Series
df[["형체력", "실린더압력"]].info()  # DataFrame

# 실습 1. 데이터 불러오기와 구조 확인하기
print("\n=== 실습 1. 데이터 불러오기와 구조 확인하기 ===")
filepath1 = os.path.join("data", "13_diecasting_small.csv")
df1 = pd.read_csv(filepath1, encoding="utf-8", sep=",")
print(df1.shape)
print(df1.columns)
print(df1.head(5))

# 실습 2. 열 선택하기
print("\n=== 실습 2. 열 선택하기 ===")
print(df1["형체력"])

print(df1[["형체력", "실린더압력"]])

print(round(df1[["형체력"]].mean(), 1))


# 목표
# 한 열(Series)과 여러 열(DataFrame)을 선택하고 바로 계산
# 단계
# · 대괄호 한 겹으로 단일 열을 Series로 선택 "형체력"
# · 대괄호 두 겹으로 복수 열을 DataFrame으로 선택 "형체력", "실린더압력"
# · 선택한 열에 mean으로 평균 계산
# 예상 결과
# Series·DataFrame 형태와 형체력 평균 출력

# print(df1.shape)
# print(df1.columns)
# print(df1.head(5))

# 실습 3. 공정 센서 열 골라내기
print("\n=== 실습 3. 공정 센서 열 골라내기 ===")
# · 주조 로그 파일 불러오기 data/13_diecasting_shot.csv

filepath3 = os.path.join("data", "13_diecasting_shot.csv")
df3 = pd.read_csv(filepath3, encoding="utf-8", sep=",")

# · 한 센서 열을 Series로 선택 "형체력"
print(df3["형체력"])

# · 여러 feature 열을 DataFrame으로 선택해 형태 확인 "형체력, 실린더압력, 주조압력"
print(df3[["형체력", "실린더압력", "주조압력"]].shape)


df_sub2 = df3.loc[0:2, ["품질등급", "형체력"]]  # loc은 0:2 인 경우 0,1,2번째 행 다 출력
print(df_sub2)

# 실습 4. loc와 iloc로 행 선택하기
print("\n=== 실습 4. loc와 iloc로 행 선택하기 ===")
filepath4 = os.path.join("data", "13_diecasting_small.csv")
df4 = pd.read_csv(filepath4, encoding="utf-8", sep=",")

df4_sub1 = df4.loc[0, "품질등급"]
print(df4_sub1)

# iloc : 특정 row의 Series 추출
# iloc로 행을 골라서 [품질등급]이라는 열 내용추출
df4_sub2 = df4.iloc[0]["품질등급"]
print(df4_sub2)

print("loc와 iloc의 범위 차이 확인")
print(f"{df4.loc[0:2]} >>>> {len(df4.loc[0:2])}개의 행")
print(f"{df4.iloc[0:2]} >>>> {len(df4.iloc[0:2])}개의 행")

# 실습 5. loc·iloc로 행·열 동시 선택하기
print("\n=== 실습 5. loc·iloc로 행·열 동시 선택하기 ===")
df5_sub1 = df4.loc[0:4, ["품질등급", "형체력"]]
print(df5_sub1)
print(df5_sub1.shape)

df5_sub2 = df4.loc[10:13, ["사이클타임", "비스킷두께"]]
print(df5_sub2)
print(df5_sub2.shape)

print("마지막행")
print(df4.iloc[-3:])

# 실습 6. 특정 구간 추출 종합
print("\n=== 실습 6. 특정 구간 추출 종합 ===")
df_shot = pd.read_csv("data/13_diecasting_shot.csv")

# cols = list(df_shot.columns) >> 열 컬럼 명을 한번에 리스트로 받아올 수 있음

col2 = ["비스킷두께", "형체력"]
print(
    df_shot[col2].loc[0:10].shape
)  # df_shot의 col2에 해당하는 열 중 loc[0:10] 즉 0~10번의 행을 추출
print(df_shot.loc[0:10, col2].shape)  # 위의 내용과 같은 내용
# loc는 열 범위값에 리스트, 즉 열 이름값이 들어가도 됨.

cols = ["실린더압력", "주조압력", "사이클타임", "비스킷두께", "형체력"]
print(
    df_shot[cols].iloc[0:10].shape
)  # df_shot의 cols의 해당하는 열 중 iloc[0:10] 즉 0~9번의 행을 추출


print(
    df_shot.iloc[0:10, 0:3].shape
)  # iloc을 활용해서 특정 구간을 추출하고 싶으면 [행 범위, 열 범위] 쉼표로 구분

# Boolean Series 코드
s_boolean = df_shot["실린더압력"] > 210
print(s_boolean)

# 실습 1. 단일 조건으로 행 추출하기
print("\n=== 실습 1. 단일 조건으로 행 추출하기 ===")

df = pd.read_csv("data/13_diecasting_small.csv")
df.info()
s_boolean_1 = df["실린더압력"] > 230
print(s_boolean_1.sum())

# 특정 컬럼에 대한 조건에 맞는 행만 추출
df_sub = df[df["실린더압력"] > 230]
df_sub.info()
print(df_sub.head())

# 실습 2. 임계값 넘는 설비 골라내기
print("\n=== 실습 2. 임계값 넘는 설비 골라내기 ===")
df_sub_bis = df[df["비스킷두께"] >= 16]
df_sub_bis.info()
print(len(df_sub_bis))
print(df_sub_bis.loc[:, ["샷", "비스킷두께"]])

# 실습 3. 두 조건 묶기
print("\n=== 실습 3. 두 조건 묶기 ===")
df_sub_3 = df[(df["비스킷두께"] >= 16) & (df["실린더압력"] > 230)]
df_sub_3.info()
print(df_sub_3.head())

# 실습 4. 부정·목록·범위 조건
print("\n=== 실습 4. 부정·목록·범위 조건 ===")
df_shot = pd.read_csv("data/13_diecasting_shot.csv")
print(len(df_shot))
print("-" * 10, "~ 활용")
df_sub_not = df_shot[~(df_shot["품질등급"] == "불량")]
print(df_sub_not.head())
print(len(df_sub_not))
print("-" * 10, "isin 활용")

df_sub_isin = df_shot[df_shot["품질등급"].isin(["불량"])]
print(df_sub_isin.head())
print(len(df_sub_isin))
print("-" * 10, "between 활용")

df_sub_bet = df_shot[df_shot["실린더압력"].between(210, 250)]
print(df_sub_bet.head())
print(len(df_sub_bet))
print("-" * 10)
