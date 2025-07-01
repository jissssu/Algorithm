import sys
input = sys.stdin.readline

N = int(input())
cards = set(map(int, input().split()))

M = int(input())
targets = list(map(int, input().split()))

result = ['1' if num in cards else '0' for num in targets]
print(' '.join(result))
