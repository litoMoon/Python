# 发起请求所需要的信息
import requests
from utils.log import Log


class Request:
    logger=Log.getlog()
    host="http://8.147.235.67:8080/"
    def get(self,url,**kwargs):
       self.logger.info("正在发起get请求，请求url为：{}".format(url))
       self.logger.info("正在发起get请求，请求信息有{}".format(kwargs))
       r= requests.get(url=url,**kwargs)
       self.logger.info("get请求完成，响应的数据信息为：{}",r.json())
       return r


    def post(self,url,**kwargs):
       self.logger.info("正在发起 post 请求，请求信息有{}".format(kwargs))
       r = requests.post(url=url, **kwargs)
       self.logger.info("post请求完成，响应的数据信息为：{}".format(r.json()))
       return r