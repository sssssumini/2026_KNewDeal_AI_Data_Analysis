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

# index()와 find() 차이 <- 없을 때 index는 오류 발생, find는 -1 return

email = "hong@gmail.com"
at = email.find("@")
user_id = email[:at]
print(user_id)
