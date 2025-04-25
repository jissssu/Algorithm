import sys
from itertools import product

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort() 


all_sequences = product(nums, repeat=m)

# 중복 제거 후 사전순 정렬
answer = sorted(set(all_sequences))


for ans in answer:
    for num in ans:
        print(num, end=" ")
    print()
