import models
from FindPreAft.FindPre import FindPre
from Shortest_path.Dijskra import Dijsktra
from Sort.QuickSort import QuickSort
from Sort.TopSort import TopSort
from cmps import *


def Sort_by_level():
    nodes = models.load2prog('data.dat')
    sorted_nodes = QuickSort(nodes, cmp1)
    return sorted_nodes


def Sort_by_similarity(node):
    nodes = models.load2prog('data.dat')
    edgs = models.To_Graph()
    dis = Dijsktra(edgs, node.id - 1)
    sorted_nodes = QuickSort(nodes, cmp3, dis=dis)
    return sorted_nodes


def Sort_by_time():
    nodes = models.load2prog('data.dat')
    sorted_nodes = QuickSort(nodes, cmp2)
    return sorted_nodes


def Top_Sort(node):
    heap = []  # 用于存储节点的优先队列
    nums = []  # 用于存储各个节点的入度
    pre_list = FindPre(node)  # 找出学习改课程所需的所有前序课程

    length = len(pre_list)
    nums = [float('inf') for _ in range(20)]

    for node in pre_list:
        nums[node.id - 1] = len(node.pre_list)

    time, ans = TopSort(20, pre_list, nums)
    return time, ans
