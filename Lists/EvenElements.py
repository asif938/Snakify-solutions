lst = [int(x) for x in input().split()]
for i in range(len(lst)):
    if lst[i] % 2 == 0:
        print(lst[i], end=' ')