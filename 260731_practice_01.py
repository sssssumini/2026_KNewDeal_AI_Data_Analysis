# =====================================================================
# 종합 실습 1. 설비 종합 모니터링 리포트
# 요구사항 자세히는 practice_guide.md 참고
# =====================================================================

sensors = [
    ("컨베이어_01", 78, 2.1),
    ("용접기_02", 92, 5.4),
    ("절단기_03", 85, 3.2),
    ("건조로_04", 101, 6.8),
    ("냉각탑_05", 67, 1.5),
    ("도장부스_06", 88, 4.1),
    ("성형기_07", 90, 2.9),
]
# (설비명, 온도, 진동)

# 판정 기준
#   온도 > 90 또는 진동 > 5.0  > "위험"
#   온도 >= 80 또는 진동 >= 3.0 > "주의"
#   그 외                      > "정상"

print(
    "========================================\n        설비 종합 모니터링 리포트\n========================================"
)
normal_count, notice_count, danger_count = 0, 0, 0
temp_sensors = []
max_temp = 0
max_temp_sensor = ""
danger_sensor = []
for i in range(len(sensors)):
    name, temp, freq = sensors[i]
    temp_sensors.append(temp)
    status = ""
    if temp > 90 or freq > 5.0:
        status = "위험 🚨"
        danger_count += 1
        danger_sensor.append(name)
    elif temp >= 80 or freq >= 3.0:
        status = "주의"
        notice_count += 1
    else:
        status = "정상 ✅"
        normal_count += 1
    print(f"{i+1}. {name} | 온도 {temp}℃ | 진동 {freq}mm/s | {status}")

    if temp > max_temp:
        max_temp = temp
        max_temp_sensor = name

print("----------------------------------------")
print(f"총 설비: {len(sensors)}대")
print(f"정상: {normal_count} / 주의: {notice_count} / 위험: {danger_count}")
ratio_danger = ((danger_count + notice_count) / len(sensors)) * 100
print(f"이상 설비 비율: {round(ratio_danger,1)}%")
temp_sensors.sort()
avg_temp = round(sum(temp_sensors) / len(temp_sensors), 1)
print(f"평균 온도: {avg_temp:.1f}℃")
print(f"최고 온도 설비: {max_temp_sensor} ({max_temp}℃)")

danger_sensor.sort()
print(f"위험 설비 목록: {danger_sensor}")
if len(danger_sensor) > 0:
    print("⚠ 즉시 점검 요망")
else:
    print("✅ 전 설비 안정")
