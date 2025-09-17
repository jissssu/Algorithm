import sys

data = sys.stdin.buffer.read().split()
it = iter(data)

n = int(next(it))
arr = set(int(next(it)) for _ in range(n))
m = int(next(it))

out = []
for _ in range(m):
    x = int(next(it))
    out.append('1' if x in arr else '0')

sys.stdout.write('\n'.join(out))
