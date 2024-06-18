n = int(input())
max = n
index = 1
maxindex = 1
while n != 0:
    if n>max:
        max = n
        maxindex = index      
    n = int(input())
    index += 1
print(maxindex)