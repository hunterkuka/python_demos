# 平年闰年的运算
year = int(input("请输入年份"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("{0}是闰年".format(year))
else:
    print("{0}是平年".format(year))
# 输入2018年的一个月份判断该月有多少天
month = int(input("请输入月份"))
if month in (1, 3, 5, 7, 8, 10, 12):
    days = 31
elif month in (4, 6, 9, 11):
    days = 30
else:
    days = 28
print(days)
