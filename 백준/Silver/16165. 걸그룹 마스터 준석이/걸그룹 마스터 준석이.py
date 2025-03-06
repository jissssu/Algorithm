import sys

# 그룹 수와 문제 수 입력 받기
N, M = map(int, sys.stdin.readline().split())
group_info = []

# 각 그룹 정보 입력 받기
for _ in range(N):
    group_name = sys.stdin.readline().rstrip()  # 그룹 이름
    members = set()  # 멤버를 저장할 집합
    num_members = int(sys.stdin.readline())  # 멤버 수
    for _ in range(num_members):
        members.add(sys.stdin.readline().rstrip())  # 각 멤버 추가
    group_info.append((members, group_name))  # 그룹 정보 저장

for _ in range(M):
    query_name = sys.stdin.readline().rstrip()  # 질의 이름
    query_type = int(sys.stdin.readline())  # 0 또는 1

    if query_type:  # 멤버 이름이 주어졌을 경우
        for group in group_info:
            members = group[0]
            if query_name in members:
                print(group[1])  # 해당 그룹 이름 출력
                break
    else:  # 그룹 이름이 주어졌을 경우
        for group in group_info:
            group_name = group[1]
            if query_name == group_name:
                sorted_members = sorted(list(group[0]))  # 그룹 멤버들 이름 정렬
                for member in sorted_members:
                    print(member)  # 멤버 이름 출력
                break
