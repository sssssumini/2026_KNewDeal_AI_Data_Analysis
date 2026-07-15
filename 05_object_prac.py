# == 실습 1 : 여러 자료형 변수 ==
print("== 실습 1 : 여러 자료형 변수 ==")
count = 30  # 정수형
temp = 88.12  # 실수형
name = "moka"  # 문자열
is_ok = False  # 불린
print(count, temp, name, is_ok, "\n")

# == 실습 2 : type()으로 자료형 확인하기 ==
print("== 실습 2 : type()으로 자료형 확인하기 ==")
print(count, "type :", type(count))
print(temp, "type :", type(temp))
print(name, "type :", type(name))
print(is_ok, "type :", type(is_ok))

# == 실습 3 : 자료형 맞히기 퀴즈 ==
print("\n== 실습 3 : 자료형 맞히기 퀴즈 ==")
print(100, "type :", type(100))  # 정수형
print(100.0, "type :", type(100.0))  # 실수형
print("100", "type :", type("100"))  # 문자열

# == 실습 4 : 문자열 숫자와 숫자 비교하기 ==
print("\n== 실습 4 : 문자열 숫자와 숫자 비교하기 ==")
print(382 + 212)  # 594
print("382" + "212")  # 382212
print("88" + "77")  # 8877

# == 실습 5 : bool값 만들어 확인하기 ==
print("\n== 실습 5 : bool값 만들어 확인하기 ==")
print(3 > 2)  # True
print(5 == 5)  # True
print(type(3 > 2))  # <class 'bool'>

# == 실습 6 : 변수의 자료형 변경하기 ==
print("\n== 실습 6 : 변수의 자료형 변경하기 ==")
num = 8
print(num, "type:", type(num))  # 정수형

num = 88.8
print(num, "type:", type(num))  # 실수로 재할당 후 출력

num = "문자열"
print(num, "type:", type(num))  # 문자로 재할당 후 출력


# == 실습 7 : 직접 자료형 표현하기 ==
print("\n== 실습 7 : 직접 자료형 표현하기 ==")
device_temp = 80.5  # 실수
check_count = 5  # 정수
device_name = "macbook air"  # 문자열
is_normal = False  # bool
