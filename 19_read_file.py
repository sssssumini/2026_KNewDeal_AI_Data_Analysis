# 기본 내장함수인 open()으로 sample.txt 파일 열기
# 읽기 모드(r)로 열고, 인코딩은 utf-8로 지정
# 가져온 정보(파인 접근 열쇠, 참조값) f에 담는다

f = open("sample.txt", "r", encoding="utf-8")  

print(type(f).__name__) # 타입의 이름 : TextIOWrapper

lines = f.readlines() 
print(lines) # ['Hello World!!\n'] : 한 줄씩 읽어서 리스트로 반환

f.close() # 열었으면 반드시 닫기 !!

with open("sample.txt", "r", encoding="utf-8") as f:  # with 구문으로 열기
    # 앞으로 이렇게 들여쓰기 된 코드가 끝나면 자동으로 f.close()가 호출됨
    lines = f.readlines()
    print(lines)

f = open("hello.txt", "w", encoding="utf-8") 
f.write("안녕하세요")
f.write("\t반갑습니다\n")
f.write("하이룽\n")
f.close()


print("=== 실습 1 : open으로 파일 읽기 ===")
f2 = open("sample2.txt", "r", encoding="utf-8") 
f3 = open("sample2.txt", "r", encoding="utf-8") 
line = f2.read() # read로 읽고 나면 통채로 읽었기 때문에 바로 readlines()를 하면 빈 값이 반환됨
# f.seek(0) << 커서를 처음위치로 초기화
read_line = f3.readlines()
print(f"read : \n{line}")
print(f"readlines : \n{read_line}")

f2.close()
f3.close()

print("\n=== 실습 2 : with open으로 파일에 쓰기 ===")
with open("sample3.txt", "w", encoding="utf-8") as f4:
    f4.write("졸리다와 잠온다의 차이는 무엇일까 ?\n")

f5 = open("sample3.txt", "r", encoding="utf-8") 
f5_line = f5.read()
print(f5_line)
f5.close()

print("\n=== 실습 3 : a 모드로 이어 붙이기 ===")
with open("sample3.txt", "a", encoding="utf-8") as f4:
    f4.write("지금 되게 졸리다.")
f6 = open("sample3.txt", "r", encoding="utf-8") 
f6_line = f6.read()
print(f6_line)
f6.close()

