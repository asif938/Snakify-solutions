import math
n = int(input())
sum = 0
for i in range(1,n+1):
    sum += math.factorial(i)
print(sum)