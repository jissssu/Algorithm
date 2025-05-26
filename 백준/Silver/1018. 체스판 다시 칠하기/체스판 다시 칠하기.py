n, m = map(int, input().split())
board = [input() for _ in range(n)]

def count_repaints(x, y, start_color):
    count = 0
    for i in range(8):
        for j in range(8):
            # 현재 칸이 올바른 색인지 확인
            if (i + j) % 2 == 0:
                expected = start_color  # 짝수 합: 시작 색
            else:
                expected = 'B' if start_color == 'W' else 'W'  # 홀수 합: 반대 색

            if board[x + i][y + j] != expected:
                count += 1
    return count

min_paint = float('inf')

# 보드의 모든 8x8 영역을 검사
for i in range(n - 7):
    for j in range(m - 7):
        count_w = count_repaints(i, j, 'W') 
        count_b = count_repaints(i, j, 'B')  
        min_paint = min(min_paint, count_w, count_b)

print(min_paint)
