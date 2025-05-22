import sys

# 현재 계란이 모두 몇개 깨졌는지 확인하는 함수
def check_eggs():
    cnt = 0
    for egg in eggs:
        if egg[0] <= 0:
            cnt += 1
    return cnt

def backtrack(start):
    global n, answer
    # 들고 있는 계란이 가장 오른쪽 계란
    if start == n:
        answer = max(answer, check_eggs())
        return
    # 손에 든 계란이 깨졌으면 계란 치기 못하니까 -> 바로 다음 계란으로 넘어가기
    if eggs[start][0] <= 0:
        backtrack(start + 1)
    # 아직 안깨졌으면 다른 계란 깨볼 수 있음
    else:
        is_all_broken = True
        # 가능한 모든 다른 계란에 대해 깨기 시도
        for i in range(n):
            # 다음 계란이 안깨진 계란이면
            if i is not start and eggs[i][0] > 0:
                is_all_broken = False
                # 계란 치기
                eggs[start][0] -= eggs[i][1]
                eggs[i][0] -= eggs[start][1]
                backtrack(start+1)
                # 다시 복구
                eggs[start][0] += eggs[i][1]
                eggs[i][0] += eggs[start][1]
        # 다음 계란이 다 깨졌음 -> 칠 수 있는 계란이 없음
        if is_all_broken:
            answer = max(answer, check_eggs())
            return


input = sys.stdin.readline
n = int(input())
eggs = []
for _ in range(n):
    eggs.append(list(map(int, input().split())))
answer = 0
backtrack(0)

print(answer)