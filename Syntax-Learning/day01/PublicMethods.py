
print('=================================python公共方法=================================')
# + 【字符串，元祖，列表】
s = 'hello' + ' ' + 'python'
print(s)

list = [1,2] + [3,4]
print(list)

t = (1,2) + (3,4)
print(t)

# * 【字符串，元祖，列表】
s = 'hello' * 3
print(s)

list = [1,2] * 3
print(list)

t = (1,2) * 3
print(t)

# in 【字符串，列表，元祖，字典】
s1 = '1';s2 = '123'
print(s1 in s2)

l1 = [1,2];l2 = [3,4]
print(l1 in l2)

t1 = (1,); t2 = (2,3,4)
print(t1 in t2)

#in在对字典操作时判断的是字典的键
d1 = {"name":"gaojun"};d2 = {"name":"zhangsan"}
print("name" not in d2)

# not in 【字符串，列表，元祖，字典】
s1 = '1';s2 = '123'
print(s1 not in s2)

l1 = [1,2];l2 = [3,4]
print(l1 not in l2)

t1 = (1,); t2 = (2,3,4)
print(t1 not in t2)

#not in在对字典操作时判断的是字典的键
d1 = {"name":"gaojun"};d2 = {"name":"zhangsan"}
print("name" not in d2)

print('=================================python内置函数=================================')
#
# #cmp
#
# print("cmp(80,100):%d"%(cmp(80,100)))