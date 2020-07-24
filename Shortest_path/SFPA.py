###SFPA算法

from queue import Queue


inf=float('inf')
def spfa(e,i):
    length=len(e[0])
    queue = Queue()
    visted=[0 for _ in range(length)]
    dis=[inf for _ in range(length)]

    dis[i]=0    #初始节点到自己的距离为0
    queue.put(i)   #初始节点入队
    visted[i] = 1  #初始节点已经被访问过

    while not queue.empty():
        v=queue.get()    #取得队列中的第一个顶点
        visted[v]=0

        for i in range(length):
            new_dis=dis[v]+e[v][i]
            if new_dis<dis[i] and e[v][i]>0:
                dis[i]=new_dis
                if visted[i]==0:    #距离被更新的点才会入队
                    queue.put(i)
                    visted[i]=1
    return dis

case1 = [
    [0,10,inf,inf,inf,9,15],
    [10,0,inf,inf,inf,2,inf],
    [inf,inf,0,inf,1,inf,10],
    [inf,inf,inf,0,7,inf,inf],
    [inf,inf,1,7,0,inf,12],
    [9,2,inf,inf,inf,0,3],
    [15,inf,10,inf,12,3,0]
]

case2 = [[0, 1, 12, inf, inf, inf],
         [inf, 0, 9, 3, inf, inf],
         [inf, inf, 0, inf, 5, inf],
         [inf, inf, 4, 0, 13, 15],
         [inf, inf, inf, inf, 0, 4],
         [inf, inf, inf, inf, inf, 0]]

case4 = [
        [0,3,2,inf,inf],
        [inf,0,inf,1,inf],
        [inf,inf,0,inf,inf],
        [4,inf,6,0,4],
        [inf,inf,4,inf,0]
]


dis = spfa(case4,0)
print(dis)