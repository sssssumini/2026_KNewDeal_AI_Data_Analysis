# 학생들의 점수를 가져와서 각 학생별 합계와 모든 학생들의 평균 점수를 내는 코드'
# 최고점, 최저점 학생 출력
# 각 과목별 평균도 출력해보세요

import os
import sys
import csv

# 1. 파일을 연다
# 2. 파일 내용으로부터 리스트 데이터를 얻는다
# 3. 점수계산 (합계, 평균)
# 4. 결과 화면에 보여주기

file_path = os.path.join("data", "student_scores.csv")

if not os.path.exists(file_path):
    print("파일을 찾지 못했습니다.")
    sys.exit(1)

total_score = 0
student_count = 0
total_kor, total_eng, total_math = 0, 0, 0
max_score = [None, None]
min_score = [None, None]
with open(file_path, "r", encoding="utf-8") as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        name = row.get("\ufeff이름", "(이름없음)")
        kor = int(row.get("국어", "0"))
        eng = int(row.get("영어", "0"))
        math = int(row.get("수학", "0"))

        student_avg = round((kor + eng + math) / 3, 2)
        total_score += student_avg
        student_count += 1

        total_kor += kor
        total_eng += eng
        total_math += math

        if student_count == 1:  # 학생 수가 1일때로 min, max 초기값 설정
            max_score[0] = name
            max_score[1] = student_avg
            min_score[0] = name
            min_score[1] = student_avg
        else:
            if max_score[1] < student_avg:
                max_score[0] = name
                max_score[1] = student_avg
            if min_score[1] > student_avg:
                min_score[0] = name
                min_score[1] = student_avg


print(f"전체 {student_count}명의 평균은 {round(total_score/student_count,2)}")
print(f"국어 과목의 평균 점수는 {round(total_kor/student_count,2)}")
print(f"수학 과목의 평균 점수는 {round(total_math/student_count,2)}")
print(f"영어 과목의 평균 점수는 {round(total_eng/student_count,2)}")
print("=" * 30)
print(f"최고점 학생은 {max_score[0]}, {max_score[1]}점 입니다.")
print(f"최저점 학생은 {min_score[0]}, {min_score[1]}점 입니다.")
