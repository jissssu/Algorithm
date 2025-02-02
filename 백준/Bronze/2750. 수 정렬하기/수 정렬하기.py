def bubblesort(a, N):
    for i in range(N-1, 0, -1):
        for j in range(0,i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

N = int(input())
n_list = []
for i in range(N):
  n_list.append(int(input()))
k = bubblesort(n_list,N)
for j in k:
  print(j)