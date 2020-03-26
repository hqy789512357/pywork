# a = 1
# b = 2
# if a > b :
#     print("a比b大")
# else:
#     print("b比a大")  
# ******************************************  
# age = int(input("请输入年龄："))
# if age > 60:
#     print("dayu60")
# elif age <40:
#     print("xiaoyu560")
# else:
#     print("zhongnianren")  
# *******************************   in
# a = "我"
# if a in "你好，今天吃饭开了":
#         print("ok")
# else:
#     print("mot")       
# **********************************  while循环

# a = 1
# while a < 10:
#   print("******")
#   a = a + 2

# highchengji = {}
# lowchengji = {}
# xuesheng = ["一","二","三","四","五","六","七"]
# a = 0
# while a <len(xuesheng):
#   chengji = int(input("输入"+xuesheng[a]+"的成绩"))
#   if chengji >= 5:
#       highchengji[xuesheng[a]] =  chengji
#   else:
#       lowchengji[xuesheng[a]] = chengji
#   a = a + 1
# print("大于5的",highchengji)
# print("小于5的",lowchengji)          
   
# ******************************  for循环
# a = ["张三","李四","王麻子","浪晋","流云","希希","小梁","二狗","陈平安","朱珠","亚索"]
# for i in a:
#   print(i)

# b = list(range(0,20,3))     # rang(1,100,3)  步进3
# for i in b:
#   print(i)

# for i in range(1,10):           乘法表
#     for j in range(1,i+1):
#       print(i,"x",j,"=",i*j,end="  ")
#     print(j)
"""
练习1：
通过print打印，模拟一个红绿灯的功能，注意：红灯30次，绿灯35次，黄灯3次。
练习2：
使用代码，实现一个注册的功能。
用户输入账号和密码，要求账号长度是5-8位，密码6-12位，并且账号必须小写开头。
储到到字典中，{username:password}
username = input("请输入用户名：")
password = input("请输入密码：")   
"""
# while 1>0: 
#     for i in range(30,0,-1):
#         print("红灯还有",i)
#     for i in range(35,0,-1):
#         print("绿灯还有",i)
#     for i in range(3,0,-1):
#         print("黄灯还有",i) 


xiaoxie = ("abcdefghijklmnopqrstuvwxyz")
a = 1
while a>0:
    username = input("请输入用户名：")
    for i in username:
        if list(username)[0] not in xiaoxie:
            print("用户名首字母需要小写")
            break
        elif int(len(username))<5 or int(len(username))>8: 
            print("用户名长度需要在5-8位") 
            break           
        else:
           a = a - 1 
b = 1    
while b>0:
    password = input("请输入密码：") 
    for i in password:
        if int(len(password))<6 or int(len(password))>12:
            print("密码需要在6-12位")
            break
        else:
            b = b - 1

user = {username:password} 
print(user)                  
 