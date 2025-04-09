import sys
input = sys.stdin.readline


m, n = map(int, input().split())
snacks = list(map(int, input().split()))


start = 1
end = max(snacks)
result = 0

while start <= end:
    mid = (start + end) // 2  
    cnt = 0  

    for snack in snacks:
        cnt += snack // mid 

    if cnt >= m:
        result = mid  
        start = mid + 1
    else:
        end = mid - 1 

print(result)
