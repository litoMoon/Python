import yaml

# 进行数据的写入进 yaml 中
def write_yml(filename,data):
    with open(filename,encoding="utf-8",mode="a+") as f:
        yaml.safe_dump(data,stream=f)

# 从 yaml 中读出数据
def read_yml(filename,key):
    with open(filename,encoding="utf-8",mode="r") as f:
        data=yaml.safe_load(f)  # 从打开的 f 文件进行数据的读取并存放到 data 中
        return data[key]  # 返回 data 中指定字段 key 的值
# 清空 yml
def clear_yml(filename):
    with open(filename,encoding="utf-8",mode="w") as f:
        f.truncate()