S = int(input())

n = 1
sum_ = 0

while True:
    sum_ += n
    if sum_ > S:
        print(n - 1)
        break
    n += 1
