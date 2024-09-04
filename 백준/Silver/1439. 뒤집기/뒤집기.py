import sys
input_string = sys.stdin.readline().strip()

change_count = 0

# 문자열의 첫 번째 문자부터 시작하여 두 번째 문자부터 비교
for index in range(1, len(input_string)):
    # 이전 문자와 현재 문자가 다르면 변화가 발생한 것
    if input_string[index - 1] != input_string[index]:
        change_count += 1

# 뒤집는 횟수는 변화된 구간의 수를 반으로 나눈 값과 같음
minimum_flips = (change_count + 1) // 2

print(minimum_flips)
