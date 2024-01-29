# 题目：输入一个正整数，判断是不是素数


# 素数（质数）是只有两个正因数的数，只能被 1 和它本身整除。素数是指大于1的自然数
# 合数是除了 1 和它本身之外还有其他正因数的数，可以被多个数整除。合数是除了 1 和它本身之外还有其他正因数的数，可以被多个数整除。

# # 方法1（最优）
# from math import sqrt
# # 先从是一个 Python 的导入语句，它导入了 math 模块中的 sqrt 函数。
# # 具体解释如下：
# # math 是 Python 标准库中的一个模块，提供了许多数学相关的函数和常量。
# # sqrt 函数是 math 模块中的一个函数，用于计算给定数的平方根。
# num = int(input('请输入一个正整数：'))
# end = int(sqrt(num))
# is_prime = True
# # 默认输入值为素数
# # is_prime是一个常见的函数名，用于判断一个数是否为素数，素数是只能被1或者自身整除的大于1的整数
# for x in range(2, end+1):
# # 素数是指大于1的自然数，所以从2开始遍历
# # range函数左开右闭，所以需要+1
#     if num % x == 0:
# # %运算符，代表取余数，如果x能被num整除（余数为0）代表num是合数
#         is_prime = False
#     break
# if is_prime and num != 1:
#     print('%d是素数'%num)
# else:
#     print('%d不是素数'%num)


# 方法2
num = int(input('请输入一个正整数：'))
is_prime = True
for x in range(2,num):
    if num % x == 0:
        is_prime = False
    break
if is_prime and num != 1:
    print('%d是素数'%num)
else:
    print('%d不是素数'%num)


