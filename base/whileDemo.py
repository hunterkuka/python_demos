# sum = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         sum += i
# print(sum)

for i in range(100, 1000):
    b = i // 100
    s = i % 100 // 10
    g = i % 10
    if i == b * b * b + s * s * s + g * g * g:
        print("{0}是水仙花数".format(i))
