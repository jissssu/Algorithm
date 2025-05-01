import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().split())

max_result = -1_000_000_000
min_result = 1_000_000_000

def dfs(index, current_result, p, m, mul, div):
    global max_result, min_result

    if index == n:
        max_result = max(max_result, current_result)
        min_result = min(min_result, current_result)
        return

    if p > 0:
        dfs(index + 1, current_result + numbers[index], p - 1, m, mul, div)
    if m > 0:
        dfs(index + 1, current_result - numbers[index], p, m - 1, mul, div)
    if mul > 0:
        dfs(index + 1, current_result * numbers[index], p, m, mul - 1, div)
    if div > 0:
        if current_result < 0:
            temp = -(-current_result // numbers[index])
        else:
            temp = current_result // numbers[index]
        dfs(index + 1, temp, p, m, mul, div - 1)

dfs(1, numbers[0], plus, minus, multiply, divide)

print(max_result)
print(min_result)
