import pandas as pd
import os

pd.set_option("display.unicode.east_asian_width", True)

# 실습 1. value_counts로 빈도 세기
print("\n=== 실습 1. value_counts로 빈도 세기 ===")

sensor = pd.read_csv("data/14_equipment_sensor.csv")

sensor.info()
print(sensor.head())
print(sensor.columns)

print("=" * 15)
print(sensor.value_counts("line"))
print(sensor.value_counts("shift"))


# 실습 2. 비율과 불균형 데이터
print("\n=== 실습 2. 비율과 불균형 데이터 ===")
hyd = pd.read_csv("data/14_hydraulic.csv")
print(hyd.head())
print(hyd.columns)

print(hyd.value_counts("result"))
print(hyd.value_counts("result", normalize=True).round(3))

# 실습 3. 구간으로 묶어 세기
print("\n=== 실습 3. 구간으로 묶어 세기 ===")
print(hyd["진동"].max(), hyd["진동"].min())
fre = pd.cut(hyd["진동"], bins=3, labels=["낮음", "보통", "높음"])
print(fre.value_counts())

print()
print("=" * 15, "선택문제", "=" * 15)

# 선택 문제
student = pd.read_csv("data/students_groupby_practice.csv")
student.info()
print(student.columns)
print(student.head(3))

# [문제 1] 이 학교의 전체 학생 수를 구하세요. (힌트: len 또는 shape)
num_student = len(student)
print(f"\n전체 학생 수 : {num_student}")

# [문제 2] 학년별 학생 수를 구하세요. (힌트: groupby + count 또는 size)
stu_by_grade = student.groupby("학년")["반"].size()
print(f"\n학년 별 학생수")
print(stu_by_grade)

# [문제 3] 학년 내 각 반별 학생 수를 구하세요. (힌트: 다중 컬럼 groupby)
stu_by_team = student.groupby(["학년", "반"])["반"]
print(f"\n학년 내 각 반별 학생 수")
print(stu_by_team.size())

# [문제 4] 각 반(학년, 반 조합)의 국어 점수 평균을 소수점 둘째 자리까지 구하세요.
kor = student.groupby(["학년", "반"])["국어"]
print(f"\n각 반(학년, 반 조합)의 국어 점수 평균")
print(kor.mean().round(2))

# [문제 5] 각 학년의 영어 점수 평균을 소수점 둘째 자리까지 구하세요.
eng = student.groupby("학년")["영어"]
print(f"\n각 학년의 영어 점수 평균")
print(eng.mean().round(2))

# [문제 6] 학교 전체의 수학 점수 평균을 소수점 둘째 자리까지 구하세요.
print(f"\n학교 전체의 수학 점수 평균")
print(student["수학"].mean().round(2))
