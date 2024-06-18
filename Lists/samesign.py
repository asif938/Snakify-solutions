lst = [int(x) for x in input().split()]
for i in range(1,len(lst)):
    if lst[i] > 0 and lst[i-1] > 0 or lst[i] < 0 and lst[i-1] < 0:
        print(lst[i-1], lst[i], end=' ')
        break
    