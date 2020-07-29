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
    file = open('TestSpeedStr.txt', 'w')
    file.flush()
    file.write(target)
    os.fsync(file)
    file.close()

def ReadTestFile():
    file = open('TestSpeedStr.txt', 'r')
    file.flush()
    target=file.read()
    os.fsync(file)
    file.close()
    return target

def Test():
    target=ReadTestFile()
    file = open('TestSpeedRes.txt', 'w+')
    file.write("字符串长度:"+str(len(target)))
    file.write('\r\n')
    TestAlogrithm = [BF, KMP, BM]
    for input_length in range(1,10):
        file.write("模式长度为" + str(input_length))
        file.write('\r\n')
        CostTime = [0, 0, 0]
        for i in range(10):
            file.write("-----正在进行模式长度为"+str(input_length)+"的第"+str(i+1)+"次测试")
            file.write('\r\n')
            input=GetRandomStr(input_length)
            for j in range(3):
                StartTime=time.time()
                TestAlogrithm[j](input,target)
                file.write("-------------------------"+str(TestAlogrithm[j]))
                t=time.time()-StartTime
                CostTime[j]+=t
                file.write("用时："+str(round(t,2))+"s")
                file.write('\r\n')
        for i in range(3):
            file.write("-----"+str(TestAlogrithm[i]))
            file.write("总时长：" + str(round(CostTime[i], 2)) + "s")
            file.write('\r\n')
    file.close()
Test()



