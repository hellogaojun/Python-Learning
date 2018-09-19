
#TODO:字典

#定义
dict = {'name':'gaojun','age':88,'height':176}
print(dict)

dict["id"] = 999
print(dict)

#KeyError: 'hh'
#print(dict['hh'])

#遍历操作
print("===================字典遍历操作===================")

for key in dict.keys():
    print(key)

for value in dict.values():
    print(value)

for item in dict.items():
    print(item)

for key,value in dict.items():
    print("key=%s,value=%s" %(key,value))

chars = ['a','b','c','d','e']
#同时遍历出数据和下标
for i,char in enumerate(chars):
    print(i,char)


#常见操作
print("===================字典常见操作===================")

#修改(存在便是删除)
dict['name'] = 'zhangsan'
print(dict)

#添加(不存在便是添加)
dict["weight"] = 130
print(dict)

#删除
#删除特定的元素，根据key寻找
del dict["name"]
print(dict)

#删除整个字典
del dict
print(dict)

dict1 = {"key":'hh','value':'gg'}
#清空字典
dict1.clear()
print(dict1)
