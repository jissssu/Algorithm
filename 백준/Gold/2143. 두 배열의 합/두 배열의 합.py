from collections import Counter

# 부배열의 모든 합을 구하는 함수
def get_all_subarray_sums(arr):
    sub_sums = []
    for i in range(len(arr)):
        total = 0
        for j in range(i, len(arr)):
            total += arr[j]
            sub_sums.append(total)
    return sub_sums

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

sumA = get_all_subarray_sums(A)
sumB = get_all_subarray_sums(B)

counterB = Counter(sumB)

# 정답 세기
answer = 0
for a in sumA:
    answer += counterB[T - a]

print(answer)
