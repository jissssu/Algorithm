from collections import deque
import sys
input = sys.stdin.readline

# 큐를 생성
queue = deque()

# 명령의 수를 입력
n = int(input().strip())

# 각 명령을 처리
for _ in range(n):
    command = input().strip().split()
    
    if command[0] == 'push':
        queue.append(int(command[1]))
    elif command[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        print(1 if not queue else 0)
    elif command[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
