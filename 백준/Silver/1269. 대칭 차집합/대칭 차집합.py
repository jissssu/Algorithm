
a_len, b_len = map(int, input().split())
a_set = set(map(int, input().split()))
b_set = set(map(int, input().split()))

# 대칭 차집합 구하기
symmetric_diff = a_set ^ b_set 

print(len(symmetric_diff))
