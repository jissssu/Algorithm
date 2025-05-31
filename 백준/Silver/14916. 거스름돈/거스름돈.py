n = int(input())

count_5 = n // 5  

while count_5 >= 0:
    rest = n - (count_5 * 5)
    if rest % 2 == 0: 
        count_2 = rest // 2
        print(count_5 + count_2)
        break
    count_5 -= 1 
else:
    print(-1)
