from models import *
from Search.FindPre import FindPre
####拓扑排序

import models
import heapq #用到了python中的堆

heap = []   #用于存储节点的优先队列
nums = []     #用于存储各个节点的入度

def TopSort(n,nodes):
    tol_time=0
    ans = []
    for node in nodes:
        if nums[node.id-1]==0:    #表示该节点入度为0,将其加入到heap中
            heapq.heappush(heap,node)

    while heap:
        top_node=heapq.heappop(heap)  #按难度取节点，令节点的所有后续点入度-1
        ans.append(top_node.name)     #更新答案路径
        tol_time += top_node.time         #更新时间
        for node in top_node.aft_list:    #更新当前节点后续节点的入度
            nums[node.id-1]-=1
            if nums[node.id-1]==0:
                heapq.heappush(heap, node)
    return tol_time,ans



nodes=load2prog("../data.dat")


pre_list=FindPre(nodes[-3])
for nodes in pre_list:
    print(nodes.name)


length=len(pre_list)
nums = [float('inf') for _ in range(20)]

for node in pre_list:
    nums[node.id-1]=len(node.pre_list)



time,ans=TopSort(length,pre_list)
print(time,ans)






