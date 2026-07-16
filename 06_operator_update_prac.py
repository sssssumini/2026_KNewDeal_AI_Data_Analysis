# == 실습 1 : 사칙연산 계산기 ==
print("== 실습 1 : 사칙연산 계산기 ==")
a = 123
b = 23

print(a, "+", b, "=", a + b)
print(a, "-", b, "=", a - b)
print(a, "*", b, "=", a * b)
print(a, "/", b, "=", a / b)
print(a, "//", b, "=", a // b)
print(a, "%", b, "=", a % b)
print(a, "**", b, "=", a**b)

# == 실습 2 : 평균과 도형 계산 ==
print("== 실습 2 : 평균과 도형 계산 ==")
width = 30
length = 20
height = 55
print(
    "평균 =",
    (width + length + height) / 3,
    "넓이 =",
    width * length,
    "부피 =",
    width * length * height,
)

# == 실습 3 : 비교 연산 출력 ==
print("== 실습 3 : 비교 연산 출력 ==")

print(3 == 80)  # False
print(3 != 80)  # True
print(3 < 80)  # True
print(3 > 80)  # False
print(3 <= 80)  # True
print(3 >= 80)  # False


# == 실습 4 : 정상범위, 다중센서 판정 ==
print("== 실습 4 : 정상범위, 다중센서 판정 ==")

temp = 85
pressure = 5

is_ok_temp = (temp >= 60) & (temp <= 90)
is_ok_pressure = (pressure >= 3) & (pressure <= 7)


print(
    "온도정상 :",
    is_ok_temp,
    "\n압력정상 :",
    is_ok_pressure,
    "\n모두정상 : ",
    (is_ok_temp == True) & (is_ok_pressure == True),
)

# == 실습 5 : 복합할당으로 재고추적 ==
print("== 실습 5 : 복합할당으로 재고추적 ==")
inven = 100
inven += 50  # 150
inven -= 30  # 120
inven += 5  # 125
print(inven)  # 125

# == 실습 6 : 설비지표계산 ==
print("\n== 실습 6 : 설비지표계산 ==")
total = 500
bad = 23

bad_p = (bad / total) * 100

run = 21
total_run = 24

run_p = (run / total_run) * 100

print("불량률 :", bad_p, "%, 가동률 ", run_p, "%")


# == 실습 7 : 시간 변환, 상자 포장 ==
print("\n=실습 7 : 시간 변환, 상자 포장 ==")
minutes = 500
print(minutes, "분은", minutes // 60, "시간", minutes % 60, "분 입니다.")
