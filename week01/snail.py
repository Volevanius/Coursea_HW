h = int(input())
up_per_day = int(input())
down_per_day = int(input())

total_per_day = up_per_day - down_per_day

time_to_get_to_min_h = (h - up_per_day + total_per_day - 1) // total_per_day

print(time_to_get_to_min_h + 1)
