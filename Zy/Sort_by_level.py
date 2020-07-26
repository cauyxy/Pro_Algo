from Sort.QuickSort import QuickSort
from cmps import cmp1
import models
#根据课程难度给知识点排序


def Sort_by_level():
    nodes=models.load2prog('../data.dat')
    sorted_nodes=QuickSort(nodes,cmp1)
    return sorted_nodes

aft_list=Sort_by_level()
for nodes in aft_list:
    print(nodes.name)
