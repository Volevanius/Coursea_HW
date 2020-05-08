first = int(input())
last = int(input())
flats_number = last - first + 1

if last % flats_number == 0:
    print('YES')
else:
    print('NO')
