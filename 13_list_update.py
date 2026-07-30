print("=== 실습 : 조건에 맞는 값만 출력하기 ===")

temp = [20, 31, 33, 19, 16, 35, 36, 38]
for i in temp:
    if i >= 30:
        print(f"고온 : {i}")


print("=== 실습 : 두 조건을 모두 만족하는 값 고르기 ===")
run_hours = [10, 20, 30, 40, 5, 4, 3]
for i in run_hours:
    if i >= 5 and i <= 10:
        print(f"{i}")


print("=== 실습 : 조건에 맞는 값만 골라 평균 구하기 ===")
temp = [20, 31, 33, 19, 16, 35, 36, 38]
total = 0
count = 0
for i in temp:
    if i > 30:
        total += i
        count += 1

print(f"고온 평균 : {(total/count):.2f}")

print("=== 실습 : 조건에 맞는 값으로 새 리스트 만들기 ===")
temp = [20, 31, 33, 19, 16, 35, 36, 38]
new = []

for i in temp:
    if i > 30:
        new.append(i)

print(f"{new}, 개수 : {len(new)}")

print("=== 실습 : 값을 가공해 새 리스트 만들기 ===")
temp = [20, 31, 33, 19, 16, 35, 36, 38]
new = []

for i in temp:
    new.append(round(i * 1.8 + 32, 1))

print(new)

print("=== 실습 : 센서 데이터 종합 분석하기 ===")

temp = [20, 31, 33, 19, 16, 35, 36, 38]
total = 0
high_temp = []

for i in temp:
    total += i
    if i > 30:
        high_temp.append(i)

temp_avg = round(total / len(temp), 1)
high_temp_avg = round(sum(high_temp) / len(high_temp), 1)

print(
    f"전체 평균 : {temp_avg}, 고온 개수 : {len(high_temp)}, 고온 평균 : {high_temp_avg}"
)
