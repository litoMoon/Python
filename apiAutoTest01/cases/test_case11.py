# 针对 yml 文件进行操作
import pytest
import yaml
from setuptools.command.egg_info import write_toplevel_names

# 凡是针对文件操作的，一定要记得，对文件的任何操作之前一定是先打开文件，
# 对文件执行完相应的操作之后，一定是关闭文件操作


# 往 yml 文件中写入数据
def writeToYml(filename,data):
        # 这里 a+ 的 mode 表示追加写，会从文件中已有的数据接着往后写
        # 如果这里的 mode 为 w ，表示写，但是之前文件中已经存在的内容就消失了
    with open(filename,mode="a+",encoding="utf-8") as f:
            # 注意这里往 yml 文件中写入数据时，使用的方法是 safe_dump
        f.write("---\n")
        yaml.safe_dump(data,stream=f)

    # 从 yml 中读取文件数据
def readFromYml(filename):
    with open(filename,encoding="utf-8",mode="r") as f:
            # 从哪儿读数据，从文件 f 中读数据
        data = list(yaml.safe_load_all(f))
        return data

    # 清除 yml 文件中的内容信息
def clearYml(filename):
    with open(filename,encoding="utf-8",mode="w") as f:
        f.truncate()  #这里是对文件执行清除操作，清除操作也就意味着对文件执行写操作
    # 测试 yml 文件的读写操作
def test_write():
    writeToYml("test.yml",{
            "name":"zhangsan",
            "age":"20"
    })

def test_read():
    print(readFromYml("test.yml"))

def test_clear():
    clearYml("test.yml")