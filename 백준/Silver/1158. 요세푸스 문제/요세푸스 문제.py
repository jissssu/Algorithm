n, k = map(int, input().split())
ans = []
num = 0
list = [0] * n
for i in range(n):
    list[i] = i + 1

for i in range(n):
    num += (k - 1)
    if num >= len(list):
        num %= len(list)
    ans.append(list[num])
    list.pop(num)

print(str(ans).replace('[', '<').replace(']', '>'))