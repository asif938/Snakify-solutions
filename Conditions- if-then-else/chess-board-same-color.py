x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if (x1 + y1 + x2 + y2) % 2 == 0:
    print('YES')
else:
    print('NO')


'''
# another solution

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (a % 2 != 0 and b % 2 != 0) or (a % 2 == 0 and b % 2 == 0):
    if (c % 2 != 0 and d % 2 != 0) or (c % 2 == 0 and d % 2 == 0):
        print('YES')
    else:
        print('NO')
elif (a % 2 == 0 and b % 2 != 0) or (a % 2 != 0 and b % 2 == 0):
    if (c % 2 == 0 and d % 2 != 0) or (c % 2 != 0 and d % 2 == 0):
        print('YES')
    else:
        print('NO')
else:
    print('NO')

'''
