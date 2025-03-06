import sys
input = sys.stdin.readline

#첫번째 줄에서 로그의수 n개 입력받음
n = int(input())


# 딕셔너리를 사용해 현재 회사에 있는 사람들을 추적
office = {}

for _ in range(n):#n개의 로그를 처리
    name, check = input().strip().split()
    if check == 'enter':
        office[name] = True
    else:
        del office[name]

# 딕셔너리의 키들을 리스트로 변환
names = list(office.keys())

# 리스트를 사전 역순으로 정렬
names.sort(reverse=True)

# 정렬된 리스트 출력
for name in names:
    print(name)
