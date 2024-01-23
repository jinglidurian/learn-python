# # 用for循环实现1~100求和
# sum = 0
# for i in range(101):
#     sum += i
# print(sum)



# 用for循环实现1~100之间的偶数求和

# sum = 0
# for x in range(2, 101, 2):
#     sum += x
# print(sum)


# 输出乘法口诀表(九九表)

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%d*%d=%d' % (i, j, i * j), end='\t')
#     print()


# 输入一个正整数判断它是不是素数

# from math import sqrt

# num = int(input('请输入一个正整数: '))
# end = int(sqrt(num))
# is_prime = True
# for x in range(2, end + 1):
#     if num % x == 0:
#         is_prime = False
#         break
# if is_prime and num != 1:
#     print('%d是素数' % num)
# else:
#     print('%d不是素数' % num)

