n = int(input())
nums = list(map(int, input().split()))
max_num = nums[0]
min_num = nums[0]
for i in range(0, n):
    if int(nums[i]) > max_num:
        max_num = nums[i]
    if int(nums[i]) < min_num:
        min_num = nums[i]
print(min_num, max_num)