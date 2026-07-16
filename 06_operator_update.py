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
