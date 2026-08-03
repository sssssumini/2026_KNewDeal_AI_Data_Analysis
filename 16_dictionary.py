# 딕셔너리 { 키 : 값 }

data_class_list = ["수민", "랄라", "스파이더맨"]
data_class_dict = {"학생": "수민", "강사": "랄라", "친절한이웃": "스파이더맨"}

print(data_class_dict)
print(type(data_class_dict))
print(data_class_dict["친절한이웃"])


sensors = {"모터온도": 78, "진동": 0.5}
print(sensors["모터온도"])

sensors["센서이름"] = "babo"

print(sensors)

# 키 삭제
del sensors["모터온도"]
print(sensors)


is_motor_degree_key = "모터온도" in sensors

if is_motor_degree_key:
    print("그런 키 있어요!")
else:
    print("그런 키 없어요!")

if "모터온도" in sensors:
    print("그런 키 있어요!")
else:
    print("그런 키 없어요!")

print(sensors.keys())


for key, value in sensors.items():

    print(key)
    print(value)


print("=== 실습 1. 딕셔너리 만들고 다루기 ===")

sensor_dict = {"모터": 30, "진동": 190, "온도": 78}
print(sensor_dict["온도"])

sensor_dict["추가"] = 30
sensor_dict["모터"] = 80
print(sensor_dict)

print(sensor_dict.get("없는값"))
print(f"모터 in sensor_dict : {"모터" in sensor_dict}")

print("\n=== 실습 2. update로 여러 값 한번에 갱신하기 ===")
sensor_dict2 = {"모터": 30, "진동": 190, "온도": 78}
print(f"원래 딕셔너리 {sensor_dict2}")
new_dict = {"포항": "포스코"}
sensor_dict2.update(new_dict)
print(f"추가된 딕셔너리 {sensor_dict2}")
print(f"원래 딕셔너리 개수 : {len(sensor_dict2)}")
del sensor_dict2["모터"]
print(f"삭제된 딕셔너리 개수 : {len(sensor_dict2)}")

print("\n=== 실습 3. 딕셔너리로 통계내기 ===")
sensor_dict3 = {"모터": 40, "진동": 210, "온도": 70, "회전": 88}
sum_values = sum(sensor_dict3.values())
avg_values = sum_values / len(sensor_dict3)
print(avg_values)

max_value = sensor_dict3["모터"]
sensor_name = ""
for key, value in sensor_dict3.items():
    if max_value < value:
        max_value = value
        sensor_name = key
print(f"최댓값센서 {sensor_name}, {max_value}")

print("\n=== 실습 4. zip으로 센서명-값 매핑하기 ===")
sensor = ["모터", "진동", "온도", "회전"]
measure = [80, 20, 40, 22]
sensor_dict4 = dict(zip(sensor, measure))
for key, value in sensor_dict4.items():
    print(f"({key}), ({value})")

print("\n=== 실습 5. 임계값으로 경고 센서 분류하기 ===")
measure_dict = {"모터": 40, "진동": 210, "온도": 70, "회전": 88}
limit_dict = {"모터": 80, "진동": 30, "회전": 85, "온도": 100}

limit_over = []
for key, value in measure_dict.items():
    if value > limit_dict.get(key):
        limit_over.append(key)
print(f"경고 센서 : {limit_over}")

print("\n=== 실습 6. 중첩 딕셔너리로 설비 관리하기 ===")
measure_dict2 = {
    "1번펌프": {"온도": 80, "진동": 120, "상태": "정상"},
    "2번펌프": {"온도": 95, "진동": 100, "상태": "경고"},
}

print(measure_dict2["1번펌프"]["온도"])
for key, value in measure_dict2.items():
    for key2, value2 in value.items():
        if value2 == "경고":
            print(f"{key} {value2} 점검필요")

print("\n=== 실습 7. 표 데이터를 딕셔너리로 변환하기 ===")
ini_data = ["모터,40", "진동,210", "온도,70", "회전,88"]
key_data = []
value_data = []
for i in ini_data:
    ini_list = i.split(",")
    key_data.append(ini_list[0])
    value_data.append(int(ini_list[1]))
data_to_dict = dict(zip(key_data, value_data))
print(data_to_dict)

print("\n=== 실습 8. 센서 데이터 통합 정리 ===")
measure_dict_final = {"모터": 40, "진동": 210, "온도": 70, "회전": 88}
limit_dict_final = {"모터": 80, "진동": 30, "회전": 85, "온도": 100}

avg_measure = sum(measure_dict.values()) / len(measure_dict)
print(f"측정값 전체 평균 : {round(avg_measure,2)}")
limit_over_final = []
for key, value in measure_dict_final.items():
    if value > limit_dict_final.get(key):
        limit_over_final.append(key)
limit_over_final.sort()

print(f"위험 센서 : {limit_over_final}")
