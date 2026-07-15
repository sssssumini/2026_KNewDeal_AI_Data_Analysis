# int - 정수형

count = 3
age = 20
tall = 180

# 0과 음수도 정수에 포함됨
zero = 0
temp = -30

# =================

# float - 실수형
# 소수점이 붙은 숫자
# 5.0처럼 딱 떨어지는 실수도 소수점이 있다면 무조건 float형임

tired = 99.99999
height = 17.2

# =================

# str - 문자열
# 띠옴표에 감싸진 모든 값

hello = "안녕하세요~"
emoji = "😳"
empty = ""  # 따옴표만 있고, 아무것도 작성되지 않아도 str
fake_num = "12345"
fake_num2 = "5.0"
# 따옴표 ", ' 둘 다 사용 가능한 이유 >> 문자열 안에 따옴표가 필요한 경우가 있기 때문
# 이럴 경우 사용하지 않는 따옴표로 쌍을 맞춰 바깥쪽에 감싸줘야 함
illit = "It's me"

# =================

# bool - 불리언형
# True 또는 False만
# 첫 글자는 대문자, 따옴표 없이 작성

ok = True
no = False

# 비교할 경우 bool로 출력
print(100 < 5)  # False
print(5 == 5)  # True

# =================

print("=== type() ===")

# type() : 자료형 확인

type(5)  # 터미널에서 확인 불가
print(type(5))  # <class 'int'>
print(type("센서A"))  # <class 'str'>
print(type(True))  # <class 'bool'>
print(type(3 > 2))  # <class 'bool'>

# 1. print 함수의 내부를 확인
# 2. print 함수에 또 함수가 있는 것을 확인하고 type 함수의 내부를 확인
# 3. type 함수의 내부에 연산자가 있는 것을 확인하고 연산 진행
# 4. 3>2의 연산 결과는 True기 때문에 type(True)로 바뀜
# 5. type(True)의 결과인 <class 'bool'>이 터미널에 출력

print(3, type(3))

num = 123
fake_num = "123"
str = "문자열"
ok = True
print(num, ">>>", type(num))
print(fake_num, ">>>", type(fake_num))
print(str, ">>>", type(str))
print(ok, ">>>", type(ok))

# =================

print("=== 자료형마다 동작이 다른 것 확인하기 ===")

print(3 + 5)
print("3" + "5")
print("안녕하" + "세요")  # 안녕하세요

print("=== 자주하는 실수 ===")
print(0.1 + 0.9)  # 가끔 컴퓨터 내부 연산 과정에서 아주 작은 오차가 발생하는 경우도 있음

print(round(0.1 + 0.8, 2))  # 소수 둘째 자리 반올림 >> 0.9 출력

# str과 int/float은 덧셈 불가
# print ("123" + 456) # TypeError발생

print(10 / 2)
print(type(10 / 2))
