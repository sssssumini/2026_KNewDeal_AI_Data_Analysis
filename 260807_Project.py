import os
import csv
import sys

# 헤더, 데이터 행, 데이터 행 수 반환하는 함수 
def csv_read(file_path) :
    header, csv_contents, row_count = [], [], None
    try :
        with open(file_path, "r", encoding="utf-8") as f:
            csv_reader = csv.reader(f)
            header = next(csv_reader)
            row_count = 0
            csv_contents = []
            for row in csv_reader :
                row_count+=1
                csv_contents.append(row)
    
    except FileNotFoundError :
        print("파일을 찾을 수 없습니다.")    
    return header, csv_contents, row_count

def make_dict(ind, header, csv_contents) :
    sensor_dict = {}

    for row in csv_contents :
        if row[ind] in sensor_dict :
            sensor_dict[row[ind]].append(row)
        else :
            sensor_dict[row[ind]] = [row] # 리스트로 만들어서 넣음 key : [[value1], [value2]]
    
    return sensor_dict

def min_value(index, contents) :
    min_measure = None
    for row in contents :
        try :
            value = float(row[index])

            if min_measure is None or min_measure > value:
                min_measure = value
        except : 
            continue

    return min_measure

def max_value(index, contents) :
    max_measure = None
    for row in contents :
        try :
            value = float(row[index])

            if max_measure is None or max_measure < value:
                max_measure = value
        except : 
            continue

    return max_measure

def sum_value(index, contents) :
    sum = 0
    for row in contents :
        try :
            float_num = float(row[index])
            sum += float_num
        except :
            continue
    return sum

def value_count(index, contents) :
    count = 0
    for row in contents :
        try :
            if row[index] != "" :
                count += 1
        except :
            continue
    return count

def avg_value(total, count):
    try :
        avg = round(total/count,2)
    except : avg = None
    return avg

def bad_check(ind, top_ind, low_ind, csv_contents):
    bad_sensor = []
    normal_sensor_count = 0
    normal_dict = {}
    for row in csv_contents :
        try : 
            top, low, measure = float(row[top_ind]), float(row[low_ind]), float(row[ind_measure])
            
            if measure < top and measure > low :
                normal_sensor_count += 1

                if row[ind] in normal_dict :
                    normal_dict[row[ind]] += 1
                else :
                    normal_dict[row[ind]] = 1
                
            else :
                bad = []
                bad.append(row[0])
                bad.append(row[1])
                if measure > top :
                    bad.append("상한치 초과")
                else :
                    bad.append("하한치 미만")
                bad_sensor.append(bad)
                
        except : continue

    return bad_sensor, normal_sensor_count, normal_dict

file_path = os.path.join("data", "09_ict_inspection_dirty.csv")

# 출력을 파일로 전환
sys.stdout = open("output.txt", "w", encoding="utf-8")

# 1번
header, csv_contents, row_count = csv_read(file_path)
print("2026.08.07 실습 레포트. txt")
print("="*50, "\n")
print("09_ict_inspection_dirty.csv 파일 개요")
print(header)
for row in csv_contents :
    print(row)

print(f"총 행 개수는 : {row_count}개 입니다")

# 2번 
ind = header.index("부품명")
sensor_dict = make_dict(ind, header,csv_contents)

print("\n부품 별 측정값의 개수")
print("|  ", end="")

for key, value in sensor_dict.items() :
    print(f"{key} :{len(value)}개", end = "  |  ")

# 3번 
print("\n\n")
ind_measure = header.index("측정값")
print(f"{header[ind_measure]}의 개수는 {value_count(ind_measure, csv_contents)}", end = " | ")
print(f"평균 : {avg_value(sum_value(ind_measure, csv_contents), value_count(ind_measure, csv_contents))}", end = " | ")
print(f"최대값 {max_value(ind_measure, csv_contents)}", end = " | ")
print(f"최솟값 {min_value(ind_measure, csv_contents)}", end = " | ")
print("\n")

# 4번
top_ind = header.index("상한치")
low_ind = header.index("하한치")

bad_sensor, normal_sensor_count, normal_dict  = bad_check(ind, top_ind, low_ind, csv_contents)

print(f"정상 센서 : {normal_sensor_count}개")
print(" ㄴ 세부사항")
print(normal_dict)

print(f"\n오류 센서 목록 (검사 ID | 부품명 | 원인)")
for i in bad_sensor :
    print(i)





# 파일 닫기 및 원래 상태 복원 (선택 사항)
sys.stdout.close()