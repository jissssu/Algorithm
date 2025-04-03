import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().strip().split()) 
sushi = [int(input().strip()) for _ in range(N)] 

# 원형 벨트를 쉽게 처리하기 위해 초밥 리스트 확장
sushi = sushi + sushi[:k-1]  


max_variety = 0

for i in range(N): 
    current_window = sushi[i:i+k]
    eaten_types = set(current_window) 
    
    # 쿠폰 초밥이 현재 윈도우에 없다면 추가
    if c not in eaten_types:
        total_types = len(eaten_types) + 1  # 쿠폰 초밥 추가
    else:
        total_types = len(eaten_types)  # 이미 먹은 종류라 추가 안됨
    
    # 최댓값 갱신
    max_variety = max(max_variety, total_types)

print(max_variety)  