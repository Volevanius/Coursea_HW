number = int(input())
a1 = number // 1000
a2 = number // 100 % 10
a3 = number // 10 % 100 % 10
a4 = number % 1000 % 100 % 10
f_num = int(str(a1) + str(a2))
s_num = int(str(a4) + str(a3))
print(f_num - s_num + 1)
