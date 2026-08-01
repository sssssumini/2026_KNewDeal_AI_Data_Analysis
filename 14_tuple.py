# tuple : 값을 묶어주는 역할
# () 소괄호 안에 쉼표로 나누어서 여러가지 자료형의 값을 저장
# 그리고 마지막 값에서는 꼭 ,를 붙여야 python 이 tuple로 인식함
# 짝지어진 값을 하나로 묶을 때 사용 가능한 자료형

# 튜플의 기준
# 1. 값이 없는 경우 : ()필수
# 2. 튜플 안의 값이 1개
#  마지막에 ,를 적어줘야 튜플로 적용됨
# 3. 값이 두개 이상인 경우
# 쉼표 , 로 값이 구분되어있으면 튜플로 생성됨.
# 값의 자료형은 상관 x

# 튜플도 슬라이싱, 인덱싱 가능

# 튜플 언패킹
# 튜플에 담긴 값을 변수로 한 번에 분리
# 튜플은 수정 불가

unpacking = (
    1,
    2,
    3,
)
one, two, three = unpacking  # one, two, three 변수에 unpacking이라는 변수를 풀어서 저장

print(one, two, three)

test = [1, 2, 3, 4]
one, two, three, four = test
print(one, two, three, four)


print("=== 실습 : 센서를 튜플로 묶고 꺼내기 ===")

sensor = (
    "모터온도",
    78,
)
for i in range(len(sensor)):
    print(sensor[i])

motor, temp = sensor
print(motor, temp)


print("=== 실습 : 튜플 리스트를 반복 처리하기 ===")

sensor = [
    (
        "모터온도",
        78,
    ),
    (
        "회전속도",
        90,
    ),
    (
        "펌프압력",
        30,
    ),
    (
        "펌프속도",
        95,
    ),
]
for name, temp in sensor:
    if temp >= 90:
        print(name, "경고")

print("=== 실습 : 중첩 튜플로 센서 위치 관리하기 ===")

sensor = [
    (
        "모터",
        78,
        (5, 3),
    ),
    (
        "펌프",
        80,
        (7, 8),
    ),
    (
        "진동",
        90,
        (10, 2),
    ),
    (
        "보리차",
        91,
        (2, -1),
    ),
]

for name, temp, pos in sensor:
    x, y = pos
    if x <= 5:
        print(name, end=" ")
