# == 실습 : 설비 정보 출력 카드 만들기 ==
print("== 실습 : 설비 정보 출력 카드 만들기 ==\n")

code = "PUMP_A"
state = "정상"
time = int(1200)
check = "2026-07-16"

print(f"설비: {code}\n상태: {state}\n가동: {time}\n점검: {check}")

# == 실습 : [:n] start 생략 ==
print("\n== 실습 : [:n] start 생략 ==")

sen = "temp_sensor"
print(sen[:4])

# == 실습 : [:n] end 생략 ==
print("\n== 실습 : [:n] end 생략 ==")

sen = "temp_sensor"
print(sen[5:])

# == 실습 : [-n:] 음수 슬라이싱 (뒤 n글자) ==
print("\n== 실습 : [-n:] 음수 슬라이싱 (뒤 n글자) ==")

sen1 = "sensor_01"
print(sen1[-2:])

# == 실습 : step으로 건너뛰기 ==
print("\n== 실습 : step으로 건너뛰기 ==")

sen2 = "Justin_Bieber_coachella"
print(sen2[::2])

# == 실습 : 문자열 뒤집기 ==
print("\n== 실습 : 문자열 뒤집기 ==")

sen2 = "Justin_Bieber_coachella"
print(sen2[::-1])

# == 실습 : len()으로 길이재기 ==
print("\n== 실습 : len()으로 길이 ==")

num = "373722919383225839"

print(f"{num}의 자릿수는 {len(num)} 입니다")

# == 실습 : in으로 포함 확인 ==
print("\n== 실습 : in으로 포함 확인 ==")

msg = "설비 고장 발생"
print(f"고장 in {msg} is {"고장" in msg} / 정상 in {msg} is {"정상" in msg}")

# == 실습 : count()로 개수 세기 ==
print("\n== 실습 : count()로 개수 세기 ==")

sen3 = "a,b,c,d"
print(sen3.count(","))

# == 실습 : find()로 위치 찾기 ==
print("\n== 실습 : find()로 위치 찾기 ==")

sen4 = "a,b,c,d"
print(sen4.find(","))
print(sen4.find("p"))
