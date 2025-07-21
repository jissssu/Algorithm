from collections import deque
n, m = map(int, input().split())
targets = list(map(int, input().split()))


dq = deque(range(1, n + 1))

cnt = 0 

for target in targets:
    # 현재 target의 위치 찾기
    idx = dq.index(target)

    # 왼쪽으로 이동하는 경우가 더 적은 경우
    if idx <= len(dq) // 2:
        dq.rotate(-idx)  # 왼쪽 회전
        cnt += idx
    else:
        dq.rotate(len(dq) - idx)  # 오른쪽 회전
        cnt += len(dq) - idx

    dq.popleft() 
print(cnt)
