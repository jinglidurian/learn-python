# '''英制单位英寸和公制单位厘米互换'''

# Value = float(input('请输入长度:'))
# unit = input('请输入单位:')
# if unit == 'in' or unit == '英寸':
#     print('%f英寸 = %f厘米' % (Value, Value * 2.54))
# elif unit == 'cm' or unit == "厘米":
#     print("%f厘米 = %f英寸" % (Value, value / 2.54))
# else:
#     print('请输入有效单位')



# '''百分制成绩转换为等级制成绩'''

# while (bool(1)):
#     try:
#         score = float(input('请输入成绩: '))
#     except ValueError:
#         print('请输入正确的成绩!')
#     else:
#         break

# if score >= 90:
#     grade = 'A'
# elif score >= 80:
#     grade = 'B' 
# elif score >= 70:
#     grade = 'C'
# elif score >= 60:
#     grade = 'D'
# elif score < 60:
#     grade = 'E'

# print('你的等级是: ', grade)




# 判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积

# a = float(input('a = '))
# b = float(input('b = '))
# c = float(input('c = '))

# if a + b > c and a + c > b and c + b > a:
#     print('周长:%f' %(a + b + c))
#     p = (a + b + c) / 2
#     area = (p * (p - a) * (p - c)) ** 0.5
#     print('面积:%f' % (area))
# else:
    # print('不能构成三角形')