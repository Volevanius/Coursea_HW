total_minutes = int(input())
hours = (total_minutes // 60) % 24
minutes = total_minutes % 60
print(hours, minutes)
