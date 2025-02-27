n = int(input())  
skyline = []

for _ in range(n):
    x, y = map(int, input().split())
    skyline.append(y)

stack = []
count = 0  

for height in skyline:
    while stack and stack[-1] > height:
        stack.pop()

    if stack and stack[-1] == height:
        continue  

    if height > 0:
        stack.append(height)
        count += 1  

print(count)
