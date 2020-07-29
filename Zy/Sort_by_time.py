from Sort.QuickSort import QuickSort
from cmps import cmp2
import models
#根据知识点的课时进行排序

def Sort_by_time():
    nodes=models.load2prog('data.dat')
    sorted_nodes=QuickSort(nodes,cmp2)
    return sorted_nodes


