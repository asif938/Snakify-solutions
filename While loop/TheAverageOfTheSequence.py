sum = 0
n = int(input())
cnt = 0
while n != 0:
    sum += n
    n = int(input())
    cnt += 1
avg = sum/cnt
print(avg)
