import logging
from cgitb import handler
from fileinput import filename

# 这里在进行日志级别的设置，这里设置表示输出日志的级别为 debug 级别的日志
# 如果没有进行日志级别的设置，默认输出日志的的级别为 warning
logging.basicConfig(level=logging.INFO)

# logging.debug("this is a debug message")
# logging.info("this is a info message")
# logging.warning("this is a warn message")
# logging.error("this is a error message")
# logging.critical("this is a critical message")

# 获取一个日志记录器对象--创建日志对象--"my_logger"是创建的日志对象的名称
logger=logging.getLogger("my_logger")

# 创建文件处理器
result=logging.FileHandler(filename="mylog.log")
# 创建⼀个⽇志格式器对象
formatter = logging.Formatter("%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d)] - %(message)s")
# 将格式器设置到文件处理器上---表示日志的打印格式是怎么样的
result.setFormatter(formatter)
# 将文件处理器加入到日志对象中,表示日志输出到文件处理器中
logger.addHandler(result)
# 设置日志记录器的日志级别
logger.setLevel(logging.DEBUG)

if __name__=="__main__":
    logger.debug("this is debug logging")
    logger.info("this is info logging")
    logger.warning("this is warning logging")
    logger.error("this is error logging")
    logger.critical("this is critical logging")


# 注意 python 在接收返回值时,直接随机创建一个对象就行了,只要对象名称不会与关机键名称重复
# 因为对象的类型根本不需要考虑,变量的类型通过变量的赋值可以体现出来


