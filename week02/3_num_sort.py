a, b, c = int(input()), int(input()), int(input())

if c > b:
    (c, b) = (b, c)
if b > a:
    (b, a) = (a, b)
if c > b:
    (c, b) = (b, c)

print(c, b, a)
