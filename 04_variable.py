print("\n")
# 변수 선언 방법
# 변수이름 = 값
# 오른쪽 값을 왼쪽 이름에 "저장"하라는 코드

temp = 36  # 숫자로 저장하고 싶다면 따옴표 금지
name = "센서 A"  # 문자로 저장하고 싶다면 따옴표 필요

print(temp, name)
print("temp")

# = "같다"가 아니라 "저장"하는 것
# 비교는 == 을 사용

# ===============================================
print("\n===== 변수 사용 활용 =====")

# 변수를 재할당할 때 변수 기존 자신의 값을 활용할 수 있음
# 변수에 할당할 때 오른쪽 값을 계산하여 할당됨
x = 5
x = x + 5
# y = y+5
# # 오류 발생, y가 정의되지 않았기 때문

print(x)  # 10

print("\n===== 변수 재할당 =====")

print("재할당 전 temp:", temp)
temp = 15  # 위에서 할당했던 36이라는 값을 15로 재할당(수정)
Temp = 15  # 대소문자 구분, temp와 Temp는 다른 변수
print("temp:", temp, "Temp:", Temp)

print("\n")
# 재할당은 지금까지 실행된 가장 최근의 값으로 바뀌게 됨
score = 10
print(score)  # 10
score = 20
score = 30
print(score)  # 30


print("\n===== 값 복사 =====")

a = 10
b = a  # a의 값을 b에 복사 (저장할 때의 그 순간의 a값을 b에 저장)
a = 100  # a의 값을 재할당해도 b 변수의 값은 변하지 않음 (10유지)
print("a:", a, "b:", b)  # a: 100 b: 10

print("\n===== 여러 변수 한 번에 선언 및 할당 =====")

# 형식 : 변수1, 변수2, ... = 값1, 값2, ... << 변수와 값의 개수가 같아야 함

width, height = 10, 20  # width에는 10, height에는 20이 할당됨
print("width:", width, "height:", height)

# x, y, z = 1, 2
# ValueError: not enough values to unpack (expected 3, got 2)
# 변수 3개를 선언했는데 값은 2개만 할당하려고 해서 오류 발생

print("\n===== 주석으로 변수 설명 =====")

# 변수 이름과 역할에 대한 설명을 주석으로 추가

temp = 25  # 온도(섭씨)
count = 3  # 센서 개수
# temp = 10000000000000000 # 주석처리된 코드는 동작하지 않음
print(temp)

print("\n===== 실습 : 변수 만들고 출력하기 =====")
temperature = 30
print(temperature)  # 변수 이름 변경시 print안의 변수 이름도 변경 필요

name = "센서 A"
print(name)


print("\n===== 실습 : 직접 변수 만들어 출력하기 =====")

# 숫자 변수 만들어서 출력
my_number = 88
print(my_number)

# 문자 변수 만들어서 출력
mood = "chill"
print(mood)

print("\n===== 실습 : 나이, 점수, 개수 변수로 표현 =====")

age = 25  # 숫자 변수 만들기
label = "나이"  # 설명용 글자 변수

# label과 age 이어서 출력
print(label)
print(age)


print("\n===== 실습 : 변수 값 바꿔가며 추적하기 =====")

x = 10
print(x)  # 10

x = x + 5
print(x)  # 15

x = x * 2
print(x)  # 30

print("\n===== 실습 : 두 변수 값 옮기고 바꾸기 =====")

a = 100
b = a  # b에 a의 값이 100일때 할당되어 b는 100이 됨
a = 999
print("a:", a, "b:", b)  # a: 999 b: 100

print("\n===== 실습 : 일부러 오류 내고 고치기 =====")

# print(temp) # NameError temp라는 변수가 선언되지 않아서 오류 발생 > 해결책 : temp 변수 선언 후 출력

temp = 25
print(temp)  # 변수를 미리 선언했기 때문에 오류없이 출력

score = 90
# print(Score)
# NameError: name 'Score' is not defined >> 해결책 : Score라는 변수를 다시 할당하거나 대소문자를 맞춰서 다시 출력
print(score)

print("\n===== 실습 : 주석으로 변수 설명 달기 =====")

temp = 25  # 온도(섭씨)
count = 3  # 센서 개수

# temp = 100
# 주석처리된 코드는 동작하지 않음

print(temp)  # temp = 100은 주석처리 되었기 때문에 25가 출력됨

print("\n===== 실습 : 값 예측 미니퀴즈 =====")

x = 5
x = 10
x = x + 1  # 이전 할당된 값이 10이므로 11이 됨

print(x)  # 11

print("\n===== 실습 : 정보 카드 만들기 (종합) =====")

# 자기소개 카드
name = "김수민"  # 이름 변수
city = "광양"  # 고향 변수
age = 25  # 나이 변수

print("=== 자기소개 카드 ===")  # 문자열만 출력
print(name)  # 변수만 출력
print("고향: ", city)  # 문자열과 변수 함께 출력
print("나이:", age)

print("\n===== 실습 : 변수 이름 다듬기 =====")

a, b = 25, 3  # 의미없는 변수 이름은 식별 어려움
temp, count = 25, 3  # 값의 의미를 영어단어로 옮기기
device_temp = 25  # 여러단어는 밑줄로 잇기

print(device_temp)  # 25

print("\n===== 실습 : 변수 한 줄 만들기 도전 =====")

x, y, z = 1, 2, 3  # 변수 세개를 동시에 선언
width, height = 4, 3  # 변수 두개를 동시에 선언

# 값 확인
print(width)
print(height)

# 주의할 점 : 변수 개수와 값의 개수가 같아야 함
