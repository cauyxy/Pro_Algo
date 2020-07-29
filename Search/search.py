from Search.BM import BM
from Search.KMP import KMP
from Search.Levenshtein import Levenshtein
from Search.CutWord import CutWord
from pypinyin import lazy_pinyin
from models import load2prog

def GetNode(id):
    nodes = load2prog("./data.dat")
    for node in nodes:
        if id==node.id:
            return node

def GetPinYin(turn):
    return "".join(lazy_pinyin(str(turn)))

def SelectAlogrithm(input,target):
    if(len(input)>=5):
        if(BM(input,target)):
            return 1
    else:
        if(KMP(input,target)):
            return 1
    return 100

def Search(input):
    ResNodes={x:100 for x in range(1,21)}
    SearchRes = []
    nodes = load2prog("./data.dat")

    for node in nodes:
        # 完全匹配搜索
        MatchTarget=[node.id,node.name,node.desc,node.level]
        for i in range(len(MatchTarget)):
            SelectRes=SelectAlogrithm(GetPinYin(input), GetPinYin(MatchTarget[i]))
            if i>=2:
                SelectRes+=1
            ResNodes[node.id]=min(ResNodes[node.id],SelectRes)

        input_word, input_pinyin = CutWord(input)
        desc_word, desc_pinyin = CutWord(node.desc)

        if(ResNodes[node.id]==100):
        #  部分匹配搜索
            for word in input_word:
                for i in range(len(MatchTarget)):
                    ResNodes[node.id] = min(ResNodes[node.id],SelectAlogrithm(word,str(MatchTarget[i])))

        if (ResNodes[node.id] == 100):
        #编辑距离搜索
            ResNodes[node.id] = max(ResNodes[node.id], Levenshtein(GetPinYin(input),GetPinYin(desc_word[0])))
            for word in desc_word:
                ResNodes[node.id] = min(ResNodes[node.id], Levenshtein(GetPinYin(input),GetPinYin(word)))

    ResNodesAftSort = sorted(ResNodes.items(), key=lambda item: item[1], reverse=False)
    for i in range(len(ResNodesAftSort)):
        SearchRes.append(GetNode(ResNodesAftSort[i][0]))
    return SearchRes

# SearchRes=Search("表")
# for node in SearchRes:
#     MatchTarget = [node.id, node.name, node.desc, node.level]
#     for line in MatchTarget:
#         print(line)

