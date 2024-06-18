n = int(input())

i = n//2
while pow(2,i) > n:
    i -= 1
print(i,pow(2,i))