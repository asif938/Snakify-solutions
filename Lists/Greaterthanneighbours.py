lst = [int(x) for x in input().split()]
cnt = 0
for i in range(1,len(lst)-1):
    if lst[i] > lst[i-1] and lst[i] > lst[i+1]:
        cnt += 1
print(cnt)
