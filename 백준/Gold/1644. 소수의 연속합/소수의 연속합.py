n = int(input())
def count_continuous_prime_sum(n):
    # 에라토스테네스의 체를 이용하여 n 이하의 소수 구하기
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    
    # 소수 목록 만들기
    primes = [i for i in range(n+1) if is_prime[i]]
    
    # 연속된 소수의 합이 n이 되는 경우의 수 세기
    count = 0
    for start in range(len(primes)):
        sum_of_primes = 0
        for end in range(start, len(primes)):
            sum_of_primes += primes[end]
            if sum_of_primes == n:
                count += 1
                break
            if sum_of_primes > n:
                break
    
    return count


print(count_continuous_prime_sum(n))