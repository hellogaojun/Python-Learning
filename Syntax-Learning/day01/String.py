
#TODO:定义字符串的三种方式
string = 'hello python'
string1 = "hello python1"
string2 = """
hello python hello python hello python hello python
"""
print(string,string1,string2)


#TODO:字符串的输入输出
name = "zhang"
position = "讲师"
address = "北京"
print('----------------------------------------------')
print("name:%s"%name)
print("position:%s"%position)
print("address:%s"%address)
print('----------------------------------------------')

"""
userName = input("请输入用户名:")
print("用户名：%s"%userName)
password = input("请输入密码:")
print("密码：%s"%password)

"""



#TODO:下标索引
name = "gaojun"
print(name[2]) #o

#TODO:切片(字符串截取)
#语法：[起始:结束:步长] 左闭又开区间,索引，步长可以为负数
testStr = "hello python"

#索引0～2之间的字符，不包括索引2
print(testStr[0:2])
#索引为3的字符
print(testStr[3:4])
#从索引3开始之后的全部字符
print(testStr[3:])
#全部字符
print(testStr[:])
#索引1～倒数第一个之间的字符，不包括倒数第一个
print(testStr[1:-1])
#索引1～6之间的字符，每次跨步2
print(testStr[1:6:2])
#索引0～3之间的字符
print(testStr[:3])
#全部字符，跨步2截取
print(testStr[::2])
#无符合要求字符
print(testStr[5:1:2])
#索引1～5之间的字符，每次跨步2
print(testStr[1:5:2])
#全部字符串倒数算起，跨步2
print(testStr[::-2])
#索引5～1之间的字符倒数算起,跨步为2
print(testStr[5:1:-2])



#TODO:字符串常用方法
myStr = "  hello world itcast and itcastcpp  "

#Return the lowest index in S where substring sub is found,
# Return -1 on failure.
find = myStr.find("itcast",0,10)
print(find)

#Return the highest index in S where substring sub is found,
#Return -1 on failure.
rfind = myStr.rfind("itcast")
print(rfind)

#Return the lowest index in S where substring sub is found,
# Raises ValueError when the substring is not found.
index = myStr.index("cpp")
print(index)

#Return the highest index in S where substring sub is found,
# Raises ValueError when the substring is not found.
rindex = myStr.rindex("cpp")
print(rindex)

#Return the number of non-overlapping occurrences of substring sub in
#        string S[start:end].
count = myStr.count("itcast")
print(count)

"""
        Return a copy with all occurrences of substring old replaced by new.

          count
            Maximum number of occurrences to replace.
            -1 (the default value) means replace all occurrences.

        If the optional argument count is given, only the first count occurrences are
        replaced.
"""
myStr1 = myStr.replace("cpp","c++",1)
print(myStr1)

#Return a list of the words in the string, using sep as the delimiter string.
myStr1 = myStr.split(" ",2)
print(myStr1)

#Return a capitalized version of the string.
# make the first character have upper case and the rest lower case.
myStr1 = myStr.capitalize()
print(myStr1)

#Return a version of the string where each word is titlecased.
# words start with uppercased characters and all remaining cased characters have lower case.
myStr1 = myStr.title()

# Return True if S starts with the specified prefix, False otherwise.
isStartrTrue = myStr.startswith("hh")
print(isStartrTrue)

#Return True if S ends with the specified suffix, False otherwise.
isEndTrue = myStr.endswith("cpp")
print(isEndTrue)

#Return a copy of the string converted to uppercase.
upperStr = myStr.upper()
print(upperStr)

#Return a copy of the string converted to lowercase.
lowerStr = myStr.lower()
print(lowerStr)

#TODO:这几个方法比较特殊。。。
myStr1 = myStr.ljust(4)
print(myStr1)

myStr1 = myStr.rjust(3)
print(myStr1)

myStr2 = myStr.center(8)
print(myStr2)



#删左侧空白字符串
myStr.lstrip()
#删右侧空白字符串
myStr.rstrip()
print(myStr)

a = "\n\t kkb \n"
a1 = a.strip()
print(a1)

#以给定的字符串为准，分三部分(正向)
myStr3 = myStr.strip().partition("itcast")
print(myStr3)
#以给定的字符串为准，分三部分(逆向)
myStr3 = myStr.strip().rpartition("itcast")
print(myStr3)

list = myStr.strip().splitlines()
print(list)

#Return True if the string is an alphabetic string, False otherwise.
is_alpha = myStr.strip().isalpha()
#Return True if the string is a digit string, False otherwise.
is_digital = myStr.strip().isdigit()
#Return True if the string is an alpha-numeric string, False otherwise.
is_alnum = myStr.strip().isalnum()
#Return True if the string is a whitespace string, False otherwise.
is_space = myStr.isspace()
print(is_alpha,is_digital,is_alnum,is_space)

#TODO:这个方法比较特殊
#原有的字符串前插入指定的字符（有几个插入几次，字符数要多于1）
myStr6 = myStr.strip().join("ggg")
print(myStr6)

