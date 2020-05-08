a_h = int(input())
a_m = int(input())
a_s = int(input())
b_h = int(input())
b_m = int(input())
b_s = int(input())

a_total = a_h*60*60 + a_m*60 + a_s
b_total = b_h*60*60 + b_m*60 + b_s

diff = b_total - a_total
print(diff)
