sec_left = int(input())
hours = (sec_left // 60 // 60) % 24
minutes = (sec_left % (60 * 60)) // 60
min_first_num = minutes // 10
min_second_num = minutes % 10
sec = sec_left % 60
sec_first_num = sec // 10
sec_second_num = sec % 10
print(hours, ':',
      min_first_num, min_second_num, ':',
      sec_first_num, sec_second_num,
      sep='')
