import heapq
import sys

# 빠른 입력을 위해 사용
input = sys.stdin.readline

def process_operations(n, commands):
    # 최소 힙 초기화
    min_heap = []

    # 각 명령 처리
    for num in commands:
        if num > 0:
            # 자연수면 힙에 추가
            heapq.heappush(min_heap, num)
        else:
            # 0이면 최소값 출력 & 제거
            if min_heap:
                print(heapq.heappop(min_heap))
            else:
                print(0)

# 메인 실행부
if __name__ == '__main__':
    # 연산 개수 입력
    count = int(input().strip())

    # 명령 리스트 입력
    operations = [int(input().strip()) for _ in range(count)]

    # 처리 함수 호출
    process_operations(count, operations)
