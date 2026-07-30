print("=== 실습 : while로 목표값 도달까지 반복하기 ===")

ans = 77
inp = 0
while inp != ans:
    inp = int(input("숫자를 입력하세요 : "))

if inp == ans:
    print("정답입니다.")

print("=== 실습 : up down 게임 만들기 ===")

ans = 30
inp = 0
while True:
    inp = int(input("숫자를 입력하세요 : "))
    if inp > ans:
        print(f"입력하신 {inp}이 답보다 큽니다. 다시")
    elif inp < ans:
        print(f"입력하신 {inp}이 답보다 작습니다. 다시")
    else:
        print("정답입니다. 게임이 종료되었습니다.")
        break

print("=== 실습 : 플래그로 조건 만족 값 검색하기 ===")

flag = False
count = int(input("횟수를 입력하세요 : "))

for i in range(count):
    temp = float(input("측정값을 입력하세요 : "))
    if temp > 80:
        flag = True
        break

if flag == True:
    print("발견")
else:
    print("없음")
