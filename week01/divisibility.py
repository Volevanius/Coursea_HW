a = int(input())
b = int(input())

div_true = 0**(a % b)
div_false = 1 - 0**(a % b)

print('YES' * div_true, 'NO' * div_false, sep='')
