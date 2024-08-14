import sys
from collections import deque

n = int(sys.stdin.readline())
stack = deque()
for i in range(n):
    word = sys.stdin.readline().split()
    if word[0] == 'push_front':
        stack.appendleft(word[1])
    elif word[0] == 'push_back':
        stack.append(word[1])
    elif word[0] == 'pop_front':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.popleft())
    elif word[0] == 'pop_back':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif word[0] == 'size':
        print(len(stack))
    elif word[0] == 'front':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[0])
    elif word[0] == 'back':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif word[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)