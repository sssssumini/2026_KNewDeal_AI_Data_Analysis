# 여러줄 문자열

notice = """
설비 점검 안내
1. 전원 확인
2. 센서 점검 
"""

print(notice)  # ''' ''' 삼중 따옴표 사용 시 모든 줄바꿈이 적용됨

notice2 = "설비 점검 안내\n1. 전원 확인\n2. 센서 점검"
print(notice2)

alp = "abcdefghijklmnopqrstuvwxyz"
print(alp[18] + alp[20] + alp[12] + alp[8] + alp[13])

# len <- 문자열 길이 구하기

# in 활용
print("===== in 활용 =====")

# in <- 특정문자가 문자열에 포함되었는지 여부 확인 / bool
print("고장" in "설비 고장 발생")  # True
print("정상" in "설비 고장 발생")  # False
print("설비 중 고장" in "설비 고장 발생")  # False
print("설비 중 고장" in "설비 중 고장 발생")  # True

# not in
print("고장" not in "설비 고장 발생")  # False
print("정상" not in "설비 고장 발생")  # True
print("설비 중 고장" not in "설비 고장 발생")  # True
print("설비 중 고장" not in "설비 중 고장 발생")  # False

print(" " in "설비 중 고장")  # True
print(" " in "설비중고장")  # False

# count() <- 특정 ()가 몇번 나오는지 셈 / 없으면 0

# find() <- 특정 ()가 처음 나오는 위치 번호 반환 / 없으면 -1

sqe = "SQE-0909"
sp = sqe.find("-")
print(sqe[:sp])
sp_index = sqe.index("-")
print(sqe[:sp])

# index()와 find() 차이 <- 없을 때 index는 오류 발생, find는 -1 return
email = "hong@gmail.com"
at = email.find("@")
user_id = email[:at]
print(user_id)

at_index = email.index("@")  # 4

# 특정 문자열로 시작/끝 검사
# Ture/False 불리언

print("EQP-001".startswith("EQP"))
print("This is monday".endswith("Monday"))

# upper() : 전부 대문자
# lower() : 전부 소문자
# capitalize() : 첫글자 대문자
# title() : 각 단어의 첫글자 대문자

print("== strip() == ")
# strip() : 공백 제거
# lstrip() : 앞공백 / rstrip() : 뒷공백

sen = "    45   "
print(sen.strip(), "\n", sen.lstrip(), "\n", sen.rstrip())

print("===정==상===".strip("="))

print("=*=정==상==*".strip("="))
print("====정==상===".strip("===="))
print(
    "abcbadab정상abababab".strip("abc")
)  # strip() 메서드에 들어가는 문자열은 완벽히 같지 않아도 작동을 한다.

# strip("=") → = 문자를 양쪽 끝에서 제거
# strip("====") → = 문자만 양쪽 끝에서 제거(같은 결과)
# strip("abc") → a, b, c 중 하나라도 양쪽 끝에 있으면 계속 제거
# 문자열 "====" 자체를 제거하는 함수는 removeprefix() 또는 removesuffix()이다.

print("====정==상===".removeprefix("===="))
print("====정==상===".removesuffix("===="))

# replace("대체할문자", "바뀔문자") : 문자 대체

# split(sep="") 문자열 자르기
# 문자열 >> list

drinks = "에스프레소 아메리카노 카페라떼"
print(drinks.split())

fruits = "딸기,거봉,키위,망고,사쿠란보"
print(fruits.split(","))

# end = "" , sep = ""

print("2026", "07", "26", sep="살해")
