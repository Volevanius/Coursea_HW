x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
sum1 = x1 + y1
sum2 = x2 + y2

if (sum1 % 2 == 0 and sum2 % 2 == 0) or (sum1 % 2 == 1 and sum2 % 2 == 1):
    if y2 - x2 >= y1 - x1 and y2 >= y1:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
