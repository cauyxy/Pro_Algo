import heapq

import models

###Dijskra算法,时间复杂度为o（n2）

inf = float('inf')


def heap_Dijsktra(e, i):
    heap = []
    dis = get_dis(e, i)  # 得到初始节点到其他各个节点的初始距离字典，方便保存节点的索引
    print(len(dis))
    for dic in dis:
        heapq.heappush(heap, [dis[dic], dic])
    visited = []  # 保存已访问过的节点
    min_index = None  # 未访问过节点中距离最小节点的索引
    min_dis = None
    while heap:
        min_node = heapq.heappop(heap)
        visited.append(min_node[1])
        min_index = min_node[1]
        min_dis = min_node[0]

        for key in heap:  # 找到最小节点之后对距离字典进行更新
            new_dis = min_dis + e[min_index][key[1]]
            if key[0] > new_dis:
                key[0] = new_dis
                dis[key[1]] = new_dis

    list_dis = [0 for _ in range(len(dis)+1)]
    for key in dis:  # 为方便后续使用，将字典转为list链表返回
        list_dis[key] = dis[key]
    return list_dis


def get_dis(e, i):  # 一个将图中第i行转化为对应字典的函数
    e_i = e[i]
    dis = {}
    for j in range(len(e_i)):
        if j != i:
            dis[j] = e_i[j]
    return dis


case4 = [
    [0, 3, 2, inf, inf],
    [inf, 0, inf, 1, inf],
    [inf, inf, 0, inf, inf],
    [4, inf, 6, 0, 4],
    [inf, inf, 4, inf, 0]
]


