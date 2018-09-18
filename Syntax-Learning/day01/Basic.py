import keyword

#TODO:基本数据类型，注意文本缩进的问题

num1 = 10
num2 = 20
result = num1 + num2
print(result)
print(type(result))

#TODO:字符串--->整型(倒过来转换有点问题)
str = "10"
print(int(str))
print(type(str))

# print(str(num2))
f1 = 3.14

#TODO:查看类型
sum = num2 + f1
print(sum)
print(type(sum))


#TODO:字符串--->浮点型
str2 = "1.23"
print(float(str2))
#print(str(f1))

#TODO:python中的关键字
kw = keyword.kwlist
print(kw)


#TODO:基本运算符
a = 10.8
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)#取整
print(a % b)
print(a ** b)

#TODO:连续赋值
a1,a2,f2,str3 = 100,200,45.6,"hh"


#TODO:判断语句
"""
s = input("请输入你的成绩:")
score = int(s)
if score >= 90 and score <= 100:
    print("优秀")
elif score >= 80 and score < 90:
    print("优良")
elif score >= 70 and score < 80:
    print("良好")
elif score >= 60 and score < 70:
    print("及格")
else:print("不及格")

"""



#TODO:循环语句
#while
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(sum)

#for in
fruits = ["apple","orange","watermelon"]
for fruit in fruits:
    print(fruit)

#for x in
sum1 = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum1 += x
print(sum1)

#break continue
for x in [1,2,3,4,5,6,7,8,9,10]:
    if x % 2 == 0:
        # continue
        break
    print(x)


#
stop = 'N'
while 1:
    print("=================成绩等级查询==================")
    s = input("请输入你的成绩:")
    if s == 'Y':
        print("您已退出！！！")
        exit(0)
    if s.isdigit():
        score = int(s)
        if score >= 90 and score <= 100:
            print("优秀")
        elif score >= 80 and score < 90:
            print("优良")
        elif score >= 70 and score < 80:
            print("良好")
        elif score >= 60 and score < 70:
            print("及格")
        elif score > 100:
            print("输入非法，请重新输入")
        else:
            print("不及格")
    else:
        print('输入非法，请重新输入！')
    print("=================成绩等级查询==================\n\n")






