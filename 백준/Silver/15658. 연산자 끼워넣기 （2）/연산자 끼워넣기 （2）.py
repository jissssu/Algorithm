import sys
input = sys.stdin.read

def solve():
    data = input().split()
    N = int(data[0])
    A = list(map(int, data[1:N+1]))
    plus, minus, mul, div = map(int, data[N+1:N+5])

    max_result = -int(1e9)
    min_result = int(1e9)

    def dfs(index, current, p, m, mu, d):
        nonlocal max_result, min_result

        if index == N:
            max_result = max(max_result, current)
            min_result = min(min_result, current)
            return

        if p:
            dfs(index + 1, current + A[index], p - 1, m, mu, d)
        if m:
            dfs(index + 1, current - A[index], p, m - 1, mu, d)
        if mu:
            dfs(index + 1, current * A[index], p, m, mu - 1, d)
        if d:
            if current < 0:
                dfs(index + 1, -(-current // A[index]), p, m, mu, d - 1)
            else:
                dfs(index + 1, current // A[index], p, m, mu, d - 1)

    dfs(1, A[0], plus, minus, mul, div)
    print(max_result)
    print(min_result)

solve()
