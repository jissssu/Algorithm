n, m = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
left = 0
total = 0

for right in range(n):
    # 오른쪽 포인터가 가리키는 값을 합에 추가
    total += arr[right]
    
    # 합이 m보다 크면 왼쪽 포인터를 이동시키며 합을 줄임
    while total > m and left <= right:
        total -= arr[left]
        left += 1
    
    # 합이 m과 같으면 카운트 증가
    if total == m:
        count += 1

print(count)