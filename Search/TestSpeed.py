from Search.BF import BF
from Search.BM import BM
from Search.KMP import KMP
import os
import random
import time
def GetRandomStr(length):
    source='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    str=''
    for i in range(length):
        str+=random.choice(source)
    return str

def CreateTestFile():
    target = GetRandomStr(100000000)
    file = open('TestStr.txt', 'w')
    file.flush()
    file.write(target)
    os.fsync(file)
    file.close()

def ReadTestFile():
    file = open('TestStr.txt', 'r')
    file.flush()
    target=file.read()
    os.fsync(file)
    file.close()
    return target

def Test():
    target=ReadTestFile()
    print("字符串长度:"+str(len(target)))
    for i in range(10):
        print("第"+str(i+1)+"次测试")
        input=GetRandomStr(1)
        for j in [BF,KMP,BM]:
            StartTime=time.time()
            j(input,target)
            print(str(j))
            print("用时："+str(round(time.time()-StartTime,2))+"s")
Test()



