def sugar_delivery(N):
    count = 0
    
    # 5의 배수가 될 때까지 3씩 빼면서 시도
    while N >= 0:
        if N % 5 == 0:  # 5의 배수이면
            count += N // 5  # 5로 나눈 몫을 더함
            print(count)
            return
        N -= 3  # 3킬로그램 봉지 하나 추가
        count += 1
    
    # 정확히 나눌 수 없다면 -1 출력
    print(-1)

# 입력 받기
N = int(input())
sugar_delivery(N)
