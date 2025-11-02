# 使用字符串的一些方法
# data="hello world"
# print(len(data))  #输出结果为 11
# data1="hello "
# data2="world"
# 对字符串进行拼接---拼接是会形成一个新的字符串，不会影响原来的字符串数据
# print(data1+data2)
# print(data1)
# print(data2)

#求字符串长度
# print(len(data1))
# print(len(data2))

# 字符串的比较，注意这里字符串的比较可以直接使用><号来进行比较
# 字符串的比较是根据字典序来进行比较的，字典序越靠后的字符串越大
# print(data1>data2)
# print(data2>data1)
# print(id(data1))
# print(id(data2))

# 字符串常量
# data1="hello world"
# data2="hello world"
# print(f"data1 is not data2 :{data1 is not data2}")
# print("data1 is not data2 :",data1 is not data2)  # 输出为 false ，表示这俩是同一个

# 字符串的切片操作
data="我爱我的祖国"
print(data)
print(data[1:4])
