import os 
import sys
import csv

csv_path = os.path.join("data", "08_press.csv")

# 위의 경로의 파일을 찾지 못하면 강제종료 시키기 
if not os.path.exists(csv_path) :
    print("파일이 없습니다.")
    sys.exit(1) # 비정상 종료 시 보통 0이 아닌 값 전달
else :
    print("파일이 있습니다.")


with open(csv_path, "r", encoding="utf-8") as f :
    reader = csv.reader(f)

    for row in reader:
        print(row) # 각 행별로 출력

csv_path2 = os.path.join("data", "result.csv")

with open(csv_path2, "w", encoding="utf-8") as f2 :
    writer = csv.writer(f2)
    writer.writerow(["시각", "설비"])
    writer.writerow(["09:00", "PUMP-01"])

# 실습 5 : csv.writer로 CSV 쓰기
csv_path3 = os.path.join("data", "practice.csv")

with open(csv_path3, "w", encoding="utf-8", newline="") as f5 :
    writer = csv.writer(f5)
    writer.writerow(["시각", "설비"])
    writer.writerow(["09:00", "PUMP-01"])
    writer.writerow(["09:10", "PUMP-02"])

with open(csv_path3, "r", encoding="utf-8", newline="") as f5 :
    reader = csv.reader(f5)
    for row in reader :
        print(row)

# 실습 6. CSV 읽어 조건 저장하기

csv_path = os.path.join("data", "08_press.csv") # 경로 지정
over_list = [] # 90초과 행을 리스트로 받아냄 
header = [] # csv 행의 값을 받아냄 

with open(csv_path, "r", encoding="utf-8") as sensor: # open() 활용하여 csv 파일을 읽어냄
    reader = csv.reader(sensor)
    header = next(reader) # 헤더를 건너뛰고 reader가 반응하게 된다
    check_ind = header.index("전류") # 확인해야할 값의 인덱스를 저장 
    for row in reader: # reader의 값을 돌면서 조건에 맞는 값을 List에 append
        if float(row[check_ind]) > 90 :
            over_list.append(row)
        

csv_path_new = os.path.join("data", "over_press.csv") # 저장할 파일 경로 지정 
with open(csv_path_new, "w", encoding="utf-8") as over_sensor: # "w"로 열어서 
    writer = csv.writer(over_sensor)
    writer.writerow(header)
    # writer.writerows(over_list) # 한번에 저장 가능
    for row in over_list :
        writer.writerow(row)

with open(csv_path_new, "r", encoding="utf-8") as over_sensor: # 확인
    reader = csv.reader(over_sensor)
    for row in reader:
        print(row)
