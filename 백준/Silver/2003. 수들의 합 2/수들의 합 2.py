n, m = map(int, input().split())
numbers = list(map(int, input().split()))

count = 0
for start in range(n):
    total = 0
    for end in range(start, n):
        total += numbers[end]
        if total == m:
            count += 1
        elif total > m:
            break

print(count)