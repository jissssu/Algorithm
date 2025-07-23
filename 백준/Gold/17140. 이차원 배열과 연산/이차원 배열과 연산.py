from collections import Counter

def operation_R(A):
    max_len = 0
    new_A = []
    for row in A:
        counter = Counter(x for x in row if x != 0)
        temp = sorted(counter.items(), key=lambda x: (x[1], x[0]))
        new_row = []
        for num, cnt in temp:
            new_row.extend([num, cnt])
        max_len = max(max_len, len(new_row))
        new_A.append(new_row)

    # 100개 초과 자르기
    max_len = min(max_len, 100)
    for i in range(len(new_A)):
        if len(new_A[i]) < max_len:
            new_A[i].extend([0] * (max_len - len(new_A[i])))
        else:
            new_A[i] = new_A[i][:max_len]

    return new_A

def operation_C(A):
    # 행렬 크기
    row_len = len(A)
    col_len = len(A[0])

    # 열 기준으로 작업 -> 전치 후 R 연산처럼 처리
    transposed = []
    for c in range(col_len):
        col = [A[r][c] for r in range(row_len)]
        transposed.append(col)

    transposed = operation_R(transposed)

    
    row_len_new = len(transposed[0])
    col_len_new = len(transposed)

    new_A = [[0]*row_len_new for _ in range(col_len_new)]

    for r in range(col_len_new):
        for c in range(row_len_new):
            new_A[r][c] = transposed[r][c]

    # 다시 전치해서 행렬 형태 맞추기
    result = [[0]*col_len_new for _ in range(row_len_new)]
    for r in range(row_len_new):
        for c in range(col_len_new):
            result[r][c] = new_A[c][r]

    return result

r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

time = 0
while time <= 100:
    if 0 <= r-1 < len(A) and 0 <= c-1 < len(A[0]) and A[r-1][c-1] == k:
        print(time)
        break

    time += 1
    if len(A) >= len(A[0]):
        A = operation_R(A)
    else:
        A = operation_C(A)
else:
    print(-1)
