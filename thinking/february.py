# 用while循环实现1-100的奇数和
# num = 1
# sum = 0
# while num < 101:
#     if num % 2 == 1:
#         sum+=num
#     num+=1
# print(sum)


# 定义一个列表【‘a','b','c','b','m','b']将所有b的索引取出，追加到一个新的列表中

# li = ['a','b','c','b','j','b']
# end_li = []
# for i in range(0,len(li)):
#     if li[i] == 'b':
#         end_li.append(i)
# print(end_li)




# 让用户输入用户名和密码，正确的用户名和密码，用户名: admin 密码: 123456
# 5 当用户输入正确的用户名和密码的时候，系统提示欢迎光临，提示:请输入你想办理的业务
# 6 如果输入1，提示取款2.提示存款3，退出(实际都让系统退出)
# 7 如果用户名输入正确，密码错误。提示:"密码错误，请重新输入，剩余次数X次"
# 8 如果用户输入的错误次数超过三次，系统提示: 该账号已被冻结，退出。
# 9 如果用户输入账号错误，密码正确，提示:"该账号未注册” 退出
# num = 1

# while True:
#     username = input('请输入用户名')

#     if username != 'admin':
#         print('该账号未注册')
#         break

#     password = input('请输入密码')

#     if  password == '123456':
#         print('欢迎光临，请输入您想办理的业务\n1.取款\n2.存款\n3.退出')
#         info = input('请输入指令')

#         if info == '1':
#             break
#         elif info == '2':
#             break
#         elif info == '3':
#             break
#         else:
#             pass

#     elif password != '123456':
#         num+=1

#         if num > 3:
#             print('该账号被冻结，退出')
#             break

#         print(f'密码错误，请重新输入，剩余次数{4-num}')
   


'''
1.让用户输入用户名，如果用户名不是 admin，那么用户就要重新输入；
2.如果用户名是 admin，那么才进入到输入密码的环节；
3.如果输入的密码不是123456，那么就要重新输入；
4.如果密码是123456，那么才打印“登陆成功”


> 1）不考虑登陆密码的次数；2）不考虑后续的存款、取款、退出指令；
'''


# while True:
#     username = input('请输入用户名：')
#     if username != 'admin': continue
                          
#     while True:  
#         password = input('请输入密码：')
#         if password != '123456': continue
        
#         print('登陆成功')
#         break

#     break
        


      
   
        






       
   






