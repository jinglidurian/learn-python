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
#学生管理系统   1.把每个学生都以字典的形式存在这个列表  2.学生属性：学号，姓名，年龄
#
students = []
def add_student():
    number = input("请输入学号")
    name = input('请输入姓名')
    age = input('请输入年龄')
    info ={
        'number':number,
           'name':name,
           'age':age
    }
    students.append(info)
    print(students)

def search_student():
    number = input('请输入需要查询的学生编号')
    for student in students:
        if student['number'] == number:
            print(student)
            return
        else:
            pass
    print('学生不存在')

'''
在Python中，return关键字用于从函数中返回一个值，并终止函数的执行。当函数执行到return语句时，它会将指定的值作为结果返回给调用者。

以下是一个简单的示例，展示了return的使用：

python
复制
def add_numbers(a, b):
    result = a + b
    return result

sum = add_numbers(3, 4)
print(sum)  # 输出: 7
在上面的示例中，add_numbers函数接受两个参数 a 和 b，将它们相加并将结果赋给 result 变量。然后，使用 return 关键字将 result 的值作为函数的结果返回。

在调用 add_numbers(3, 4) 后，返回的结果 7 被赋给变量 sum,然后打印出来。

需要注意的是，return 语句可以在函数中的任何地方使用，一旦执行到 return，函数将立即停止执行并返回结果。如果函数没有显式的 return 语句，它将默认返回 None。

break代表终止循环，在循环中使用。return代表结束函数，是函数的结束符
'''
    
def update_student():
    number = input('请输入您要修改的学生编号')
    for student in students:
        if student['number'] == number:
            name = input('请输入修改后的姓名')
            age = input('请输入修改后的年龄')
            student['name'] = name
            student['age'] = age
            print(student)
            return
            
        else:
            pass
    print('学生不存在')
        
def delete_student():
    number = input('请输入想要删除的学生编号')
    for student in students:
        if student['number'] == number:
            students.remove(student)
            print('删除成功')
            return
        
        else:
            pass
    print('学生不存在')
    
'''在Python中，remove() 是列表对象的方法之一，用于删除列表中指定的元素。它会修改原始列表，将第一个匹配到的元素从列表中移除。

remove() 方法的语法如下：

python
复制
list.remove(element)
其中，list 是要操作的列表对象，element 是要删除的元素。

下面是一个使用 remove() 方法的示例：

python
复制
my_list = [1, 2, 3, 4, 5]
my_list.remove(3)  # 删除列表中的元素3
print(my_list)  # 输出：[1, 2, 4, 5]
在上述示例中，remove(3) 会将列表中第一个值为 3 的元素删除，结果列表变为 [1, 2, 4, 5]。

需要注意的是，如果列表中不存在要删除的元素，会触发 ValueError 异常。因此，在使用 remove() 方法之前，最好确保要删除的元素存在于列表中，或者使用异常处理机制来处理可能的异常情况。

另外，remove() 方法只会删除列表中的第一个匹配项。如果列表中有多个相同的元素，只有第一个匹配项会被删除。如果要删除所有匹配项，可以使用循环结构或其他方法来实现。


'''

if __name__ == '__main__':
    while True:
        num = input('请输入你要执行的内容:\n1.新增学生\n2.查询学生\n3.修改学生 \n4.删除学生\n5.退出')
        if num == '1':
            add_student()
        elif num == '2':
            search_student()
        elif num == '3':
            update_student()
        elif num == '4':
            delete_student()
        elif num == '5':
            print('下次再见')
            break
        else:
            print('输入有误 请重新输入')


           








