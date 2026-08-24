import pandas as pd

pd.set_option("display.unicode.east_asian_width", True) # 터미널에서 정렬

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