import pandas as pd 
import numpy as np

pd.set_option("display.unicode.east_asian_width", True) # 터미널에서 정렬

data = pd.read_csv("data/01-01_철강_공정_개관_설비태그.csv", encoding="UTF-8")
print(data.head())

tag = data["tag"]

parts = tag[0].split("-")
print(parts)

plant = parts[0] # 공장 
process = parts[1] # 공정  
equip = parts[2] # 설비 
unit_no = parts[3] # 일련번호
measure = parts[4] # 측정항목

print(f"공장 {plant} 공정 {process} 설비 {equip} 일련번호 {unit_no} 측정항목 {measure}")

print("="*50)

# 공정데이터 분류
process_KR = {
    "SNT" : "소결",
    "CKO" : "코크스",
    "BF" : "고로",
    "BOF" : "전로",
    "CCM" : "연주",
    "HSM" : "열간압연",
    "CRM" : "냉간압연",
    "UTL" : "유틸리티",
}

print(process_KR["BOF"])
print(f"미등록 방지 get 메소드 활용  : .get(\"항목\", \"미등록\") >>> {process_KR.get("BOF1", "미등록")}")
      
# 계측항목 규칙표 
measure_KR = {
    "VIB" : "진동",
    "CUR" : "전류",
    "TMP" : "온도",
    "PRS" : "압력",
    "FLW" : "유량",
    "SPD" : "속도",
    "LVL" : "레벨",
    }

print(data.shape)
print(data.columns.tolist())

# 공정별로 몇개의 태그가 있는지 확인 
split_cols = data["tag"].str.split("-", expand=True)

temp = 0 
for i in ["plant", "process", "equip", "unit_no", "measure"]:
    data[i] = split_cols[temp]
    temp += 1

data["process_kr"] = data["process"].map(process_KR).fillna("미등록")
print(data[["tag", "process_kr"]].head(3))
print(data.groupby("process_kr").size())


# 실습1 - 설비 태그에서 공정 위치 추론
# 실습 목표
# 24개 태그를 읽어 공정과 상하공정 구분을 판정한 표 작성

data.info()

# 매핑 활용 
# stage(공정) 구분 값은 연주를 기준으로 상공정, 하공정, 유틸리티 
stage_KR = {
    "SNT" : "상공정",
    "CKO" : "상공정",
    "BF" : "상공정",
    "BOF" : "상공정",
    "CCM" : "상공정",
    "HSM" : "하공정",
    "CRM" : "하공정",
    "UTL" : "유틸리티",
}

data["stage"] = data["process"].map(stage_KR).fillna("미등록")
print(data.groupby("stage").size())

data["measure_kr"] = data["measure"].map(measure_KR).fillna("미등록")
print(data.groupby("measure_kr").size())

max_measure = data.groupby("measure_kr").size().sort_values(ascending=False, kind="stable")
print(max_measure)

print("="*15, "실습 2", "="*15)

df = pd.read_csv("data/01-02_원료_전처리와_제선_제선조업.csv", encoding="UTF-8")

print(df.shape)
print(f"원래 timestamp 데이터타입 : {df["timestamp"].dtype}") # str
df["timestamp"] = pd.to_datetime(df["timestamp"])
print(f"바꾼 timestamp 데이터타입 : {df["timestamp"].dtype}") # datetime64[us]

# (+) read_csv() 옵션 활용 
df2 = pd.read_csv("data/01-02_원료_전처리와_제선_제선조업.csv", encoding="UTF-8", parse_dates=["timestamp"])
print(f"(+) timestamp 데이터타입 : {df["timestamp"].dtype}") # datetime64[us]

gaps = df["timestamp"].diff().value_counts()
print(gaps)
# timestamp
# 0 days 00:01:00    719


# [3단원 실습2]
# * 송풍기 데이터 앞 6시간과 뒤 6시간 비교
# 변수	앞 6시간 평균	뒤 6시간 평균	변화 방향
# 송풍량  blast_flow_nm3min	약 5198.67	약 4977.83	감소
# 송풍압  blast_pressure_kpa	약 379.79	약 397.72	증가
# 송풍기 진동  blower_vib_mms	약 3.40	약 3.40	거의 변화 없음

before = df.iloc[:360]
after = df.iloc[360:]

cols = ["blast_flow_nm3min","blast_pressure_kpa", "blower_vib_mms"]
print("=== 앞 6시간 ===")
print(before[cols].mean())
print("=== 뒤 6시간 ===")
print(after[cols].mean())

# 결과값 
# === 앞 6시간 ===
# blast_flow_nm3min     5198.667778
# blast_pressure_kpa     379.786667
# blower_vib_mms           3.397361
# dtype: float64
# === 뒤 6시간 ===
# blast_flow_nm3min     4977.828056
# blast_pressure_kpa     397.715833
# blower_vib_mms           3.398583

# <의미 해석>
# 송풍량 감소, 송풍압 유지, 송풍기 진동 유지

# 앞 6시간과 뒤 6시간을 비교한 결과, 송풍량은 약 5198.7에서 4977.8로 감소했고, 
# 송풍압은 약 379.8에서 397.7로 증가했다. 반면 송풍기 진동은 약 3.4 mm/s 수준으로 거의 변화가 없었다. 
# 따라서 뒤 6시간에는 송풍량 감소와 송풍압 상승이 나타났지만 송풍기 자체의 진동 변화는 크지 않았다.
# 송풍압은 증가하고 송풍량은 감소했지만 송풍기 진동은 정상 수준을 유지했으므로, 
# 송풍기 자체의 기계적 이상보다는 고로 내부 통기성 저하와 같은 조업 상태 변화를 우선 의심할 수 있다.




# ----------------------------------------------------------------------------
# 공정별로 몇개의 태그가 있는지 확인 

# val = data["tag"]
# pro = []
# for i in val : 
#     temp = i.split("-")
#     pro.append(temp[1])

# for key, value in process_KR.items():
#     print(f"{value} : {pro.count(key)}")


# 공정명 매핑
# 공정 코드를 한글 이름으로 변환

# 상하공정 분류
# stage 컬럼에 상공정·하공정·유틸리티 구분
# data['stage'] = "유틸리티"
# data.loc[(data["process"] == "SNT") | (data["process"] == "CKO") | (data["process"] == "BF") , 'stage'] = '상공정'
# data.loc[(data["process"] == "CCM") | (data["process"] == "HSM"), 'stage'] = '하공정'

# print(data.head())
# print(data.groupby("stage").size())

# stage_count = data["stage"].value_counts()

# print(f"가장 많이 등장하는 공정 : {stage_count.idxmax()}")
# print(f"태그 개수 : {stage_count.max()}개")

# # STEP 2
# # 계측항목별 태그개수와 가장 많이 등장하는 물리량(계측항목) 출력해보기
# print(data.groupby("measure").size())

# measure_count = data["measure"].value_counts()

# print(f"가장 많이 등장하는 공정 : {measure_count.idxmax()}")
# print(f"태그 개수 : {measure_count.max()}개")