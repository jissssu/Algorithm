n = int(input())
arr = list(map(int, input().split()))

max_sum = arr[0]  
current_sum = arr[0]  # 현재 위치까지의 최대 연속합

for i in range(1, n):
    current_sum = max(arr[i], current_sum + arr[i])
    max_sum = max(max_sum, current_sum)

print(max_sum)
