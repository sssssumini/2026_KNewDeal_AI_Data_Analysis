# # 트레이스백으로 에러 읽기

# # 정상
# temp = int("20")
# print(temp)

# # ValueError : 글자를 숫자로 변환 요구 -- 당연히 실패
# # temp_error = int("스물")
# # valueerror: invalid literal for int() with base 10:
# # print(temp_error)

# # ZeroDivisionError : 숫자는 0으로 나눌 수 없다는 에러
# # result = 10/0
# result = 10 / 3
# print(result)

# temp = -1
# try:
#     temp = int("스물")
# except:
#     print("해봤는데 안되네요")
#     temp = 0  # 문제가 있어도 앞으로 잘 진행될 수 있도록 대안/추가 처리 필요

# print(temp)

# # 실습 2 : 예외처리
# origin = input("온도 : ")
# print(f"입력한 온도는 {origin}")

# temp = 0
# try:
#     temp = int(origin)
# except ValueError:
#     # Valueerror인 상황이었다면 여기로 예외처리
#     print("숫자 아니면 왜 저를 부르셨어요?")

# next_temp = temp + 10
# print(f"10도만 더 높으면 {next_temp}")

# # 실습 3 : 구체적 예외로 입력 검증하기
# number = input("숫자를 입력하세요 : ")
# try:
#     number_to_int = int(number)
# except ValueError:
#     print("숫자만 입력하세요.")

# number2 = input("100을 나눌 수를 입력하세요 : ")
# try:
#     number2_to_int = int(number2)
#     answer = 100 / number2_to_int
#     print(f"100을 {number2_to_int}로 나누면 {round(answer,2)} 입니다.")
# except ValueError:
#     print("정수만 입력하세요.")
# except ZeroDivisionError:
#     print("0이 아닌 정수를 입력하세요")


# # 실습 1 : finally로 파일 안전하게 닫기
# import csv
# import os

# file_name = input("What is your file name? ")
# csv_path = os.path.join("data", file_name) # 경로 지정
# try :
#     f = open(csv_path, "r", encoding="utf-8")
#     csv_reader = csv.reader(f)
#     for row in csv_reader:
#         print(row)
# except FileNotFoundError:
#     print("파일이 없습니다.")
# finally :
#     print("파일을 닫습니다.")
#     f.close()


# 반복문 안에서 예외처리
my_list = ["123", "456", "영ㅋㅋ", "32", "54", "늙ㅋㅋ", "배고프다"]

# 문제 발생 경우를 세어봅시다
problems = 0

for i in my_list:
    # 반복을 하는 중에 문제가 생긴 경우만 건너뛰고 계속 반복을 이어서 진행시키기
    try:
        my_number = int(i)
    except:
        # print("문제발생")
        problems += 1
        continue

    print(my_number)

print(f"{len(my_list)}개 중 {problems}개의 문제 발생")

# [실습 2] 반복문에서 불량 줄 건너뛰기
# 소숫점 이하의 숫자가 포함된 숫자들을 20개 만들어 문자열 list에 담아주세요 "123.45"
# 그 사이에 엉뚱한 글자들이 포함된 내용도 포함 "영ㅋㅋ"
# 위 list 데이터를 사용해서 문제 풀이

float_list = [
    "123.45",
    "373.33",
    "203.3",
    "영ㅋㅋ",
    "3.22",
    "2.234",
    "소수점",
    "293.33",
    "111.23",
    "28.33",
    "123.45",
    "373.33",
    "203.3",
    "쭌과십수백수만수",
    "3.22",
    "2.234",
    "소수점",
    "293.33",
    "111.23",
    "28.33",
]

total_num = 0
for i in float_list:
    try:
        my_num = float(i)
        total_num += my_num
    except ValueError:
        continue
print(f"리스트 안의 실수값의 합계는 {total_num}")


# [실습 3] 여러 파일 묶어 처리하기
# 다음과 같은 식의 리스트를 만들어 반복문으로 처리해봅시다.
# for문으로 리스트의 문자열을 꺼내어 해당 이름의 파일들을 열어보기 시도
import os

count = 0
files = [
    "08_press.csv",
    "hi.csv",
    "09_ict_inspection.csv",
    "practice.csv",
    "쭌과만만수.csv",
]
for i in files:
    csv_path = os.path.join("data", i)  # 경로 지정
    try:
        f = open(csv_path, "r", encoding="utf-8")
        count += 1
    except FileNotFoundError:
        continue
    finally:
        f.close()

print(f"총 {len(files)}개의 파일 중 {count}개 열기 성공!")

# [실습 4] 함수 안에서 입력값 검증받기 
