from models import load2prog
from Search.BF import BF
from Search.BM import BM
from Search.KMP import KMP
from Search.Levenshtein import Levenshtein
data=load2prog("data.dat")
TestAlogrithm = [BF, KMP, BM,Levenshtein]
for node in data:
    target=node.desc
    for Test in TestAlogrithm:
        res=Test("数据",target)
        if Test==Levenshtein:
            if(res<10):
                print(str(Test))
                print(target)
        elif(res):
            print(str(Test))
            print(target)

