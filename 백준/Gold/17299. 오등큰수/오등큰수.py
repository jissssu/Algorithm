from collections import Counter

n = int(input())
data = list(map(int, input().split()))
count = Counter(data)
stack = []
result = [-1] * n
stack.append(0)

for i in range(n):
    while stack and count[data[stack[-1]]] < count[data[i]]:
        result[stack.pop()] = data[i]
    stack.append(i)

for r in result:
    print(r, end=' ')