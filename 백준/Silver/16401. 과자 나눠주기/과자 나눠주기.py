def can_divide_snacks(snacks, M, length):
    count = 0
    for snack in snacks:
        count += snack // length
    return count >= M

def max_snack_length(M, N, snacks):
    left, right = 1, max(snacks)
    best_length = 0

    while left <= right:
        mid = (left + right) // 2
        if can_divide_snacks(snacks, M, mid):
            best_length = mid
            left = mid + 1
        else:
            right = mid - 1

    return best_length

# 입력 처리
M, N = map(int, input().split())
snacks = list(map(int, input().split()))

# 결과 출력
print(max_snack_length(M, N, snacks))
