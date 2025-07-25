import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
queue = deque()
output = []

for _ in range(n):
    cmd = input().strip()
    
    if cmd.startswith('push'):
        _, value = cmd.split()
        queue.append(int(value))
    elif cmd == 'pop':
        output.append(queue.popleft() if queue else -1)
    elif cmd == 'size':
        output.append(len(queue))
    elif cmd == 'empty':
        output.append(0 if queue else 1)
    elif cmd == 'front':
        output.append(queue[0] if queue else -1)
    elif cmd == 'back':
        output.append(queue[-1] if queue else -1)

print('\n'.join(map(str, output)))
