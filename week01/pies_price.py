a = int(input())
b = int(input())
n = int(input())

penny_total = a * n * 100 + b * n
print(penny_total // 100, penny_total % 100)
