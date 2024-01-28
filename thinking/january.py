# name_str = ['a','b','c','b','f','b']  把b的索引取出来之后求和

# name_str = ['a','b','c','b','f','b']  

# sum = 0
# for i in range(len(name_str)):
#     if name_str [i] == 'b':
#         sum += i
#     else :
#         pass
# print(sum)
# 1.确定取值范围  012345 range（0，6）
# 2.通过什么表达式求出   
# 3.这个值放到range（）形成了什么范围   
# 4.i 的取值是什么
# 5.判断我们想要的值
# 6.把这些只在外面定义一个最终变量进行追加

# 知识点：
# range(101)：可以用来产生0到100范围的整数，需要注意的是取不到101。
# range(1, 101)：可以用来产生1到100范围的整数，相当于前面是闭区间后面是开区间。
# range(1, 101, 2)：可以用来产生1到100的奇数，其中2是步长，即每次数值递增的值。
# range(100, 0, -2)：可以用来产生100到1的偶数，其中-2是步长，即每次数字递减的值。
# len()是一个内置函数，用于返回一个对象的长度或元素个数。它可以用于字符串、列表、元组、字典、集合等各种可迭代对象以及一些其他数据结构。

# i = 【5，2，3，12，66，8，9，18】 取出偶数并求和
# i = [5,2,3,12,66,8,9,18]
# sum = 0
# for x in(i):
#     if x % 2 == 0:
#         sum += x
#     else:
#         pass
# print(sum)



# 在控制台输入几个英文单词，单词之间以空格隔开，输入单词之后应该输出你刚才输入的单词数量
# words = input('请输入你的单词')

# print(len(words.split(' ')))


# 手写字典，定义4个key，分别是：手机型号，手机内存，手机品牌，手机的app。其中手机品牌需要定义列表储存，app需要定义键值对，
# “app名称”：“类型”  类型如：游戏，社交，理财。。。

# telephon = {'手机型号':' 14pm',
#            '手机内存':'128G',
#            '手机品牌':['苹果','华为','小米','锤子'],
#            ' app名称':{
#                '微信':'社交',
#                '支付宝':'理财',
#                '消消乐':'游戏'

#            }};


# 通过input输入两句话，并且合并至一句话存入列表中
# one = input('大家好')
# two = input('我叫jingle')

# print((one + two).split())


# 输入一个正整数判断是不是素数

# 方法1

# from math import sqrt
# num = int (input('请输入一个正整数：'))
# end = int(sqrt(num)) 
# is_prime = True
# '''is_prime是一个常见的函数名，用于判断一个数是否为素数，素数是只能被1或者自身整除的大于1的整数'''
# for x in range(2, end + 1):
#     if num % x == 0:
#         is_prime = False
#         break
# if is_prime and num != 1:
#     print('%d是素数' % num)
# else:
#     print('%d不是素数'% num)

# 方法2（GPT提供）
# def is_prime(n):
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range(3, int(n**0.5) + 1, 2):
#         if n % i == 0:
#             return False
#     return True

# # 用户输入一个正整数
# num = int(input("请输入一个正整数："))

# # 判断是否为素数
# if is_prime(num):
#     print(num, "是素数")
# else:
#     print(num, "不是素数")



# # 求1--100的奇数和
# sum = 0
# for i in range(1,101,2):
#     sum += i

# print(sum)










        


