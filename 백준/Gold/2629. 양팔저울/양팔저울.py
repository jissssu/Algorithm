import sys
input = sys.stdin.readline

n = int(input())  
weights = list(map(int, input().split()))
m = int(input())  
balls = list(map(int, input().split()))


MAX_WEIGHT = 40000
possible = [False] * (MAX_WEIGHT + 1)
possible[0] = True

for w in weights:
    new_possible = possible[:]  # 이번 추를 사용했을 때 변경본
    for diff in range(MAX_WEIGHT + 1):
        if possible[diff]:
            # 왼쪽에 올리기
            if diff + w <= MAX_WEIGHT:
                new_possible[diff + w] = True
            # 오른쪽에 올리기
            if abs(diff - w) <= MAX_WEIGHT:
                new_possible[abs(diff - w)] = True
    possible = new_possible


result = []
for b in balls:
    if b <= MAX_WEIGHT and possible[b]:
        result.append("Y")
    else:
        result.append("N")

print(" ".join(result))
