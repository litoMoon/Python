

from utils.log import Log

if __name__=="__main__":
    logger=Log.getlog()
    logger.info("---this is a info message---")
    logger.error("---this is a error message---")

