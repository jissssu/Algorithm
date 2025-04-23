import sys
input = sys.stdin.readline

from itertools import combinations

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()  

answer = list(combinations(nums, m))  

for ans in answer:
    for num in ans:
        print(num, end=" ")
    print()
