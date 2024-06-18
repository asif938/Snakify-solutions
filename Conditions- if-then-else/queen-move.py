c1 = int(input())
r1 = int(input())
c2 = int(input())
r2 = int(input())

if abs(c2-c1) == abs(r2-r1) or c1==c2 or r1==r2:
    print('YES')
else:
    print('NO')