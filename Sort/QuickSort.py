###快排nlog，数据量较大时，速度快于归并排序，同样需要额外的空间开销


def QuickSort(arr, cmp, dis=[]):
    length = len(arr)
    if length < 2:  # 为空或只有一个节点的数组为有序的数组
        return arr
    pivot = arr[0]  # 每次均选取数组第一个作为基准元素
    less = []
    greater = []
    for i in range(1, length):  # 分别将比基准元素小的和大的元素存储到less和greater中
        if cmp(arr[i], pivot, dis):
            less.append(arr[i])
        else:
            greater.append(arr[i])
    return QuickSort(less, cmp, dis) + [pivot] + QuickSort(greater, cmp, dis)  # 递归进行排序
