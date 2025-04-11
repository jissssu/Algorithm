import sys
input = sys.stdin.readline


S, P = map(int, input().split())
dna = input().strip()
required = list(map(int, input().split()))


count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
result = 0


for i in range(P):
    count[dna[i]] += 1

# 조건을 만족하는지 확인하는 함수
def is_valid():
    return (count['A'] >= required[0] and
            count['C'] >= required[1] and
            count['G'] >= required[2] and
            count['T'] >= required[3])


if is_valid():
    result += 1


for i in range(P, S):
    outgoing = dna[i - P]  # 빠져나가는 문자
    incoming = dna[i]      # 새로 들어오는 문자

    count[outgoing] -= 1
    count[incoming] += 1

    if is_valid():
        result += 1


print(result)
