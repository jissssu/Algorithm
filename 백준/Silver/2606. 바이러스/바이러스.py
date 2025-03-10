# 컴퓨터의 수 입력받기
n = int(input())
# 연결된 컴퓨터 쌍의 수 입력받기
m = int(input())

# 각 컴퓨터와 연결된 컴퓨터들을 저장할 리스트
# 0번 인덱스는 사용하지 않고, 1번부터 n번까지 사용
connections = [[] for _ in range(n+1)]

# 연결 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    # a와 b가 연결되어 있다는 정보 저장 (양방향)
    connections[a].append(b)
    connections[b].append(a)

# 각 컴퓨터의 감염 여부를 저장할 리스트
infected = [False] * (n+1)

# DFS 함수 정의
def dfs(computer):
    # 현재 컴퓨터를 감염 처리
    infected[computer] = True
    
    # 현재 컴퓨터와 연결된 모든 컴퓨터에 대해
    for connected_computer in connections[computer]:
        # 아직 감염되지 않았다면 감염시키기
        if not infected[connected_computer]:
            dfs(connected_computer)

# 1번 컴퓨터부터 바이러스 퍼뜨리기 시작
dfs(1)

# 1번 컴퓨터를 제외하고 감염된 컴퓨터의 수 세기
# infected[1]은 항상 True이므로 1번 컴퓨터는 카운트에서 제외
count = 0
for i in range(2, n+1):  # 2번 컴퓨터부터 n번 컴퓨터까지
    if infected[i]:
        count += 1

print(count)