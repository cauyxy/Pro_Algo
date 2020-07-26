from models import *
from Search.FindPre import FindPre
from Sort.TopSort import TopSort
#规划到node节点的学习路径并最短学习时间

def Top_Sort(node):
    heap = []  # 用于存储节点的优先队列
    nums = []  # 用于存储各个节点的入度
    pre_list = FindPre(node)    #找出学习改课程所需的所有前序课程

    length = len(pre_list)
    nums = [float('inf') for _ in range(20)]

    for node in pre_list:
        nums[node.id - 1] = len(node.pre_list)

    time, ans = TopSort(20, pre_list,nums)
    return time,ans

nodes=load2prog("../data.dat")
time,dis=Top_Sort(nodes[-1])
print(time)
print(dis)