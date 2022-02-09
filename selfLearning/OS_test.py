import os
import os.path
import zipfile
import calendar

#取得当前文件的绝对路径
s=os.getcwd()
cp=os.curdir
print(s)
print(cp)
#修改工作目录
#os.chdir("c:\\")

z = 10
class cla():
    def __init__(self,year,month):
        days = calendar.monthrange(year,month)
        self.fd = days[0]+1
        self.d = days[1]

    def count(self):
        day=1
        print("Mon Tue Wen Thu Fri Sat Sun")
        while day<=self.d:

          for i in range(1,8):

            if day>self.d or ( day==1 and i<self.fd ):
              print(" "*4,end='')
            else:
              print(" {:0>2d} ".format(day),end="")
              day=day+1
          print()

class test():

    name="name"
    __private=1
    def __init__(self):
        self.age=2
        self.grade=4

    def set_age(self,age):
        self.age=age
        grade = 2


if __name__=="__main__":
    #show = cla(2022,3)
    #show.count()
    a=test()
    b=test()
    a.sex="M"  #可以追加属性
    a.set_age(4)
    #print(b.sex) #b 没有被追加sex 属性
    #print(a.grade)   #不能访问
    print()
    b.name=8
    print(a.name)
    print()
    del a.age
    print(b.age)
    print()
    test.name="changed"
    print(test.name)
    print (b.name)
    #print(test.age) 实例成员被删了，类成员也被删了





