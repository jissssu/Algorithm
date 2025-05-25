n, s = map(int, input().split())
nums = list(map(int, input().split()))

count = 0

def dfs(index, total):
    global count
    if index == n:
        if total == s and index != 0:
            count += 1
        return
    dfs(index + 1, total + nums[index])
    dfs(index + 1, total)

dfs(0, 0)

# 합이 S인 경우 중 공집합은 제외해야 함
# 여기선 애초에 dfs에서 크기가 0인 경우는 걸러짐
if s == 0:
    count -= 1 

print(count)
