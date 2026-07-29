# list는 python 자료형 중 하나
# 여러 개의 값을 [대괄호] 에 감싸서 순서대로 저장
# 나열된 값들은 자동으로 각자의 인덱스 번호를 순서대로 가지게 됨

print("=== 실습 : 나만의 데이터 리스트 만들기 ===")
temp = [35, 33, 39, 40, 25]
print(f"temp = {temp}")
emp = []
print(f"temp = {len(temp)}개, emp = {len(emp)}개")

print("=== 실습 : 인덱스로 값 꺼내기 ===")
time_temp = [20, 24, 26, 28, 29, 36]
print(
    f"첫번째 값 : {time_temp[0]}, 세번째 값: {time_temp[2]}, 마지막 값 : {time_temp[-1]}"
)

print("=== 실습 : 인덱스로 꺼낸 값 계산하기 ===")
line = [123, 432, 2355, 267, 474, 2394]
line_a, line_b = line[0], line[-1]
print(f"합 : {line_a+line_b}, 중간값 : {(line_a+line_b)/2}")

print("=== 실습 : 슬라이싱으로 구간 자르기 ===")
temp = [20, 33, 44, 55, 66, 77, 88, 99, 102, 23]
print(temp[:3], len(temp[:3]))
print(temp[-3:])

print("=== 실습 : 데이터를 두 구간으로 나누기 ===")
num = [20, 33, 44, 55, 66, 77, 88, 99, 102, 23, 35, 112]
first = num[:6]
second = num[-6:]
print(first, second, len(first), len(second))


print("\n=== 실습 : 데이터를 두 구간으로 나누기 ===")
temp = [34, 35, 36, 37, 40, 240, 20]
print(240 in temp)
if 240 in temp:
    ind = temp.index(240)
    temp[ind] = 24

print(temp, 240 in temp)

# 주소값 할당
nums = [34, 35, 36, 37, 40, 240, 20]
new_nums = nums  # 단순 복사
# 복사한 메모리 주소에 값을 재할당 하게 되면 원본까지 영향을 받음
new_nums.append(3)
print(nums, new_nums)
nums.append(5)
print(nums, new_nums)

# 해결법
new_nums2 = nums.copy()  # 원본에 영향을 주지 않고 새로 저장
new_nums2.append(80)
print(nums, new_nums2)

# insert(a,b) : a번째에 b값 추가
# first.extend(second) : first리스트에 second리스트 합침

print("\n=== 실습 : 측정값 추가하기 ===")
emp = []
ready = [31, 32]
emp.append(3)
print(emp)
emp.insert(0, 10)
print(emp)
emp.extend(ready)
print(emp)

# remove() : 리스트에서 특정 값 제거
# pop() : 리스트에서 (인덱스) 해당 값 제거하고 그 값 반환
# del : 리스트 슬라이싱해서 제거 가능

print("\n=== 실습 : 잘못된 값 제거하기 ===")
test = [22, 33, 44, 55, 999]
print("제거 전: ", test)
test.remove(999)
print("remove: ", test)
print("꺼낸 값: ", test.pop(2))
del test[0]
print("del 제거: ", test)

# sorted() >> 오름차순
# sorted( , reverse = 1(True)) >> 내림차순 정렬
# reverse() : 리스트 순서 뒤집기
# count() : 개수 반환
# index() : 처음 ()가 등장하는 위치 반환

f = ["jake", "jay", "jake", "jay", "jake", "jay", "jake"]
count_jake = f.count("jake")
print(count_jake)

first_jay = f.index("jay")
print(first_jay)

print("\n=== 실습 : 정렬하고 탐색하기 ===")
temp = [22, 30, 56, 33, 12, 345, 53, 12, 12]
temp_sort = sorted(temp)  # 오름차순
print(f"원본 : {temp}, 오름차순 정렬 : {temp_sort}")
temp_rev = list(reversed(temp_sort))
print(f"원본 : {temp}, 뒤집어 정렬 : {temp_rev}")
count_12 = temp.count(12)
print(f"12의 개수는 {count_12}")
