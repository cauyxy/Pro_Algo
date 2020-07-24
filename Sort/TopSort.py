####拓扑排序

import models
import heapq #用到了python中的堆

heap = []   #用于存储节点的优先队列
nodes=[]    #用于存储节点列表
nums=[]     #用于存储各个节点的入度

def TopSort(e,n):
    tol_time=0
    ans = []
    for i in range(0,n):
        if nums[i]==0:    #表示该节点入度为0,将其加入到heap中
            heapq.heappush(heap,nodes[i])
    len=0

    while heap:
        top_node=heapq.heappop(heap)  #按难度取节点，令节点的所有后续点入度-1
        ans.append(top_node.name)     #更新答案路径
        tol_time += top_node.time         #更新时间
        for node in top_node.aft_list:    #更新当前节点后续节点的入度
            nums[node.id]-=1
            if nums[node.id]==0:
                heapq.heappush(heap, nodes[node.id])

    return tol_time,ans










