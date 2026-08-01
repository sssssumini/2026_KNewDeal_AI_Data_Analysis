# set
# set은 순서, 횟수 상관 없음

# set은 길이가 짧음 (중복 제거)
# set은 인덱스가 없음
# 순회 속도가 리스트보다 훨씬 빠름

# set에 sorted(정렬, 순서가 필수불가결한 조건)를 적용하게 되면 리스트형으로 형변환을 하게 됨

# alerts = {"s01", "s02", "s03", "s04", "s05", "s06"}
# print(type(alerts))

# print("s01" in alerts)
# if "s01" in alerts:
#     print("s01 정비필요")

# print("=== 실습 : set으로 중복 센서 제거하기 ===")
# sensor_ID = [
#     "WOR_01",
#     "WOR_01",
#     "WOR_01",
#     "WOR_01",
#     "WOR_06",
#     "WOR_06",
#     "WOR_03",
#     "WOR_05",
# ]
# print(sensor_ID)
# sensor_set = set(sensor_ID)
# print(f"{sensor_ID} \n {sensor_set}")

print("=== 실습 : 두 라인의 센서 구성 비교하기 ===")
a_sensor = {"s01", "s02", "s03", "s05"}
b_sensor = {"s04", "s03", "s05"}
total = a_sensor.union(b_sensor)
intersection = a_sensor & b_sensor
difference_a = a_sensor - intersection
difference_b = b_sensor - intersection
print(f"공통 : {intersection}")
print(f"A만  : {difference_a}")
print(f"B만  : {difference_b}")


print("=== 실습 : 두 시점의 이벤트 센서 추적하기 ===")
yesterday_error = {"S02", "S03"}
today_error = {"S02", "S03", "S05"}
difference = today_error - yesterday_error
intersection = today_error & yesterday_error
print(f"신규 이상 : {difference} \n지속 이상 : {intersection}")
