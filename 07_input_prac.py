# # == 실습 1 : 이름을 입력받아 출력 ==
print("== 실습 1 : 이름을 입력받아 출력==")
name = input("이름을 입력하세요 :")

print("안녕하세요", name, "님")

# # == 실습 2 : 숫자 입력받아 계산하기 ==
print("\n== 실습 2 : 숫자 입력받아 계산하기 ==")
year = int(input("태어난 해를 입력하세요 :"))

print("올해 만", 2026 - year, "세")

# == 실습 3 : 여러 개의 값 입력받기 ==
print("\n== 실습 3 : 여러 개의 값 입력받기 ==")
country, city = map(
    str, input("거주 국가와 도시를 입력하세요. (ex. 한국 포항)").split()
)

print(country + "의 " + city + " 에서 거주하시는군요!")

# == 실습 4 : 두 수 입력받아 사칙연산 ==
print("\n== 실습 4 : 두 수 입력받아 사칙연산 ==")
a, b = map(int, input("숫자를 입력하세요 (ex. 23 43)").split())

print("합 :", a + b, "\n차 :", a - b, "\n곱 :", a * b, "\n나눗셈 ", round(a / b, 2))

# == 실습 5 : 입력값 비교해 출력하기 ==
print("\n== 실습 5 : 입력값 비교해 출력하기 ==")
temp = int(input("현재 온도 : "))

print("80 초과?", temp > 80)
print("0 이상?", temp >= 0)

# == 실습 6 : 입력, 변환, 계산, 비교, 출력 ==
print("\n== 실습 6 : 입력, 변환, 계산, 비교, 출력 ==")
sc1, sc2, sc3 = map(int, input("점수를 입력하세요 (ex. 23 43 80)").split())

avg = (sc1 + sc2 + sc3) / 3
print("평균 :", round(avg, 2), ", 60 이상?", avg >= 60)
