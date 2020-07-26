from models import *

###Dijskra算法

inf = float('inf')


def Dijsktra(e, i):
    dis = get_dis(e, i)  # 得到初始节点到其他各个节点的初始距离字典，用字典是为了保存节点的索引，方便在下文找出距离最小且未被访问过的节点索引，若使用
    visited = []  # list，则排序后无法确定当前节点是否已经为最优解
    path = []
    min_index = None
    min_dis = None
    for j in range(len(dis)):
        sorted_dis = sorted(dis.items(), key=lambda item: item[1])  # 对字典按值排序，返回一个元组链表，元组第一个元素为节点id，第二个元素为节点到初始节点的距离
        for tup in sorted_dis:  # 找到距离最小且未被访问过的节点
            if tup[0] not in visited:
                visited.append(tup[0])
                path.append(tup[0])
                min_index = tup[0]
                min_dis = tup[1]
                break

        for key in dis:  # 找到最小节点之后对dis字典进行更新
            new_dis = min_dis + e[min_index][key]
            if dis[key] > new_dis:
                dis[key] = new_dis
        list_dis=[0 for _ in range(20)]
        for key in dis:
            list_dis[key]=dis[key]
    return list_dis


def get_dis(e, i):
    e_i = e[i]
    dis = {}
    for j in range(len(e_i)):
        if j != i:
            dis[j] = e_i[j]
    return dis
