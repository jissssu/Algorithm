n = int(input())
arr = [0] * n
arr[0] = 1

if n == 2:
    arr[1] = 2
elif n >= 3:
    arr[1] = 2    
    for i in range(2, n):
        arr[i] = arr[i-1] + arr[i-2]

print(arr[-1]%10007)