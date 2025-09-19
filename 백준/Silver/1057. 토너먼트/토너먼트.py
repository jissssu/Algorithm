
N, kim, lim = map(int, input().split())

round_num = 1

while kim != lim:
    kim = (kim + 1) // 2
    lim = (lim + 1) // 2
    round_num += 1

print(round_num - 1)
