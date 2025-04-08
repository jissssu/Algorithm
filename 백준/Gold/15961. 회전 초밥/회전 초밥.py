N, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(N)]

# 슬라이딩 윈도우를 위한 딕셔너리 (각 초밥 종류별 개수 저장)
sushi_count = {}
max_types = 0

# 초기 윈도우 설정 (처음 k개)
for i in range(k):
    sushi = belt[i]
    if sushi in sushi_count:
        sushi_count[sushi] += 1
    else:
        sushi_count[sushi] = 1


if c in sushi_count:
    max_types = len(sushi_count)
else:
    max_types = len(sushi_count) + 1

for i in range(N):
    # 맨 앞 초밥 제거
    remove_sushi = belt[i]
    sushi_count[remove_sushi] -= 1
    if sushi_count[remove_sushi] == 0:
        del sushi_count[remove_sushi]
    
    # 새로운 초밥 추가 (원형 벨트 고려)
    add_idx = (i + k) % N
    add_sushi = belt[add_idx]
    if add_sushi in sushi_count:
        sushi_count[add_sushi] += 1
    else:
        sushi_count[add_sushi] = 1
    
    # 쿠폰 초밥 고려해서 최대값 갱신
    if c in sushi_count:
        types = len(sushi_count)
    else:
        types = len(sushi_count) + 1
    
    max_types = max(max_types, types)

print(max_types)