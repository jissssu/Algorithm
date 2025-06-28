from itertools import combinations

N = int(input())
mp, mf, ms, mv = map(int, input().split())

foods = []
for _ in range(N):
    foods.append(tuple(map(int, input().split())))  # (p, f, s, v, c)

min_cost = float('inf')
answer = []

# 1개부터 N개까지 조합
for r in range(1, N + 1):
    for comb in combinations(range(N), r):
        tp, tf, ts, tv, tc = 0, 0, 0, 0, 0
        for idx in comb:
            p, f, s, v, c = foods[idx]
            tp += p
            tf += f
            ts += s
            tv += v
            tc += c
        if tp >= mp and tf >= mf and ts >= ms and tv >= mv:
            if tc < min_cost:
                min_cost = tc
                answer = [comb]
            elif tc == min_cost:
                answer.append(comb)

if not answer:
    print(-1)
else:

    answer.sort()
    print(min_cost)
    print(' '.join(str(i + 1) for i in answer[0]))
