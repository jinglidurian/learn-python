"""
自定义函数
1.可复用性强   2.保证代码的一致性   3.代码的逻辑和结构更加简洁
定义函数
def a():
    print(10 + 10)      函数自带print所以在控制台就会有输出
a()

def 关键字 函数名（自定义的）  函数名定义需规范，函数后要：（冒号）
    缩进  代表在函数内部

调用函数
函数名（）

"""

'''
def add2(x, y):
#在定义的时候缩写的参数，叫做形式参数，简称形参
    print(x + y)
add2(1,2)
#在调用的时候所写参数，叫做实际参数，简称实参
#int类型+  代表算数运算
#string类型  +代表字符串拼接
def add():
    print(10 + 20)
def add3():
    add()

add
'''
#形参和实参都有两种方式：位置参数，关键字参数
#位置参数必须在关键字参数之前，否则报错
#如果满足定义的方式，还要注意类型的报错，有一些数据类型是无法进行加减乘除的

'''
def add(x, y, z=1):
    print(x + y)
    print(x + z)
add(1,2,3)
'''


'''
def add(a, b=True, c=1):#定义形参  参数就是一个变量名 定义变量的时候，不能以数字开头
    a += c
#a = a+c
    print(a)
    print(a + b)
#真或假  可以用1 和 0代替  true理解为1  false理解为0
add(2)
'''
#学生管理系统   1.把每个学生都以字典的形势存在这个列表  2.学生属性：学号，姓名，年龄
students = []
def add_students():
    number = input("请输入学号")
    name = input('请输入姓名')
    age = input('请输入年龄')
    info ={'number':number,
           'name':name,
           'age':age
    }
    students.append(info)
    print(students)
add_students()




