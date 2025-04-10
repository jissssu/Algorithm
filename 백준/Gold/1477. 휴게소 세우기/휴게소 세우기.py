import sys
input = sys.stdin.readline


N, M, L = map(int, input().split())  
if N:
    rest = list(map(int, input().split()))
else:
    rest = []


rest.append(0)
rest.append(L)
rest.sort()


gaps = []
for i in range(1, len(rest)):
    gaps.append(rest[i] - rest[i - 1])


start = 1
end = L
answer = 0

while start <= end:
    mid = (start + end) // 2  # 최대 간격 길이 후보
    cnt = 0

    for gap in gaps:
        # gap이 정확히 나누어떨어지면 (gap // mid) - 1
        if gap <= mid:
            continue
        else:
            cnt += (gap - 1) // mid  # (gap // mid) - 1 과 동일

    if cnt > M:  
        start = mid + 1
    else:  
        answer = mid
        end = mid - 1

print(answer)
