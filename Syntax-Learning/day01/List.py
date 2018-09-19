
#TODO:列表

list = ["Chinese","Math","English","Physics","Chemistry ","Biology"]

#列表的遍历1～～for
for x in list:
    print(x)

#列表遍历2～～while
i = 0
while i < len(list):
    print(list[i])
    i += 1

#==============================列表的常见操作==============================

#列表长度
length  = len(list)

#列表取值
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[-1])
print(list[-2])
print(list[-3])
#print(list[-9])#越界

#列表的增删改查
print("==============列表的增==============")
a = [1,2,3]
b = [4,5]
#b被作为一个整体添加
a.append(b)
print(a)
#b中的元素被逐一添加到a中
a.extend(b)
print(a)
#在指定位置添加
a.insert(1,6)
print(a)

print("==============列表的删==============")
num = [1,2,3,4,5,6]
#删除指定索引的数据
del num[2]
print(num)
#删除最后一个元素
num.pop()
print(num)
#删除指定的元素
num.remove(4)
#num.remove(4)#如果删除的元素不存在，会异常ValueError: list.remove(x): x not in list
print(num)

print("==============列表的改==============")
nameList = ["zhangsan","lisi","wanger","mazi"];
nameList[2] = "gaojun"
print(nameList)

print("==============列表的查==============")
num2 = [1,2,3,4,5,3,4]
if 3 in num2:
    print("3 exists")
else:
    print("3 not exists")

#如果元素不存在，会抛异常ValueError: 'h' is not in list
print(num2.index(3))
print(num2.count(4))

#列表排序
print("==============列表排序==============")
num3 = [1,3,2,4,5,7,9,8]
num3.sort()
print(num3)
num3.reverse()
print(num3)

#列表嵌套
print("==============列表嵌套==============")
schoolNames = [["清华大学","北京大学"],["上海交通大学","上海大学","复旦大学","南开大学"],
               ["浙江大学","杭州师范大学","杭州电子科技大学"]]
print(schoolNames)

#demo:将8个学生随机分配到3个班级中
import random
classes = [[],[],[]]
students = ['A','B','C','D','E','F','G','H']
for student in students:
    #产生0～2的随机数
    index = random.randint(0,2)
    classes[index].append(student)
print(classes)

i = 1
for tempClass in classes:
    #注意打印多个值的格式
    print("班级%d的人数:%d"%(i,len(tempClass)))
    i += 1
    for x in tempClass:
        print("姓名:%s\t"%x,end = '')
    print("\n")
    print("*"*20)


#元祖tuple

#定义一个元祖
print("==============元祖==============")
teammates = ('Michale','Maria','Kangkang')
print(teammates)

print(teammates[0],teammates[-1])

#元祖一旦定义就不可改变,如果只有一个元素，要加上,
names = ('hehe',)
print(names)

#TODO:这样写也不可改变！！！
#"可变"的元祖
names1 = ('gaojun','liuhe',[1,2,3,4])
# names1[2,1] = 20
# names1[-1,-1] = 40
print(names1)