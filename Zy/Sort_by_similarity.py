from Sort.QuickSort import QuickSort
from cmps import cmp3
from Shortest_path.Dijskra import Dijsktra
import models
#根据到所需知识点的相似度对知识点进行排序

def Sort_by_similarity(node):
    nodes = models.load2prog('../data.dat')
    edgs = models.To_Graph()
    dis = Dijsktra(edgs, node.id-1)
    sorted_nodes = QuickSort(nodes, cmp3, dis=dis)
    return sorted_nodes

