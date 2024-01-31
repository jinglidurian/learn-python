# 用while循环实现1-100的奇数和
# sum = 0
# unm = 1
# while unm < 101:
#     if unm %2 == 1:
#         sum += unm
#     unm += 1
#     print(sum)

# 定义一个列表【‘a','b','c','b','m','b']将所有b的索引取出，追加到一个新的列表中

# x = ['a','b','c','b','j','b']
# y = []
# for li in x:
#   if li == ['b']:
#     y = len(li)
#     print(y)


# 让用户输入用户名和密码，正确的用户名和密码，用户名: admin 密码: 123456
# 5 当用户输入正确的用户名和密码的时候，系统提示欢迎光临，提示:请输入你想办理的业务
# 6 如果输入1，提示取款2.提示存款3，退出(实际都让系统退出)
# 7 如果用户名输入正确，密码错误。提示:"密码错误，请重新输入，剩余次数X次"8 如果用户输入的错误次数超过三次，系统提示: 该账号已被冻结，退出。
# 9 如果用户输入账号错误，密码正确，提示:"该账号未注册” 退出

your = input('请输入用户名')
password = input('请输入密码')
while your == 'admin'and password == '123456':
    im = input('欢迎光临，请输入你想办理的业务')
    break
if your == 'admin'and password != '123456':
    print('密码错误，请重新输入')
if your != 'admin':
    print('该账号未注册')
if im == 1:
    print('请输入取款金额')
elif im == 2:
    print('请输入存款金额')
else:
    im == 3
    print('退出系统')







