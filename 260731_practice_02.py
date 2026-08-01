# 02
LIMIT = 100  # 임계값 (100 초과 시 즉시 경고)

count = 0
measure = []
total = 0
while True:
    n = input("측정값을 입력하세요. 종료하려면 q 입력. : ")
    if n == "q":
        if len(measure) == 0:
            print("입력된 측정값이 없습니다.")
        else:
            print(f"총 입력 개수 : {len(measure)}")
            print(f"최댓값 : {max}, 최솟값 : {min}")
            print(f"평균값 : {(round(total/len(measure))):.2f}")
            print(f"임계값 초과 개수 : {count}")
            print("평균보다 큰 값의 개수 :", end=" ")
            avg_over = 0
            avg = total / len(measure)
            for i in measure:
                if i > avg:
                    avg_over += 1
            print(avg_over)

            sorted_measure = sorted(measure, reverse=True)
            print("상위 3개 값", sorted_measure[:3])
        break

    else:
        n = float(n)
        measure.append(float(n))
        min, max = measure[0], measure[0]

        total += n
        if min > n:
            min = n
        if max < n:
            max = n

        if n > LIMIT:
            count += 1
            print(f"🚨 임계값({LIMIT}) 초과! 현재까지 초과 {count}회")
