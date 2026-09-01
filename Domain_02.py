import pandas as pd 

pd.set_option("display.unicode.east_asian_width", True) # 터미널에서 정렬


df = pd.read_csv("data/02-01_측정의_3요소_측정샘플.csv", encoding="UTF-8")

print(df.shape)
print(df.head(3))
df.info()

df["timestamp"] = pd.to_datetime(df["timestamp"])

gaps = df["timestamp"].diff().value_counts()
print(gaps)

print(df.describe())

print(df.min())
print(df.max())
print(df.mean())

gap_df = df.diff().abs()
print(gap_df.head(10))
print(gap_df.replace(0,pd.NA).min())

numeric_df = df.select_dtypes("number")
for col in numeric_df.columns:
    print(f"\n[{col}]")
    print(df[["timestamp", col]].head(20))
# # timestamp
# # 0 days 00:01:00    719


# # [3단원 실습2]
# # * 송풍기 데이터 앞 6시간과 뒤 6시간 비교
# # 변수	앞 6시간 평균	뒤 6시간 평균	변화 방향
# # 송풍량  blast_flow_nm3min	약 5198.67	약 4977.83	감소
# # 송풍압  blast_pressure_kpa	약 379.79	약 397.72	증가
# # 송풍기 진동  blower_vib_mms	약 3.40	약 3.40	거의 변화 없음

# before = df.iloc[:360]
# after = df.iloc[360:]

# cols = ["blast_flow_nm3min","blast_pressure_kpa", "blower_vib_mms"]
# print("=== 앞 6시간 ===")
# print(before[cols].mean())
# print("=== 뒤 6시간 ===")
# print(after[cols].mean())

# # 결과값 
# # === 앞 6시간 ===
# # blast_flow_nm3min     5198.667778
# # blast_pressure_kpa     379.786667
# # blower_vib_mms           3.397361
# # dtype: float64
# # === 뒤 6시간 ===
# # blast_flow_nm3min     4977.828056
# # blast_pressure_kpa     397.715833
# # blower_vib_mms           3.398583

# # <의미 해석>
# # 송풍량 감소, 송풍압 유지, 송풍기 진동 유지
# print(">> 송풍량 감소, 송풍압 유지, 송풍기 진동 유지")
# # 앞 6시간과 뒤 6시간을 비교한 결과, 송풍량은 약 5198.7에서 4977.8로 감소했고, 
# # 송풍압은 약 379.8에서 397.7로 증가했다. 반면 송풍기 진동은 약 3.4 mm/s 수준으로 거의 변화가 없었다. 
# # 따라서 뒤 6시간에는 송풍량 감소와 송풍압 상승이 나타났지만 송풍기 자체의 진동 변화는 크지 않았다.
# # 송풍압은 증가하고 송풍량은 감소했지만 송풍기 진동은 정상 수준을 유지했으므로, 
# # 송풍기 자체의 기계적 이상보다는 고로 내부 통기성 저하와 같은 조업 상태 변화를 우선 의심할 수 있다.
