import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)  # 터미널에서 정렬


tags = pd.read_csv("data/03-01_회전기계_신호_회전기계태그목록.csv")
df = pd.read_csv("data/03-01_회전기계_신호_진동추세.csv")

# 1번 모터에 대한 태그 목록
print(
    tags.columns.tolist()
)  # ['tag', 'equipment', 'physical_qty', 'indicator', 'summary', 'unit', 'direction', 'install_location']
print(
    tags.loc[
        tags["equipment"] == "1번 모터",
        [
            "tag",
            "indicator",
            "summary",
            "unit",
            "direction",
        ],
    ]
)

# 진동의 정상 범위 정하기
# 맨 앞 기준으로 20일 구간을 정상 기간으로 볼 것
MTR = ["MTR01_VIB_H", "MTR01_VIB_V", "MTR01_VIB_A", "MTR01_VIB_ACC"]
normal = df.head(20)

print(normal[MTR].agg(["min", "max"]))  # 최대최소(극단값) 출력

PMP = ["PMP01_VIB_H", "PMP01_VIB_V", "PMP01_VIB_A", "PMP01_VIB_ACC"]
print(normal[PMP].agg(["min", "max"]))


def first_over(col):
    limit = normal[col].max()
    over = df.index[df[col] > limit]
    return int(over[0] + 1) if len(over) else None


print("-" * 30)
print("[1번 모터]")
for c in MTR:
    print(c, first_over(c))
print("[1번 펌프]")
for c in PMP:
    print(c, first_over(c))

# 모터의 전류와 온도의 정상 범위 정하기
# 맨 앞 기준으로 20일 구"간을 정상 기간으로 볼 것
print("-" * 30)
print("[1번 모터 전류와 온도]")
for c in ["MTR01_CURRENT", "MTR01_TEMP"]:
    print(c, first_over(c))

# 전류와 온도가 이상반응에 대해서 늦게 반응한다

##### 모터 1번의 회전수
# 모터1번의 회전수와 컬럼 이름
# 1780, 1450 각각 몇 번 찍히는지
print("\n==모터 1번의 회전수==")
print(df["MTR01_RPM"].value_counts())

print(
    df.loc[
        df["MTR01_RPM"] == 1780, ["date", "MTR01_VIB_H", "MTR01_VIB_ACC", "MTR01_RPM"]
    ].head(4)
)
print(
    df.loc[
        df["MTR01_RPM"] == 1450, ["date", "MTR01_VIB_H", "MTR01_VIB_ACC", "MTR01_RPM"]
    ]
)

# 설비의 변화가 아닌 회전수(RPM)의 변화로 진동수가 변경됨

import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)  # 터미널에서 정렬


tags = pd.read_csv("data/03-01_유압·열설비_신호_계통태그목록.csv")
df = pd.read_csv("data/03-01_유압·열설비_신호_가열로온도.csv")


# FUR로 시작하는 태그를 측정 대상별로 나눕니다.
fur_df = tags[tags["tag"].str.startswith("FUR")]

# 분위기 온도, 소재 표면 온도, 배기가스 온도, 라인 속도
print(fur_df)

# [Step 2] 존별로 '앞 20일 구간'의 평균 편차(정상구간) 학인
# 존 - Z1, Z2, Z3

# 계산식 좌우 온도 편차 = 우측 온도 - 좌측 온도
df["Z1_DIFF"] = df["FUR01_Z1_TEMP_R"] - df["FUR01_Z1_TEMP_L"]
df["Z2_DIFF"] = df["FUR01_Z2_TEMP_R"] - df["FUR01_Z2_TEMP_L"]
df["Z3_DIFF"] = df["FUR01_Z3_TEMP_R"] - df["FUR01_Z3_TEMP_L"]
print(df.head(20)[["Z1_DIFF", "Z2_DIFF", "Z3_DIFF"]].mean())


# [Step 3] 시간이 지나며 편차가 어떻게 변하는지 확인
# 존(Z1,Z2,Z3)별로 아래 시점의 좌우 온도 편차를 비교하세요.


days = [1, 20, 40, 60]

for day in days:
    print(f"{day}일차")
    print(df[["Z1_DIFF", "Z2_DIFF", "Z3_DIFF"]].iloc[day - 1])

result = df.iloc[[d - 1 for d in days]][["Z1_DIFF", "Z2_DIFF", "Z3_DIFF"]].copy()
result.index = [f"{d}일차" for d in days]
print(result)

# [Step 4] 이상 위치 확인
# 편차가 가장 크게 증가한 존의 좌측 온도와 우측 온도를 비교하세요.

for day in days:
    print(f"{day}일차")
    print(df.iloc[day - 1][["FUR01_Z2_TEMP_L", "FUR01_Z2_TEMP_R"]])

# [Step 5] 소재 온도와 라인 속도 비교
# 아래 시점에서 소재 온도와 라인 속도를 확인하세요.
# 1일차, 20일차, 44일차, 45일차, 60일차

days_2 = [1, 20, 44, 45, 60]
result = df.iloc[[d - 1 for d in days_2]][["FUR01_MAT_TEMP", "FUR01_LINE_SPEED"]].copy()
result.index = [f"{d}일차" for d in days_2]
print(result)
