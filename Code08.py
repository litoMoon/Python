# 针对文件操作--读写操作
# 使用内置方法 open 用于打开文件
# f=open("test.txt","w")
# print(f)
# print(type(f))
import os.path

# list=[]
# count=0
# 查看当前程序最多能打开多少个文件
# while True:
#     f=open("test.txt",'r')
#     list.append(f)
#     count+=1
#     print(f"打开 {count} 个文件了")

# 输出结果显示为打开 8189 个文件之后，就抛出了异常，数据再计算机中是按二进制数据来进行存储的。
# 8189 + 3 = 8192 是2的13次方，这里还差的3个文件，不是没有没有打开，是当程序运行起来之后默认会有三个
# 会有三个默认的文件被打开，第一个是标准输入，第二个是标准输出，第三个是标准错误
# 当然这里的最大可以打开的文件数是可以自己配置的
# 使用方法 close 用于关闭打开的文件


# 这里的当前相对路径表示当前项目Code09.py所在的路径，是C:\PycharmProject\pythonProject这个路径下，所以说这里打开的test.txt
# 是打开 C:\PycharmProject\pythonProject 这个路径下的文件，由于当前没有文件存在，所以说会创建一个新的独立的文件，是创建再这个
# C:\PycharmProject\pythonProject 目录下的文件
# f = open("test.txt", "w")

# 打开文件---..表示上一级目录，从C:\PycharmProject\pythonProject，回到了C:\PycharmProject这级目录
# f = open("../test.txt", "w")
# 写文件
# f.write("hello world")
# 关闭文件
# f.close()

#现在删除C:\PycharmProject\pythonProject目录下t est.txt 文件
# 先判断文件是否存在
# file_name="test.txt"
# if os.path.exists(file_name):
#     os.remove(file_name)

# 打开文件---..表示上一级目录，从C:\PycharmProject\pythonProject，回到了C:\PycharmProject这级目录
# f = open("../test.txt", "w",encoding='UTF-8' ) #这里表示写按照utf-8的编码格式去写，如果这里不规定写进记事本的数据直接打开会乱码

# f = open("../test.txt", "r",encoding='UTF-8' )
#若在进行读写操作时，没有指定默认的编码格式，python解释器会用默认的 GBK 编码方式来解释
# 为了避免乱码需要加上 encoding 的关键字参数
f = open("../test.txt", "r",encoding='utf-8')

# 写文件
# f.write("你好，世界！")
# 读文件---1.使用readLines()方法
# 使用 readLines() 方法默认是读取一行数据，且读取到的数据默认会加一个 “\n”换行符
# for elem in f.readlines():
#     print(elem,end="")
# 读文件---2.使用文件对象，python默认文件对象是可迭代的对象
for elem in f:
    print(elem,end="") # end 默认参数是 \n
# 关闭文件
f.close()