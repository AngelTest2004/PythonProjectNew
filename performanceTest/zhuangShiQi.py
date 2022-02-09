
#for decoration
import time

rs_list=[]
def monitor(func ):
    def inner(*args):
        startTime=time.time()*1000
        func(*args)
        endTime=time.time()*1000
        duration=endTime-startTime
        rs_list.append(duration)
    return inner

def loop(interation):
    def loop(func):
        def inner(*args):
            for i in range(interation):
                startTime = time.time() * 1000
                func(*args)
                endTime = time.time() * 1000
                duration = endTime - startTime
                rs_list.append(duration)
        return inner
    return loop;