import logging

# 注意这里使用 pytest 进行操作的时候，
# 不会打印 logging 打印的信息，会打印 print 所在的信息
def estLogging():
    logging.debug("this is a debug message")
    logging.info("this is a info message")
    logging.warning("this is a warn message")
    logging.error("this is a error message")
    logging.critical("this is a critical message")
    print("xixi")
