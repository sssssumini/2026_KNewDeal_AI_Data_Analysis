# for 문
# for i in range(범위):

print("\n=== 실습 : range로 숫자 흐름 출력하기 ===")

N = int(input("enter number : "))
for i in range(1, N + 1):  # N까지 출력하려면 N+1
    print(i, end=" ")
print()
for i in range(2, N + 1, 2):
    print(i, end=" ")
print()
for i in range(N, 0, -1):
    print(i, end=" ")


print("\n=== 실습 : 369 게임 ===")

num = input("enter number : ")
for i in range(1, int(num) + 1):
    count_365 = str(i)
    count = count_365.count("3") + count_365.count("6") + count_365.count("9")
    if count == 0:
        print(i, end=" ")
    else:
        print("👏" * count, end=" ")
    if i % 10 == 0:
        print("")

print("\n=== 실습 : 3의 배수 출력하기 ===")

num2 = int(input("enter number : "))
print(num2)
for i in range(1, num2 + 1):
    if i % 3 == 0:
        print(i, end=" ")
print("")
num = input("숫자를 입력하세요 > ")
count = 0

enumerate : 낱낱이 세다
enumerate의 인자는 자료형 list, set, tuple, dictionary, string
index, value 값 반환

for i in enumerate("string"):
    print(i, end=" ")
""" 인덱스 값과 문자값 튜플로 반환
(0, 's')
(1, 't')
(2, 'r')
(3, 'i')
(4, 'n')
(5, 'g')
"""
print("")
for i, alp in enumerate("hello"):
    print(alp, end=" ")
print("")


# "안녕"의 인덱스 출력
li = ["안녕", "hi", "hi" "안녕", "hi", "안녕"]
for i in range(len(li)):
    if li[i] == "안녕":
        print(i, end=" ")

print("")
for ind, sen in enumerate(li):
    if sen == "안녕":
        print(ind, end=" ")

print("")

print("\n=== 실습 : 짝수단 구구단 출력 ===")

for i in range(2, 9, 2):
    for j in range(1, 10):
        print(f"{i}*{j} = {i*j}", end=" ")
    print("")

print("")
for i in range(1, 10):
    if i % 2 == 0:
        for j in range(1, 10):
            print(f"{i}*{j} = {i*j}", end=" ")
        print("")
