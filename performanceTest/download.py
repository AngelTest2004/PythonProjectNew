import os

import requests,re
from bs4 import BeautifulSoup
from  zhuangShiQi import rs_list,monitor,loop  #导入装饰器和其中的全局变量

url1="https://www.woniuxy.com/woniusales"
url2="https://www.baidu.com"
httplink=[]

class download:
    def __init__(self):
        self.re=requests.session()

    def home(self):
        global url2
        result=self.re.get(url1)
        self.getLink(result.text)

    #使用装饰器 zhuangShiQi.py 中定义的方法
   # @monitor
   # @loop(2)
    def getLink(self, text):
        link = []
        link += re.findall('src="(.*?)\?"', text)
        #link += re.findall('href=//(.*)name', text)
        #link += re.findall('url="\(.*?\)"', text)

        #获取上一级目录
        folder=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        folder=folder+r"\downloadFile"
        fileList=os.listdir(folder)

        global httplink
        httpSlide=[]
        for item in link:
            if item.startswith("/"):
                l=url1+item

            elif item.startswith("http"):

                l=item
                httpSlide=item.splite("/")
                item=httpSlide[len(httpSlide)-1]

            else :i=2
            httplink.append(l)
            fileNmae = item.replace("/", "_")
            if not( fileNmae in fileList):
               result = self.re.get(l)  #重新请求，没有保存在本地
               with open(folder+"\\"+fileNmae,'wb') as file:
                 file.write(result.content)



    def parseText ( text ):
        msg = BeautifulSoup(text)
        global httplink
        for item in msg.findAll("a"):
            print(item.get("href"))


if __name__ == "__main__":
    dw=download()
    dw.home()