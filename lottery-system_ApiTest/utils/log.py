# 操作日志所需的操作
import logging
import os.path
import time

class info_Filter(logging.Filter):
    def filter(self, record):
         return record.levelno==logging.INFO
class err_Filter(logging.Filter):
    def filter(self, record):
        return record.levelno==logging.ERROR
class Log:
    # 获取到 log对象
    @classmethod
    def getlog(cls):
        cls.logger=logging.getLogger(__name__)
        # 设置日志级别
        cls.logger.setLevel(logging.DEBUG)
        LOG_PATH = "./logs/"
        # 获取日期
        now = time.strftime("%Y-%m-%d")
        # 设置不同的文件处理器
        All_log=LOG_PATH + now +".log"
        Info_log=LOG_PATH + now +"-info.log"
        Err_log=LOG_PATH + now+"-err.log"
        # 创建 logs 包，和文件处理器，将文件处理器放在 logs 包下
        if not os.path.exists(LOG_PATH):
        #     创建
            os.mkdir(LOG_PATH)
        # 创建文件处理器--当代码执行到这里会自动创建相应的文件
        all=logging.FileHandler(All_log,encoding="utf-8")
        info=logging.FileHandler(Info_log,encoding="utf-8")
        err=logging.FileHandler(Err_log,encoding="utf-8")

        # 设置输出格式
        # 创建⼀个⽇志格式器对象
        formatter = logging.Formatter(
            "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d)] - %(message)s")
        # 将格式器设置到处理器上
        all.setFormatter(formatter)
        info.setFormatter(formatter)
        err.setFormatter(formatter)

        # 添加过滤器--传入的参数为过滤的类对象
        info.addFilter(info_Filter())
        err.addFilter(err_Filter())

        # 将处理器加入到logger
        cls.logger.addHandler(all)
        cls.logger.addHandler(info)
        cls.logger.addHandler(err)

        return cls.logger
