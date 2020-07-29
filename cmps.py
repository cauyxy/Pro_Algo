def cmp1(node1, node2, dis=[]):
    if node1.level != node2.level:
        return node1.level < node2.level
    else:
        return node1.id < node2.id


def cmp2(node1, node2, dis=[]):
    if node1.time != node2.time:
        return node1.time < node2.time
    else:
        return node1.id < node2.id


def cmp3(node1, node2, dis=[]):  # dis为用SFPA算法或dijskra算法计算出的到各个节点的最短距离
    if dis[node1.id - 1] != dis[node2.id - 1]:
        return dis[node1.id - 1] <= dis[node2.id - 1]
    elif node1.level != node2.level:
        return node1.level <= node2.level
    elif node1.time != node2.time:
        return node1.time <= node2.time
    else:
        return node1.id <= node2.id
