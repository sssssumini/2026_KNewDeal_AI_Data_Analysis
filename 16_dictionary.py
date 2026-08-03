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
