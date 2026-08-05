from math import sqrt

print(sqrt(16))
# print(sin(180))

import math

print(math.sin(180))

import math as mt

print(mt.tan(180))

import datetime

now = datetime.datetime.now()
print(now)

print("=== 실습 1 : import 세 방식으로 모듈 가져오기 ===")

import math

print(math.sqrt(16))

from math import sqrt

print(math.sqrt(16))

import math as mt

print(mt.sqrt(16))

# math 표준 라이브러리
import math

print(dir(math))  # dir(module) : module에 있는 함수값 호출
print(math.sqrt(9))
print(math.ceil(4.2))  # 올림
print(2**3)  # 2의 3승

# sqrt, ceil 만 쓸 경우 이렇게 사용해도 됨
from math import sqrt, ceil

print(math.sqrt(math.ceil(15.3)))

print("=" * 20)

# random module
import random

print(random.randint(1, 100))  # 1부터 100 중 랜덤으로 하나를 뽑아서 return

# while 1:
#     a = random.randint(1, 100)
#     if a == 77:
#         break
#     elif a < 50:
#         print("a")
#     else:
# print("b")
print(random.choice(["정상", "경고", "위험"]))  # 리스트 안의 값 중 랜덤으로 골라서 호출

# 표준 라이브러리의 datetime module
now = datetime.datetime.now()

sensor = []
for i in range(10):
    sensor.append(random.randint(1, 100))
    print(round(math.sqrt(sensor[i]), 2))


print("=== 실습 1 : import 세 방식으로 모듈 가져오기 ===")

import math 
print(math.sqrt(16))

from math import sqrt
print(math.sqrt(16))

import math as m
print(m.sqrt(16))


print("=== 실습 2 : 표준 라이브러리로 센서값 만들기 ===")
import random
for i in range(5) :
    sensor = random.randint(1,100)
    sensor_sqrt = math.sqrt(sensor)
    print(sensor, sensor_sqrt)

print("=== 실습 4 : os로 파일 존재확인하기 ===")
import os 

folder = "/Users/<username>/<folder_path>"  # Replace with your actual folder path  
filename = "08_press.csv"

path = os.path.join(folder, filename)
print(os.path.exists(path))


print("=== 실습 5 : datetime으로 점검 기록 남기기 ===")
import datetime
file_count = len(os.listdir(folder))
present_time = datetime.datetime.now()

print(f"파일 개수 : {file_count}, 점검 시각 : {present_time}")

print("=== 실습 3 : os로 폴더 목록 살펴보기 ===")
present_directory = os.getcwd()
my_file = os.listdir(present_directory)
 
for i in my_file:
    if i.endswith(".csv") == True :
        print(present_directory, i)
