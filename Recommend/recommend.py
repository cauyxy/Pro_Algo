from models import load2prog


def GetNode(id):
    nodes = load2prog("data.dat")
    for node in nodes:
        if id == node.id:
            return node


def IsLearnable(LearntLevel, AftLevel, Grade):
    # 通过已学习知识点难度、分数和后续知识点难度判断该后续知识点是否可推荐
    if ((AftLevel - LearntLevel) > 4):
        if Grade >= 80:
            return 1
        else:
            return 0
    elif ((AftLevel - LearntLevel) <= 4 and (AftLevel - LearntLevel) > 2):
        if Grade >= 70:
            return 1
        else:
            return 0
    elif ((AftLevel - LearntLevel) <= 2):
        if Grade >= 60:
            return 1
        else:
            return 0


def Count(LearntNodes_id, Grades):
    # 统计推荐节点记录次数，进行推荐排序
    CountList = {x: 0 for x in range(1, 100)}
    for i in range(len(LearntNodes_id)):
        LearntNode = GetNode(LearntNodes_id[i])
        for AftNode in LearntNode.aft_list:
            if IsLearnable(LearntNode.level, AftNode.level, int(Grades[i])):
                CountList[AftNode.id] += 1
    CountListAftSort = sorted(CountList.items(), key=lambda item: item[1], reverse=True)
    return CountListAftSort


def GetRecommendNodes(CountListAftSort):
    # 给出推荐知识点序列
    RecommendNodes = []
    for i in range(len(CountListAftSort)):
        if (CountListAftSort[i][1] > 0):
            RecommendNodes.append(GetNode(CountListAftSort[i][0]))
    return RecommendNodes


def Recommend(LearntNodes_id, Grades):
    # 推荐算法
    CountListAftSort = Count(LearntNodes_id, Grades)
    return GetRecommendNodes(CountListAftSort)
