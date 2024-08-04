def min_length_of_lion_subarray(N, K, dolls):
    start = 0
    lion_count = 0
    min_length = float('inf')

    for end in range(N):
        if dolls[end] == 1:
            lion_count += 1
        
        while lion_count >= K:
            min_length = min(min_length, end - start + 1)
            if dolls[start] == 1:
                lion_count -= 1
            start += 1
    
    return min_length if min_length != float('inf') else -1

# 입력 처리
N, K = map(int, input().split())
dolls = list(map(int, input().split()))

# 결과 출력
print(min_length_of_lion_subarray(N, K, dolls))
