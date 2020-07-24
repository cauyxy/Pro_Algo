###快排

def QuickSort(arr):
    length=len(arr)
    if length < 2:  # 为空或只有一个节点的数组为有序的
        return arr
    pivot = arr[0]
    less = []
    greater = []
    for i in range(1,length):
        if arr[i]<=pivot:
            less.append(arr[i])
        else:
            greater.append(arr[i])
    return QuickSort(less)+[pivot]+QuickSort(greater)