# error

print("\n==========NameError 만들기===========")
# print(NameError 만들기)
# SyntaxError 발생 (띄어쓰기가 있어서 변수 2개를 쉼표없이 작성했다고 판단)

# print(NameError만들기)
# NameError 발생 (변수 설정이 안되어있다고 판단)

print("NameError 만들기")
# 코드는 위에서 아래로 실행되기 때문에 위에서 에러 발생하면 그 이후 코드 실행 X

print("\n==========SyntaxError 만들기===========")
# print("온도) # 따옴표
# print("진동" # 괄호

print("온도")  # 따옴표
print("진동")  # 괄호


print("\n==========실습 : 오류 하나씩 고치기===========")
# print(온도, 75)  # NameError: name '온도' is not defined > 해결책 : 온도를 따옴표에 넣어 문자화
# print("진동", 2.3 # SyntaxError > 해결책 : 괄호
# print("압력": 4.0) # SyntaxError: invalid syntax > 해결책 : ":"를 따옴표 안에 넣고 콤마

print("온도", 75)
print("진동", 2.3)
print("압력:", 4.0)

print("\n========== 실습 : 점검 리포트 안내 ===========")
print("===== " + "1번 " + "설비 " + "점검 " + "=====")  # 문자열 합치기 "+" 활용
print("온도(℃):", 82)  # 정상온도, 문자와 숫자 한번에 출력
print("온도", "상승량:", 93 - 82)  # 연산자
