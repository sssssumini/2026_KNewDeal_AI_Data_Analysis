# 트레이스백으로 에러 읽기

# 정상
temp = int("20")
print(temp)

# ValueError : 글자를 숫자로 변환 요구 -- 당연히 실패 
# temp_error = int("스물")
# valueerror: invalid literal for int() with base 10: '%EC%8A%A4%EB%AC%BC'
# print(temp_error)

# ZeroDivisionError : 숫자는 0으로 나눌 수 없다는 에러 
# result = 10/0
result = 10/3
print(result)

temp = -1
try : 
    temp = int("스물")
except :
    print("해봤는데 안되네요")
    temp = 0 # 문제가 있어도 앞으로 잘 진행될 수 있도록 대안/추가 처리 필요

print(temp)

# 실습 2 : 예외처리
origin = input("온도 : ")
print(f"입력한 온도는 {origin}")

temp = 0
try:
    temp = int(origin)
except ValueError:
    # Valueerror인 상황이었다면 여기로 예외처리
    print("숫자 아니면 왜 저를 부르셨어요?")

next_temp = temp + 10
print(f"10도만 더 높으면 {next_temp}")

# 실습 3 : 구체적 예외로 입력 검증하기
number = input("숫자를 입력하세요 : ")
try :
    number_to_int = int(number)
except ValueError:
    print("숫자만 입력하세요.")

number2 = input("100을 나눌 수를 입력하세요 : ")
try :
    number2_to_int = int(number2)
    answer = 100 / number2_to_int
    print(f"100을 {number2_to_int}로 나누면 {round(answer,2)} 입니다.")
except ValueError :
    print("정수만 입력하세요.")
except ZeroDivisionError :
    print("0이 아닌 정수를 입력하세요")
