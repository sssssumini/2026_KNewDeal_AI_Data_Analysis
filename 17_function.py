# 함수


def say_hello():
    print("안녕하세요 ")


say_hello()


def show_number():

    my_number = 44
    print(my_number)


show_number()

# 함수안의 my_number 데이터가 영향을 끼치는 범위를 전문용어로 스코프(scope)라고 함.

print("=== 실습 : 첫 함수 만들고 호출하기 ===")


def start_checking():
    print("점검을 시작합니다")


start_checking()
start_checking()


def show_counting():
    count = 0
    print(count)
    count += 1


show_counting()
show_counting()


# 각 함수의 이름은 이름에 걸맞는 역할만 해줘야 한다.
def show_student():
    print("학생 1 : 리락쿠마")
    print("학생 2 : 차이로이코구마")


def show_teacher():
    print("선생님 : 키이로이토리")


def show_classroom():
    show_student()
    show_teacher()


show_classroom()

print("=== 실습4 : 함수로 설비 점검 자동화하기 ===")


def print_line():
    print("=" * 30)


def print_check(sensor):
    print(f"{sensor} 점검 안내 출력")


print_line()
print_check("Sensor A")

print_line()
print_check("Sensor B")


def say_hi(name):
    print(f"반갑습니다 {name}")


name_list = ["Ned", "Layla", "Jake", "ddu"]
for i in name_list:
    say_hi(i)


print("=== 실습2  : 다중 매개변수로 센서값 계산하기 ===")


def sensor_measure(sensor, temp):
    print(f"{sensor}의 온도는 {temp}도 입니다. ")


sensor_measure("모터", 78)
sensor_measure(92, "펌프")

print("\n=== 실습3 : 키워드 인자로 함수 호출하기 ===")


def sensor_measure(sensor, temp):
    print(f"{sensor}의 온도는 {temp}도 입니다. ")


sensor_measure("모터", 78)
sensor_measure(temp=80, sensor="펌프")

print("\n=== 실습4 : 반환값으로 간단 계산기 만들기 ===")


def simple_cal(num1, ope, num2):
    ans = 0
    if ope == "+":
        ans = num1 + num2
    elif ope == "-":
        ans = num1 - num2
    elif ope == "*":
        ans = num1 * num2
    elif ope == "/":
        ans = num1 / num2
    return ans


cal1 = simple_cal(80, "+", 38)
print(f"80+38={cal1}")
cal2 = simple_cal(cal1, "*", 3)
print(f"{cal1}*3={cal2}")


print("\n=== 실습5 : 센서 통계 함수 만들기 ===")


def min_max_avg(measure_list):
    measure_list.sort()
    min_measure, max_measure = measure_list[0], measure_list[-1]
    avg = round(sum(measure_list) / len(measure_list), 2)
    return min_measure, max_measure, avg


measure_sensors = [80, 20, 370, 400, 88]
ans1, ans2, ans3 = min_max_avg(measure_sensors)
print(ans1, ans2, ans3)

print("\n=== 실습6 : 처리 흐름 만들기 ===")


def avg_making(sensors):
    avg = round(sum(sensors) / len(sensors), 2)
    return avg


def decision_normal(avg_temp):
    if avg_temp > 90:
        state = "고온"
    elif avg_temp > 70:
        state = "정상"
    else:
        state = "저온"
    return state


temp1 = [20, 77, 93]
temp2 = [88, 90, 99]
print(f"{temp1} 평균 : {avg_making(temp1)} -> {decision_normal(avg_making(temp1))}")
print(f"{temp2} 평균 : {avg_making(temp2)} -> {decision_normal(avg_making(temp2))}")

print("\n=== 실습7 : 센서 분석 함수 세트 만들기 ===")


def avg_making(sensors):
    avg = round(sum(sensors) / len(sensors), 2)
    return avg


def decision_normal(avg_temp):
    if avg_temp > 90:
        state = "고온"
    elif avg_temp > 70:
        state = "정상"
    else:
        state = "저온"
    return state


temp1 = [20, 77, 80]
temp2 = [88, 80, 83]
print(f"{temp1} 평균 : {avg_making(temp1)} -> {decision_normal(avg_making(temp1))}")
print(f"{temp2} 평균 : {avg_making(temp2)} -> {decision_normal(avg_making(temp2))}")
