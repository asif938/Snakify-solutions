n = int(input())
sum = 0
for i in range(1,n):
    t = int(input())
    sum += t
sum2=0
for i in range(1,n+1):
    sum2 += i
print(sum2-sum)
