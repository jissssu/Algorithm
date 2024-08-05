# 단어 뒤집기
import sys

n = int(sys.stdin.readline())
for i in range(n):
    text = sys.stdin.readline().split()
    for j in text:
        answer = list(j)
        answer.reverse()
        for k in range(len(answer)):
            print(answer[k], end="")
        print('', end=" ")
    print('')