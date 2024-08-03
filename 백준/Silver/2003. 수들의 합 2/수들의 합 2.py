N, M = map(int, input().split())
nums = list(map(int, input().split()))

left = 0
right = 0
cnt = 0
current_sum = 0

while right < N:
    current_sum += nums[right]
    right += 1
    while current_sum > M and left < right:
        current_sum -= nums[left]
        left += 1

   
    if current_sum == M:
        cnt += 1

print(cnt)
