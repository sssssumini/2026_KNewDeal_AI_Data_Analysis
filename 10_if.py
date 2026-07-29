# if문 실습
# 사용자에게 나이를 입력받아 성인인지 출력하는 조건문 작성하기
age = int(input())
if age >= 20:
    print("당신의 나이는 성인입니다")
else:
    print("당신의 나이는 미성년자입니다")

# if문 실습2
# 숫자 맞추기 게임
# 정답은 임의로 지정
ans = 77
num = int(input("숫자를 입력하세요 :"))
if num == ans:
    print("정답입니다")
else:
    print("틀렸습니다.")

while True:
    num = int(input("숫자를 입력하세요 :"))
    if num == ans:
        print("정답입니다")
        break
    else:
        if num > ans:
            print(f"정답은 {num}보다 작습니다")
        else:
            print(f"정답은 {num}보다 큽니다")

# 신호등 색 입력받아 "Green" "Red" 출력
color = input("신호등 색 입력 :")
if color == "Green" or color == "초록" or color == "green":
    print(f"{color}색 입니다. 건너가세요.")
elif color == "Red" or color == "빨강" or color == "red":
    print(f"{color}색 입니다. 멈추세요.")
else:
    print("다시 입력하세요")

print("=== 실습 : 설비 온도 상태 판정하기 ===")
temp = [85, 70, 50]
for i in temp:
    if i >= 80:
        print(f"{i} -> 위험")
    elif i >= 70:
        print(f"{i} -> 주의")
    else:
        print(f"{i} -> 정상")

print("\n=== 실습 : 두 조건을 모두 만족하는지 검증하기 ===")
cor_id = "admin"
cor_pw = "1234"

id = input("아이디를 입력하세요 : ")
pw = input("비밀번호를 입력하세요 : ")
if (id == cor_id) and (pw == cor_pw):
    print(f"{id}/{pw} 로그인에 성공하였습니다.")
else:
    print(f"{id}/{pw} 로그인 실패")

print("\n=== 실습 : 세 값으로 설비 종합 상태 판정하기 ===")

temp = float(input("온도 : "))
fre = float(input("진동 : "))
volt = float(input("전류 : "))
if (temp > 80) or (fre > 4.0):
    print("위험 : 즉시 정지")
else:
    if (volt > 60) and (temp > 70):
        print("주의 : 부하 점검")
    elif fre > 2.5:
        print("주의 : 진동관찰")
    else:
        print("정상")
