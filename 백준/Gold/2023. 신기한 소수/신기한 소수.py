N = int(input())

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def dfs(number, length):
    if length == N:
        print(number)
        return

    for digit in range(1, 10):
        next_num = number * 10 + digit
        if is_prime(next_num):
            dfs(next_num, length + 1)

for prime in [2, 3, 5, 7]:
    dfs(prime, 1)
