import pandas as pd
import os

pd.set_option("display.unicode.east_asian_width", True)

# 실습 1. value_counts로 빈도 세기
print("\n=== 실습 1. value_counts로 빈도 세기 ===")

sensor = pd.read_csv("data/14_equipment_sensor.csv")

sensor.info()
print(sensor.head())
print(sensor.columns)

print("=" * 15)
print(sensor.value_counts("line"))
print(sensor.value_counts("shift"))


# 실습 2. 비율과 불균형 데이터
print("\n=== 실습 2. 비율과 불균형 데이터 ===")
hyd = pd.read_csv("data/14_hydraulic.csv")
print(hyd.head())
print(hyd.columns)

print(hyd.value_counts("result"))
print(hyd.value_counts("result", normalize=True).round(3))

# 실습 3. 구간으로 묶어 세기
print("\n=== 실습 3. 구간으로 묶어 세기 ===")
print(hyd["진동"].max(), hyd["진동"].min())
fre = pd.cut(hyd["진동"], bins=3, labels=["낮음", "보통", "높음"])
print(fre.value_counts())

print()
print("=" * 15, "선택문제", "=" * 15)

# 선택 문제
student = pd.read_csv("data/students_groupby_practice.csv")
student.info()
print(student.columns)
print(student.head(3))

# [문제 1] 이 학교의 전체 학생 수를 구하세요. (힌트: len 또는 shape)
num_student = len(student)
print(f"\n전체 학생 수 : {num_student}")

# [문제 2] 학년별 학생 수를 구하세요. (힌트: groupby + count 또는 size)
stu_by_grade = student.groupby("학년")["반"].size()
print(f"\n학년 별 학생수")
print(stu_by_grade)

# [문제 3] 학년 내 각 반별 학생 수를 구하세요. (힌트: 다중 컬럼 groupby)
stu_by_team = student.groupby(["학년", "반"])["반"]
print(f"\n학년 내 각 반별 학생 수")
print(stu_by_team.size())

# [문제 4] 각 반(학년, 반 조합)의 국어 점수 평균을 소수점 둘째 자리까지 구하세요.
kor = student.groupby(["학년", "반"])["국어"]
print(f"\n각 반(학년, 반 조합)의 국어 점수 평균")
print(kor.mean().round(2))

# [문제 5] 각 학년의 영어 점수 평균을 소수점 둘째 자리까지 구하세요.
eng = student.groupby("학년")["영어"]
print(f"\n각 학년의 영어 점수 평균")
print(eng.mean().round(2))

# [문제 6] 학교 전체의 수학 점수 평균을 소수점 둘째 자리까지 구하세요.
print(f"\n학교 전체의 수학 점수 평균")
print(student["수학"].mean().round(2))


# 실습 4. groupby로 그룹 집계
print("\n=== 실습 4. groupby로 그룹 집계 ===")
print(hyd.groupby("운전부하")["온도"].mean().round(3))
print(hyd.groupby("냉각기상태")["온도"].size())

# 실습 5. 그룹별 평균 비교와 정렬
print("\n=== 실습 5. 그룹별 평균 비교와 정렬 ===")
print(hyd.groupby("result")["진동"].mean().round(3))


# 실습 6. 여러 기준 조합 그룹
print("\n=== 실습 6. 여러 기준 조합 그룹 ===")
print(hyd.groupby('냉각기상태')['온도'].mean().round(2))
print(hyd.groupby('운전부하')['진동'].mean().round(3))
print(hyd.groupby(['냉각기상태', '운전부하'])['온도'].mean().round(2))
print(hyd.groupby('냉각기상태').size())

# 실습 7. 빈도와 그룹 집계 종합
print("\n=== 실습 7. 빈도와 그룹 집계 종합 ===")
print(hyd['밸브상태'].value_counts())
print(hyd.groupby('result').size())
print(hyd.groupby('냉각기상태')[['온도', '진동']].mean().round(2))


# 실습 1. 평균·분산·표준편차 구하기
print("\n=== 실습 1. 평균·분산·표준편차 구하기 ===")
print(hyd['진동'].mean().round(3)) # 45.339
print(hyd.groupby('냉각기상태')['진동'].mean().round(3))
print(hyd.groupby('냉각기상태')['진동'].var().round(3))
print(hyd.groupby('냉각기상태')['진동'].std().round(3))

# 실습 2. 그룹별 통계 응용
print("\n=== 실습 2. 그룹별 통계 응용 ===")

df = pd.read_csv("data/14_hydraulic_qc.csv", encoding="utf-8")
feats = ['지표01', '지표05']
print(df.groupby('검사결과')[feats].mean().round(2))
print(df.groupby('검사결과')[feats].std().round(2))

# 실습 3. agg로 여러 통계 한 번에
print("\n=== 실습 3. agg로 여러 통계 한 번에 ===")
report = hyd.groupby('냉각기상태').agg(
    평균진동 = ('진동', 'mean'),
    진동표준편차 = ('진동', 'std'),
    최대진동 = ("진동", "max")
).round(2)
print(report)

# 실습 4. agg 진단표 만들기
print("\n=== 실습 4. agg 진단표 만들기 ===")
report2 = hyd.groupby('result').agg(
    평균온도 = ('온도', 'mean'),
    온도편차 = ('온도', 'std'),
    평균진동 = ('진동', 'mean'),
    진동편차 = ('진동', 'std'),
    평균압력 = ("압력", "mean")
).round(2)
print(report2)
print(report2.sort_values('온도편차', ascending=False))

# 실습 5. 그룹별 통계량 종합

print("\n=== 실습 5. 그룹별 통계량 종합 ===")
# · 온도 열의 전체 평균과 표준편차
print(hyd['온도'].mean().round(2))
print(hyd['온도'].std().round(2))

print(hyd.groupby('냉각기상태')['온도'].agg(['mean', 'median']).round(2))

report3 = hyd.groupby('밸브상태').agg(
    평균온도 = ('온도', 'mean'),
    온도편차 = ('온도', 'std'),
    평균진동 = ('진동', 'mean')
).round(2)

print(report3)
# 내림차순 정렬 
print(report3.sort_values('온도편차', ascending=False))

# 실습 1) 상관계수와 상관행렬 구하기
print("\n=== 실습 1) 상관계수와 상관행렬 구하기 ===")
df = pd.read_csv("data/14_hydraulic_qc.csv", encoding="utf-8")
print(df[["지표01", "지표02", "지표03", "지표04"]].corr().round(3)) # 상관행렬

# 대각선(항상 1)과 대칭 구조를 확인하고 절댓값 큰 칸 찾기 : -0.983

# 실습 2) 강한 상관 쌍 찾기
print("\n=== 실습 2) 강한 상관 쌍 찾기 ===")

# "%02d"는 10진수를 두 자리로 만들어 포함시키라는 뜻
feat = ["지표%02d" % i for i in range(1, 11)]
print(feat)

cm = df[feat].corr().round(3)
print(cm)

# 위 cm 자료에서 0.4 이상의 상관관계가 크다 판단되는 경우를 뽑아보기
for i in range(len(cm.columns)):
    print(f"{i}번째 컬럼 이름 {cm.columns[i]}") 
    for j in range(i + 1, len(cm.columns)):

        c = cm.iloc[i, j]

        if abs(c) > 0.4:
            print(
                f"{i}번째 컬럼 {cm.columns[i]}과 비교할 {cm.columns[j]} : {c} -> 강한 상관계수"
            )

# 절댓값이 기준 이상인 쌍만 모아 큰 순서로 정렬

# 8/20
df_qc = pd.read_csv("data/14_hydraulic_qc.csv", encoding="utf-8")
df_qc.info()

r1 = df_qc["지표07"].corr(df_qc["지표08"])
print(r1)  
print(r1.round(3))  

cols = [
    "지표01",
    "지표02",
    "지표03",
    "지표04",
    "지표05",
    "지표06",
    "지표07",
    "지표08",
    "지표09",
    "지표10",
]
r2 = df_qc[cols].corr()
print(r2.round(2))

# 실습 3) 그룹별 상관 비교 
print("\n=== 실습 3) 그룹별 상관 비교 ===")
# 같은 센서 쌍의 상관이 그룹에 따라 달라지는지 비교

# 전체 데이터의 지표07과 지표08 상관관계
r_all = df_qc["지표07"].corr(df_qc["지표08"])
print(r_all.round(3))  # -0.969

# 검사결과가 합격인 데이터 그룹의 지표 07과 지표08 상관관계
df_qa = df_qc[df_qc["검사결과"] == "합격"]
r_qa = df_qa["지표07"].corr(df_qa["지표08"])
print(r_qa.round(3))  # 0.385

# 검사결과가 불합격인 데이터 그룹의 지표07과 지표08 상관관계
df_nqa = df_qc[df_qc["검사결과"] == "불합격"]
r_nqa = df_nqa["지표07"].corr(df_nqa["지표08"])
print(r_nqa.round(3))  # -0.998

# 해석 ------- 
# 검사결과 합격의 경우 지표07과 지표08 사이에 관계성이 약함
# 불합격이라면 그 관계성이 강하다

# 예상 결과
# 전체 -0.969, 합격 0.482, 불합격 0.564 (불합격 12건 주의)


# 실습 4) 통합 리포트 종합 
# 그룹 통계와 상관 분석을 묶어 발견/해석/행동 리포트 구성
print("\n=== 실습 4) 통합 리포트 종합  ===")
df = pd.read_csv("data/14_equipment_sensor.csv", encoding="utf-8")
df.info()

# 라인(line)으로 그룹을 나눠
# (temp의) 측정수(count)/평균온도(mean)/온도편차(std) 요약 -> agg
report = df.groupby("line")["temp"].agg(["count", "mean", "std"]).round(2)
print(report)

report = (
    df.groupby("line")
    .agg(측정수=("temp", "count"), 평균온도=("temp", "mean"), 온도편차=("temp", "std"))
    .round(2)
)
print(report)

print("-----------------------------")
print("라인별 통계")
print(report.sort_values("온도편차", ascending=False))

# 온도(temp)와 진동(vibration)의 상관계수(corr)를 구해 함께 움직임 확인
r = df["temp"].corr(df["vibration"])
print("-"*15)
print("온도와 진동의 상관계수")
print(r.round(3))  # 0.345

# 고장(result == 고장) 행을 걸러 라인별(line) 고장 건수까지 더해 우선 점검 대상 정리
df_bad = df[df["result"] == "고장"]

print("-"*15)
print("라인별 고장 건수")
print(df_bad.groupby("line").size())

# 실습 1) 상관계수와 상관행렬 구하기
print("\n=== 실습 1) 상관계수와 상관행렬 구하기 ===")
df = pd.read_csv("data/14_hydraulic_qc.csv", encoding="utf-8")
print(df[["지표01", "지표02", "지표03", "지표04"]].corr().round(3)) # 상관행렬

# 대각선(항상 1)과 대칭 구조를 확인하고 절댓값 큰 칸 찾기 : -0.983

# 실습 2) 강한 상관 쌍 찾기
print("\n=== 실습 2) 강한 상관 쌍 찾기 ===")

# "%02d"는 10진수를 두 자리로 만들어 포함시키라는 뜻
feat = ["지표%02d" % i for i in range(1, 11)]
print(feat)

cm = df[feat].corr().round(3)
print(cm)

# 위 cm 자료에서 0.4 이상의 상관관계가 크다 판단되는 경우를 뽑아보기
for i in range(len(cm.columns)):
    print(f"{i}번째 컬럼 이름 {cm.columns[i]}") 
    for j in range(i + 1, len(cm.columns)):

        c = cm.iloc[i, j]

        if abs(c) > 0.4:
            print(
                f"{i}번째 컬럼 {cm.columns[i]}과 비교할 {cm.columns[j]} : {c} -> 강한 상관계수"
            )


# 실습 1. 눈으로 결측 찾기
print("\n=== 실습 1. 눈으로 결측 찾기 ===")
df_log = pd.read_csv('data/15_사출성형_로그.csv', encoding='utf-8')
print(df_log.describe())

# 진짜 결측(NaN)과 위장 결측을 코드로 세어 확인

# 설비 센서 데이터를 불러와 isna로 컬럼별 NaN 개수 세기
print(df_log.isna().sum()) # True = 1(결측), False = 0 

# 조건 필터링으로 압력 0, 진동 -999 같은 위장 결측 개수 세기
print((df_log['사출압력'] == 0.0).sum()) # 2
print((df_log['스크루속도'] == -999.0).sum()) # 2

# 실습 2. SECOM 첫 탐색
print("\n=== 실습 2. SECOM 첫 탐색 ===")

df = pd.read_csv('data/15_01_사출성형_공정.csv', encoding='utf-8')

# head·shape·info·describe로 결측 분위기 파악
print(df.head())
print(df.shape)
df.info()

print(df.describe())

# 실습 3. 위장 결측 사냥
print("\n=== 실습 3. 위장 결측 사냥 ===")
df_log = pd.read_csv('data/15_사출성형_로그.csv', encoding='utf-8', na_values=[-999, 999])

# 위장 결측이 있는 열을 조건 필터링으로 추출해 확인
print((df_log['배럴온도'] == 999.0).sum())  
print((df_log['스크루속도'] == -999.0).sum()) 

# 실습 4. 컬럼별 결측 개수와 비율
print("\n=== 실습 4. 컬럼별 결측 개수와 비율 ===")
df = pd.read_csv('data/15_01_사출성형_공정.csv', encoding='utf-8')
# isna·sum으로 개수와 비율을 한 표로 정리
counts = df.isna().sum()
print(counts)

# · 전체 행 수로 나누고 백분율로 바꿔 비율 계산
ratio = (counts / len(df) * 100).round(1)
print(ratio)

# 결측이 있는 컬럼만 골라 개수와 비율을 나란히 정리 -> 새로운 데이터 프레임
table = pd.DataFrame({ '개수': counts, '비율': ratio })
print(table[table['개수'] > 0])


# 실습 5. 결측 순위와 행별 분석
print("\n=== 실습 5. 결측 순위와 행별 분석 ===")

# · 결측 비율을 내림차순 정렬해 가장 심한 컬럼 확인
print(ratio.sort_values(ascending=False).head(3))

df_axis = df.isna().sum(axis=1) # row 기준 
print(f"결측없는 행 {(df_axis == 0).sum()}개") 
print(f"결측있는 행 {(df_axis > 0).sum()}개")

print(f"결측 5개 이상있는 행 {(df_axis >= 5).sum()}개")

# 8/21

df = pd.read_csv('data/15_02_사출성형_공정.csv', encoding='utf-8')
df.info()

# 실습 1. dropna로 행·열 삭제
# 결측 있는 행과 열을 삭제하고 크기 변화 확인
# 결측 있는 행과 열을 삭제하고 크기 변화 확인

# · 원본 크기를 shape로 확인
print(df.shape) # (250, 22)

# · dropna로 결측 있는 행을 모두 삭제
print(df.dropna().shape) # (76, 22)

# · 방향을 열로 바꿔 결측 있는 열을 삭제
print(df.dropna(axis = 1).shape) # (250, 10)

# 예상 결과
# 250×22 → 행삭제 76×22, 열삭제 250×10

print('-------------------------------')

# 실습 2. dropna 옵션 조절
# how·thresh·subset로 삭제 기준을 세밀하게 조절

# · how로 완전히 빈 행만 삭제하는 기준 적용 -> how = 'all'
print(df.dropna(how = 'all').shape) # (250, 22)
# 250개 row가 다 살아남았다는 의미 
# : NaN으로 모든 컬럼 내용이 다 채워진 row가 없다는 뜻

# · thresh로 값이 일정(예, 20개) 개수 "이상"인 행만 남기기 -> thresh = 20
print(df.dropna(thresh = 20).shape) # (162, 22)
# 250 - 162 = 88개 row는 NaN이 3개 이상이라는 뜻

# · subset으로 특정 컬럼이 빈 행만 삭제
# 예, 불량여부 컬럼에 NaN이 있는 row들만 제거 -> subset = ['불량여부']
print(df.dropna(subset = ['불량여부']).shape) # (250, 22)
# '불량여부' 컬럼에는 NaN이 하나도 없다고 판단 가능

# 예상 결과
# 완전 결측 행만 삭제는 거의 유지, 임계값 20은 162행

df = pd.read_csv('data/15_02_사출성형_공정.csv', encoding='utf-8')
print(df.shape) # (250, 22)
print(df.isna().sum())

# 실습 3. 결측 비율 기준 컬럼 제거
# 결측 비율이 높은 컬럼만 골라 제거

# 단계
# · 컬럼별 결측 비율을 계산
df_rate = df.isna().sum() / len(df)
print(df_rate)

# · 비율이 기준을 넘는 컬럼 이름만 목록으로 뽑기 
# -> 40% 이상 NaN으로 채워진 컬럼 목록
df_terminates = df_rate[df_rate > 0.4]
print(df_terminates)

# 최초 컬럼 이름들이 df_terminates의 index labels가 되었다.
list_terminates = df_terminates.index.tolist() # ['최대사출속도', '감압시간']
print(list_terminates)

# · 그 컬럼들을 drop으로 제거하고 크기 확인
# drop에 컬럼을 제시하면 기본동작 : 컬럼을 지워버림
df_final = df.drop(columns = list_terminates)
df_final.info()

# 예상 결과
# 40% 초과 센서19·20 제거 → 250×20

print("--------------------------------------")

# 실습 4. 삭제 손실 비교
# 삭제 방식별 남는 행 수와 손실률을 표로 비교

# 단계
# · 원본·행삭제·thresh 각 방식의 남는 행 수 구하기
# · 방식과 행 수를 하나의 표로 모으기

비교 = pd.DataFrame({
    '방식': ['원본', '행삭제', 'thresh20'],
    '행': [len(df), len(df.dropna()), len(df.dropna(thresh = 20))]
})

비교['손실률'] = ((1 - 비교['행'] / len(df)) * 100) .round(2)

print(비교)
#          방식    행   손실률
# 0        원본  250   0.0
# 1       행삭제   76  69.6
# 2  thresh20  162  35.2

# 위 코드는 너무 고급기술 - DF의 더 깊은 이해 경험 필요
# 여러분은 그냥 개별 3가지 항목들을 따로따로 계산시켜 출력해도 괜찮아요


# · 원본 대비 손실률을 백분율로 계산해 나란히 보기

# 예상 결과
# 행삭제 손실 약 70%, thresh 손실 약 35%

df = pd.read_csv('data/15_02_사출성형_공정.csv', encoding='utf-8')

# 실습 5. fillna 평균·중앙값 대체
# 결측을 평균과 중앙값으로 채우고 차이 이해
print(df['최대사출압'].isna().sum()) # 60개 NaN 확인

# · 대상 컬럼의 평균과 중앙값을 각각 구해 비교
# · fillna로 평균을 채운 결과 만들기
mean = df['최대사출압'].mean()
print(f"최대사출압의 평균 : {mean}")
# 최대사출압의 평균 : 1241.6723684210526

s_fillmean = df['최대사출압'].fillna(mean)
print(s_fillmean)
df['최대사출압'] = s_fillmean
print(df['최대사출압'].isna().sum()) # 최대사출압 컬럼의 NaN 0개

# · fillna로 중앙값을 채운 결과 만들기(이상치에 강함)
median = df['최대사출압'].median()
print(f"최대사출압의 중앙값 : {median}")
# 최대사출압의 중앙값 : 1240.84

s_fillmedian = df['최대사출압'].fillna(median)
print(s_fillmedian)
df['최대사출압'] = s_fillmedian
print(df['최대사출압'].isna().sum()) # 최대사출압 컬럼의 NaN 0개

# 예상 결과
# 센서17 평균 466.26·중앙값 465.9로 대체, 남은 결측 0


df = pd.read_csv('data/15_02_사출성형_공정.csv', encoding='utf-8')
# 실습 8. 제거 vs 대체 비교
# 같은 데이터에 제거와 대체를 적용해 결과 비교

# · 결측 심한 컬럼을 먼저 뺀 기준 데이터 만들기
print(df.isna().sum())
# 최대사출속도    109
# 감압시간      109
기준 = df.drop(columns=['최대사출속도', '감압시간'])
기준.info() # 최대사출속도, 감압시간 컬럼 제거 확인
print(기준.shape) # (250, 20)

# · 기준 데이터에서 결측 행을 삭제한 제거 버전 만들기
제거판 = 기준.dropna()
print(제거판.shape) # (110, 20)

# · 기준 데이터의 결측을 중앙값으로 채운 대체 버전 만들기
대체판 = 기준.fillna(기준.median(numeric_only = True))
print(대체판.shape) # (250, 20)

# 예상 결과
# 제거 버전 110행, 대체 버전 250행(모두 유지)

print("----------------------------------------")

# 실습 9. SECOM·AI4I 종합 처리
# 제거와 대체를 조합해 전체 결측을 처리하고 저장

# · 결측 비율 높은 컬럼을 제거하고 나머지는 중앙값으로 채우기
# 앞서 처리한 대체판 재사용!

# · 처리 후 남은 결측과 크기를 확인하고 파일로 저장
print(대체판.isna().sum().sum()) # 0
대체판.to_csv('data/15_02_사출성형_공정_clean.csv', index=False, encoding='utf-8')

# · 같은 절차를 AI4I 데이터에도 반복해 결측 0 확인

# 예상 결과
# SECOM 결측 0·저장, AI4I 결측 0

# 8/24
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)

# 실습 1. 주조 데이터 구조·분포 살펴보기
print("\n=== 실습 1. 주조 데이터 구조·분포 살펴보기 ===")
# 주조 데이터를 불러와 크기·컬럼·자료형을 확인

# · read_csv로 데이터를 불러와 head로 앞부분 확인
df1 = pd.read_csv("data/16_diecasting.csv", encoding='utf-8')
# · shape와 columns로 크기와 컬럼 이름 확인
print(df1.shape)
print(df1.columns)
# · info로 자료형과 결측 여부 훑기
df1.info()

# 실습 2. 한 컬럼의 최소·최대·범위
print("\n=== 실습 2. 한 컬럼의 최소·최대·범위 ===")
# 한 컬럼의 최솟값·최댓값·범위를 구해 퍼짐 확인

# · 실린더압력 열의 최솟값, 최댓값 구하기
min_sil = df1["실린더압력"].min()
print(f"최솟값 :  {min_sil}")
max_sil = df1["실린더압력"].max()
print(f"최댓값 :  {max_sil}")
# · 최댓값에서 최솟값을 빼 범위 계산
print(f"최대 - 최소 :  {max_sil-min_sil}")


# 실습 3. 정렬해서 이상치 후보 찾기
print("\n=== 실습 3. 정렬해서 이상치 후보 찾기 ===")
# · 사이클타임 열을 기준으로 내림차순 정렬
s_sorted = df1.sort_values('사이클타임', ascending = False)
# · 위쪽 끝에서 동떨어진 큰 값 찾기
print(s_sorted.head(5))
# · 각 후보를 정상 상태와 이상 상태로 나누기

# 실습 4. 평균·중앙값으로 이상치 영향 확인
print("\n=== 실습 4. 평균·중앙값으로 이상치 영향 확인 ===")
# · 사이클타임의 평균과 중앙값을 각각 구해 차이 확인
avg_cycle = df1["사이클타임"].mean()
median_cycle = df1["사이클타임"].median()
print(f"평균 :  {avg_cycle} / 중앙값 : {median_cycle}")
print(f"평균과 중앙값의 차이 :  {avg_cycle-median_cycle}")
# · 상태가 정상인 행만 조건으로 골라내기
df_ok = df1[df1["상태"] == 0]
# · 정상만의 평균이 중앙값에 가까워지는지 확인
print(f"정상값 평균과 중앙값의 차이 :  {round(df_ok["사이클타임"].mean()-df_ok["사이클타임"].median(),2)}")


# 실습 5. quantile로 Q1·Q2·Q3
print("\n=== 실습 5. quantile로 Q1·Q2·Q3 ===")
print(f"25% Q1 = {df1["사이클타임"].quantile(0.25)}")
print(f"50% Q2 = {df1["사이클타임"].quantile(0.5)}")
print(f"중앙값 = {df1["사이클타임"].median()}")
print(f"75% Q3 = {df1["사이클타임"].quantile(0.75)}")


# 실습 6. describe로 격차 큰 컬럼 찾기
print("\n=== 실습 6. describe로 격차 큰 컬럼 찾기 ===")
# · 여러 공정 컬럼을 describe로 요약
print(df1.describe())

# · 요약을 컬럼별로 정리하고 평균과 중앙값 격차 계산
# .T -> describe 결과의 axis를 바꿈
report = df1[['실린더압력', '주조압력', '사이클타임', '비스킷두께', '형체력']].describe().T
print(report)

# · 격차가 큰 순으로 정렬해 이상치 의심 컬럼 확인
# -> 격차라는 새로운 컬럼을 추가해서 계산결과들을 담기 : 새로운 컬럼이름을 언급하면 추가가 된다
# -> 그 다음에 격차 결과순서로 정렬
report['격차'] = (report['mean'] - report['50%']).abs() # 절대값 

print(report.sort_values('격차', ascending = False)[['mean', '50%', 'max', '격차']].head(3))

# 실습 7. 여러 컬럼의 가운데 절반 폭 비교
print("\n=== 실습 7. 여러 컬럼의 가운데 절반 폭 비교 ===")
# · 세 컬럼의 사분위수를 한 번에 구하기
df_q = df1[["사이클타임","실린더압력","비스킷두께"]].quantile([0.25, 0.5, 0.75])
print(df_q)
# · 각 컬럼의 75% 값에서 25% 값을 빼 가운데 절반 폭 계산
print(df_q.loc[0.75] - df_q.loc[0.25])
# · 폭이 좁은 안정 컬럼과 넓은 의심 컬럼 구분

import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)

# 실습 1. IQR과 이상치 경계 구하기
print("\n=== 실습 1. IQR과 이상치 경계 구하기 ===")
df = pd.read_csv('data/16_diecasting.csv', encoding='utf-8')

# · 사이클타임의 25%·75% 값을 구해 IQR(Q3-Q1) 계산
q1 = df['사이클타임'].quantile(0.25)
q3 = df['사이클타임'].quantile(0.75)
print(f"Q1: {q1}, Q3: {q3}")
iqr = round(q3 - q1,2)
print(f"IQR: {iqr}")

# · Q1에서 IQR의 1.5배를 빼 하한 계산
# · Q3에 IQR의 1.5배를 더해 상한 계산
lower = round(q1 - 1.5 * iqr,2)
upper = round(q3 + 1.5 * iqr,2)
print(f"하한선: {lower}, 상한선: {upper}")


# 실습 2. 조건 필터로 이상치 골라내고 개수·비율
print("\n=== 실습 2. 조건 필터로 이상치 골라내고 개수·비율 ===")
# · 하한보다 작거나 상한보다 큰 조건을 각각 괄호로 감싸 또는로 연결
mask = (df['사이클타임'] < lower) | (df['사이클타임'] > upper)
# · 조건에 맞는 이상치 행만 골라 확인
# · sum으로 개수, mean으로 비율 계산
print(mask.sum())
print(df[mask].shape) 
print(df[~mask].shape)



# 실습 4. 이상치 제거 후 크기 비교
print("\n=== 실습 4. 이상치 제거 후 크기 비교 ===")
# · 조건을 뒤집어 정상 범위 행만 남기기
mask_ok = df[~mask]
print(mask_ok.shape) # (182, 7) : 이 경우는 결측치는 제외함
# · 원본과 제거 후의 행 수를 비교
print(f"원본 : {len(df)} / 이상치 제거 : {len(mask_ok)}")
# · 제거 후 평균을 구해 변화 확인
print(round(df['사이클타임'].mean(), 2))
print(round(mask_ok['사이클타임'].mean(), 2))

# 실습 5. 경계값 보정 clipping
print("\n=== 실습 5. 경계값 보정 clipping ===")
# · clip으로 하한보다 작은 값은 하한으로 올리기
# · 상한보다 큰 값은 상한으로 내리기
re_df = df['사이클타임'].clip(lower=lower, upper=upper)
# · 보정 후 최솟값·최댓값·평균 확인
print(round(re_df.min(), 2), round(re_df.max(), 2))   # 20.6 58.61
print(round(re_df.mean(), 2)) # 28.28

# 실습 6. 처리 전후 통계 비교
print("\n=== 실습 6. 처리 전후 통계 비교 ===")

# · 실린더압력 이상치 경계와 조건을 만들기
Q1 = df['실린더압력'].quantile(0.25)
Q3 = df['실린더압력'].quantile(0.75)
IQR = Q3 - Q1
L = Q1 - 1.5 * IQR
U = Q3 + 1.5 * IQR

m = (df['실린더압력'] < L) | (df['실린더압력'] > U)
fill_df= df['실린더압력'].mask(m).fillna(df['실린더압력'].mask(m).median())

# · 제거·보정·중앙값 채움 세 방식을 각각 적용
# · 처리 전 평균과 세 방식의 평균을 나란히 비교
print(f"처리 전 : {round(df['실린더압력'].mean(), 2)}") 
print(f"제거 : {round(df[~m]['실린더압력'].mean(), 2)}") 
print(f"이상치 최대 최소로 대치 : {round(df['실린더압력'].clip(L, U).mean(), 2)}") 
print(f"중앙값 대치 : {round(fill_df.mean(), 2)}") 

# 실습 7. duplicated로 중복 찾기와 개수
print("\n=== 실습 7. duplicated로 중복 찾기와 개수 ===")
# · duplicated로 중복 행 여부를 참·거짓으로 표시
# · sum으로 중복 개수 세고 중복 행 직접 확인
print(df.duplicated().sum()) # 2
print(df[df.duplicated()])

# · keep을 거짓으로 두면 겹친 행이 모두 표시되는 것 확인
print(df.duplicated(keep=False).sum()) # 4 : 겹친 행을 원본까지 모두 표시 


# 실습 8. drop_duplicates로 중복 제거
print("\n=== 실습 8. drop_duplicates로 중복 제거 ===")
# · drop_duplicates로 완전 중복 행 제거
# · 제거 후 행 수와 남은 중복 개수 확인
print(len(df)) # 202
df_onlyone = df.drop_duplicates()
print(len(df_onlyone)) # 200
# · subset으로 특정 컬럼만 기준 삼아 제거
df_onlyone_shot = df.drop_duplicates(subset=['샷'], keep='last')
print(len(df_onlyone_shot)) # 200


# 실습 9. reset_index로 인덱스 정리
print("\n=== 실습 9. reset_index로 인덱스 정리 ===")
# · drop_duplicates로 중복을 제거
df_clean = df.drop_duplicates()

# · reset_index로 인덱스를 0부터 다시 매기기
df_clean_idxreset = df_clean.reset_index(drop = True)

print(df_clean.index.min(), df_clean.index.max()) # 0 199
print(len(df_clean)) # 200

print(df_clean_idxreset.index.min(), df_clean_idxreset.index.max()) # 0 199
print(len(df_clean_idxreset)) # 200

# · 인덱스 최솟값·최댓값으로 연속성 확인

# 실습 10. 다른 현장(용접) 이상치·중복 종합 정제
print("\n=== 실습 10. 다른 현장(용접) 이상치·중복 종합 정제 ===")

# · 용접 통전전류의 IQR 경계로 이상치 개수·비율 확인
wf = pd.read_csv("data/16_welding.csv", encoding="UTF-8")

print(f"초기 : {len(wf)}")

q1, q3 = wf['통전전류'].quantile(0.25), wf['통전전류'].quantile(0.75)
lo, hi = q1 - 1.5 * (q3 - q1), q3 + 1.5 * (q3 - q1)
m = (wf['통전전류'] < lo) | (wf['통전전류'] > hi)
print(int(m.sum()), round(m.mean() * 100, 1)) # 24 14.8 (판정 0 불량과 대체로 일치)

# · clip으로 이상치를 보정하고 중복을 제거·정리
wf["통전전류"] = wf["통전전류"].clip(lower=lo, upper=hi)
wf = wf.drop_duplicates().reset_index(drop=True) # 중복 제거 
print(len(wf)) # 158 >> 4개 행 제거 

# · 정제한 데이터를 파일로 저장
wf.to_csv('data/16_welding_cleaned.csv', index=False)