###归并排序nlog,数据量较大时，速度慢于快排，需要额外的空间开销，用于保存数组
from cmps import *
from Shortest_path.Dijskra import Dijsktra
import models

def merge(arr, l, r, m,cmp,dis=[]):    #合并函数
    n1 = m - l + 1
    n2 = r - m

    L = [0 for _ in range(0, n1)]
    R = [0 for _ in range(0, n2)]

    for i in range(0, n1):     #L存储待排序数组的左半部分
        L[i] = arr[l + i]

    for j in range(0, n2):     #R存储待排序数组的右半部分
        R[j] = arr[m + j + 1]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:    #将L和R中按从小到大顺序移到数组中
        if cmp(L[i],R[j],dis):
            arr[k] = L[i]
            i += 1
            k += 1
        else:
            arr[k] = R[j]
            j += 1
            k += 1

    while i < n1:      #将L和R中剩余元素移到arr中
        arr[k] = L[i]
        k += 1
        i += 1

    while j < n2:
        arr[k] = R[j]
        k += 1
        j += 1


def MergeSort(arr, l, r,cmp,dis=[]):      #递归进行归并排序
    if l < r:
        m = int((l + r - 1) / 2)
        MergeSort(arr, l, m,cmp,dis)
        MergeSort(arr, m + 1, r,cmp,dis)
        merge(arr, l, r, m,cmp,dis)
    return arr

