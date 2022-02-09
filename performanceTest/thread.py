import requests
import json
import unittest
import threading
import time
import psutil

cpuList=[]
memList=[]

class Test:

    def Test(self):
        self.url = "http"
        print("start")

    def apiTest(self):
        startTime=int(time.time()*1000) #unit is ms
        data={"1":1,"2":2}
        request=requests.post(self.url,data)
        response=request.json()
        endTime=int(time.time()*1000) #unit is ms
        responTime=endTime-startTime

    def monitor(self):
        cpu=psutil.cpu_percent()
        mem=psutil.virtual_memory()
        global cpuList,memList #读取全局变量时需要声明 否则后面会作为一个局部变量使用
        cpuList.append(cpu)
        memList.append(mem)

if __name__=="__main__":

    for i in range(1,6):
        t= Test()
        threadT=threading.Thread(traget = t.apiTest)
        threadT.setDaemon(True) #设置为主线程的守护线程，主线程结束，守护进程就结束了
        threadT.start()

    monitorT=threading.Thread(target=t.monitor())
    monitorT.setDaemon(True)
    monitorT.start()
    threadT.join()  # 子线程结束后，主线程才会往后执行





