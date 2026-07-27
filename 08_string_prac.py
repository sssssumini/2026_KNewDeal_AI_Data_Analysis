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

# == 실습 : 시작과 끝 확인하기 ==
print("\n== 실습 : 시작과 끝 확인하기 ==")

sen5 = "sensor_log.csv"
print("sensor데이터인가요?", sen5.startswith("sensor"))
print("csv파일인가요?", sen5.endswith(".csv"))

# == 실습 : 대문자로 바꾸기 ==
print("\n== 실습 : 대문자로 바꾸기 ==")

sen6 = "ready"
sen6_up = sen6.upper()
print(sen6_up)

# == 실습 : 소문자로 바꾸기 ==
print("\n== 실습 : 소문자로 바꾸기 ==")

sen7 = "WARNING"
sen7_low = sen7.lower()
print(sen7_low)

# == 실습 : 대문자인지 소문자인지 검사하기 ==
print("\n== 실습 : 대문자인지 소문자인지 검사하기 ==")

sen = ["ABC", "abc", "Abc"]
print(sen[0].isupper())
print(sen[1].islower())
print(sen[2].isupper())

# == 실습 : 파일명 규칙 한번에 점검하기 ==
print("\n== 실습 : 파일명 규칙 한번에 점검하기 ==")

f = "Sensor_LOG.CSV"
f_low = f.lower()
print(f_low.startswith("sensor"), f_low.endswith("csv"))


# == 실습 : strip, 체이닝 ==
print("\n== 실습 : strip, 체이닝 ==")

str = "         Warning    "
str1 = str.lower()
str2 = str.lower().strip()
print("[" + str1 + "]")
print("[" + str2 + "]")

# == 실습 : 쉼표 기준으로 나누기 ==
print("\n== 실습 : 쉼표 기준으로 나누기 ==")

str3 = "a,b,c,d"
print(str3.split(","))

# == 실습 : 리스트 합치기 ==
print("\n== 실습 : 리스트 합치기 ==")

l1 = ["2025", "01", "15"]
print("-".join(l1))


word = "python"
print(word[:2] + word[2].upper() + word[3:])
print(
    word[: word.index("t")]
    + word[word.index("t")].upper()
    + word[word.index("t") + 1 :]
)
print(word.replace("t", "T"))

# == 실습 : 구분자 통째로 바꾸기 ==
print("\n== 실습 : 구분자 통째로 바꾸기 ==")

sen10 = "2026/7/26"
sen_split = sen10.split("/")
print("-".join(sen_split))
print(sen10.replace("/", "-"))

# == 실습 : CSV 한 줄에서 값 꺼내 정리하기 ==
print("\n== 실습 : CSV 한 줄에서 값 꺼내 정리하기 ==")

csv_8 = "1,NORMAL,25.3"
csv_8_split = csv_8.split(",")
print(csv_8_split[1].strip().lower())

# == 실습 : f-string으로 변수 끼워 출력하기 ==
print("\n== 실습 : f-string으로 변수 끼워 출력하기 ==")

sulbi = "PUMP_A"
temp = 87
print(f"설비 {sulbi}, 온도 {temp}도")
