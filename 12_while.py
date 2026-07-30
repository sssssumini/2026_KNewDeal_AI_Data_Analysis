# print("=== 실습 : while로 목표값 도달까지 반복하기 ===")

# ans = 77
# inp = 0
# while inp != ans:
#     inp = int(input("숫자를 입력하세요 : "))

# if inp == ans:
#     print("정답입니다.")

# print("=== 실습 : up down 게임 만들기 ===")

# ans = 30
# inp = 0
# while True:
#     inp = int(input("숫자를 입력하세요 : "))
#     if inp > ans:
#         print(f"입력하신 {inp}이 답보다 큽니다. 다시")
#     elif inp < ans:
#         print(f"입력하신 {inp}이 답보다 작습니다. 다시")
#     else:
#         print("정답입니다. 게임이 종료되었습니다.")
#         break

# print("=== 실습 : 플래그로 조건 만족 값 검색하기 ===")

# flag = False
# count = int(input("횟수를 입력하세요 : "))

# for i in range(count):
#     temp = float(input("측정값을 입력하세요 : "))
#     if temp > 80:
#         flag = True
#         break

# if flag == True:
#     print("발견")
# else:
#     print("없음")

# print("=== 실습 : 조건에 맞는 값만 출력하기 ===")

# temp = [20, 31, 33, 19, 16, 35, 36, 38]
# for i in temp:
#     if i >= 30:
#         print(f"고온 : {i}")


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
