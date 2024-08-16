import sys
n = int(sys.stdin.readline())
stack=[]
answer = []
now = 1
FT = True
for i in range(n):
    num = int(sys.stdin.readline())
    # 스택 쌓기
    while now <= num:
        stack.append(now)
        answer.append("+")
        now += 1
    # 스택 꺼내기
    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    # 불가능한 경우
    else:
        FT = False

# 스택 수열 만들수 있는지 여부에 따라 출력
if FT:
    for ans in answer:
        print(ans)
else:
    print('NO')

