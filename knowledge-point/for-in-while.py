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


# # 输入一个正整数判断它是不是素数

# from math import sqrt

# is_prime = True  
# # 默认输入的正整数是素数（素数是指能被1或者它本身整除的大于1的正整数）
# num = int(input('请输入一个正整数: '))
# # 输入一个正整数
# start = 2
# # 起始数字是2
# end = int(sqrt(num)) + 1
# # 截止数字为输入的数据的平方根+1

# for x in range(start, end):
# # 遍历开始到结束的数字
#     if num % x == 0:
#     # 如果 num和x的余数=0
#         is_prime = False
#         break
#         # 不是素数，结束for循环
# if is_prime and num != 1:
# # 如果满足：是素数并且num不等于1
#     print('%d是素数' % num)
#     # 打印
# else:
#     print('%d不是素数' % num)




# for 循环分为两种情况
# 1.序列循环
# name = ["lijing","xiaojin"]
# for i in name:
#     print(i)
# 2.range（）函数循环
# for i in range(2,20,2):
#     print(i)

# 输入两个正整数计算他们的最大公约数和最小公约数

# x = int(input('x = '))
# y = int(input('y = '))
# # 如果x大于y就交换x和y的值
# if x > y:
#     # 通过下面的操作将y的值赋给x, 将x的值赋给y
#     x, y = y, x
# # 从两个数中较小的数开始做递减的循环
# for factor in range(x, 0, -1):
#     if x % factor == 0 and y % factor == 0:
#         print('%d和%d的最大公约数是%d' % (x, y, factor))
#         print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
#         break


# 打印如下所示的三角形图案。
# *
# **
# ***
# ****
# *****

#     *
#    **
#   ***
#  ****
# *****

#     *
#    ***
#   *****
#  *******
# *********


# row = int(input('请输入行数: '))

# for i in range(row):
#     for j in range(i + 1):
#         print('*', end='')
#     print()

# for i in range(row):
#     for j in range(row):
#         if j < row - i - 1: print(' ', end='')
#         else: print('*', end='')
#     print()

# for i in range(row):
#     for _ in range(row - i - 1):
#         print(' ', end='')
#     for _ in range(2 * i + 1):
#         print('*', end='')
#     print()


# 将12345变成54321
# num = 1,2,3,5
# reversed_num = list(reversed(num))
# print(reversed_num)
# 可以用list（）函数将迭代器对象转化为列表

# 在 Python 中，reversed() 是一个内置函数，用于反转（逆序）可迭代对象（如列表、元组或字符串）的元素顺序。
# 它返回一个反向迭代器对象，可以用于遍历或生成反向的元素序列。

my_tuple = (1, 2, 3, 4, 5)
for num in reversed(my_tuple):
    print(num)
# 或者是使用for循环遍历