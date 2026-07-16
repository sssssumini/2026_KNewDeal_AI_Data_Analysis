# 산술연산자
# + - * / //(몫) %(나머지) **(거듭제곱)
print(3 + 5)
print(3842 - 33)
print(23 * 332)
print(2412 / 2)
print(2764 // 3)
print(2764 % 3)
print(2**3)

# 연산 우선순위와 우선순위 지정
# (**) -> (* / // %) -> (+ -)

print(2 + 8 * 3)
print((2 + 8) * 3)

# ===============
# 복합연산자
result = 3 * 5
print(result)

# *= += -= /= : 재할당 기호
result += 10  # 25
result -= 5  # 20
result *= 3  # 60
result /= 10  # 6.0

# ===============
# 문자열연산
print("안녕" + "하세요")  # 안녕하세요

# 공백추가 > 쉼표 또는 공백 추가, 공백만 있는 문자열 더하기
print("안녕", "하세요")
print("안녕 " + "하세요")
print("안녕" + " " + "하세요")

# 문자열 곱하기
print("안녕" * 5)  # 안녕안녕안녕안녕안녕

# ====================
print("=== 비교연산자 ===")

print(7 < 16)  # True
print(7 > 16)  # False
print(7 <= 16)  # True
print(7 >= 16)  # False
print(7 == 16)  # False
print(7 != 16)  # True

# 1. 대소문자구분
print("hello" == "Hello")  # False
# 2. 공백이 있어도 다르다고 판단
print("hello" == "hello ")  # False
# 3. 부정연산자
print("hello" != "hello")  # False

# 질문 1) hello 변수에 할당하는 값을 따옴표로 감싸지 않고 비교
# print("=== 질문 1) hello 변수에 할당하는 값을 따옴표로 감싸지 않고 비교 ===")
# hello = hi
# print(hello == hi)  # NameError(선언하지 않은 이름 호출했을 때)
# hi는 따옴표에 감싸져있지 않기 때문에 변수로 취급됨
# 그런데 우리는 hi 변수를 선언한 적이 없기 때문에 에러

# 질문 1) 해결방법
# print("=== 질문 1) 해결 방법 ===")
hi = "안녕"  # hello 변수에 hi 변수를 할당하기 전 hi 변수 선언
hello = hi  # print(hello) > 안녕
print("=== 변수 hello(안녕)와 변수 hi(안녕) 비교 ===")
print(hello == hi)  # True

# ==============================
# and / or / not : 논리연산자
# and :둘 다 참이면 True 반환
print(5 == 5 and 7 == 7)  # True
print(5 == 7 and 7 == 7)  # False
print(5 == 5 and 7 != 7)  # False

# or :둘 중 하나가 참이면 True 반환
print(5 == 5 or 7 == 7)  # True
print(5 == 7 or 7 == 7)  # True
print(5 == 5 or 7 != 7)  # True

# not : 값을 반대로 뒤집음
print(not True)
print(not 5==5)
