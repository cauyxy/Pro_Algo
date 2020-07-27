from models import load2prog
def GetNode(id):
    nodes = load2prog("./data.dat")
    for node in nodes:
        if id==node.id:
            return node

def IsLearnable(LearntLevel, AftLevel, Grades):
    if((AftLevel - LearntLevel)>4):
        if Grades>=80:
            return 1
        else:
            return 0
    elif((AftLevel - LearntLevel) <= 4 and (AftLevel - LearntLevel) > 2):
        if Grades>=70:
            return 1
        else:
            return 0
    elif((AftLevel - LearntLevel) <= 2):
        if Grades>=60:
            return 1
        else:
            return 0

def Count(LearntNodes_id,Grades):
    CountList={x:0 for x in range(1,21)}
    for i in range(len(LearntNodes_id)):
        LearntNode=GetNode(LearntNodes_id[i])
        for AftNode in LearntNode.aft_list:
            print(AftNode.name)
            if IsLearnable(LearntNode.level,AftNode.level,Grades[i]):
                CountList[AftNode.id]+=1
    CountListAftSort=sorted(CountList.items(), key=lambda item:item[1], reverse=True)
    return CountListAftSort

def GetRecommendNodes(CountListAftSort):
    RecommendNodes=[]
    for i in range(len(CountListAftSort)):
        if(CountListAftSort[i][1]>0):
            RecommendNodes.append(GetNode(CountListAftSort[i][0]))
    return RecommendNodes

def Recommend(LearntNodes_id,Grades):
    CountListAftSort=Count(LearntNodes_id,Grades)
    return GetRecommendNodes(CountListAftSort)


