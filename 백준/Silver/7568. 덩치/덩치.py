n = int(input())
person = []

for i in range(n):
    x, y = map(int, input().split())
    person.append([x, y])

for i in person:
    rank = 1
    for j in person:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")
