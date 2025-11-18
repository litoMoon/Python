'''
对创建奖品接口进行测试
'''
import os.path
from importlib.metadata import files
from venv import logger

import requests

from utils.Requests import Request
from utils.log import Log


class TestPrizeCreat:
    url=Request().host+"prize/crete"
    logger=Log.getlog()
    def test_create_prize(self):
        header={"User_token":"eyJhbGciOiJIUzI1NiJ9.eyJpZGVudGl0eSI6IkFETUlOIiwiaWQiOjY0LCJpYXQiOjE3NjM0Njk3MzMsImV4cCI6MTc2MzQ3MzMzM30.KZKxZDd9hRWeBUZkQiidfMShplg3la9M91GLGNiNgNI"}
        # 防止转义字符这里加上双斜杠--这里打开文件了没有关闭文件，注意在完成后需要关闭文件
        param_file=open(os.path.join("C:\\PIC","param.json"),"rb")
        pic_file=open(os.path.join("C:\\PIC","水杯.jpg"),"rb")
        # param_file = open(os.path.join(r"C:\PIC", "param.json"))
        # pic_file = open(os.path.join(r"C:\PIC", "水杯.jpg"))
        file=[
            ("param",("param.json",param_file,"application/json")),
            ("prizePic",("水杯.jpg",pic_file,"image/jpeg"))
        ]
        logger.info("正在执行创建奖品操作")
        Request().post(url=self.url,headers=header,files=file)
        logger.info("奖品创建完成")

        pic_file.close()
        param_file.close()


