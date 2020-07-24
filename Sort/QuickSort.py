###快排

def QuickSort(arr):
    length=len(arr)
    if length < 2:  # 为空或只有一个节点的数组为有序的数组
        return arr
    pivot = arr[0]  #每次均选取数组第一个作为基准元素
    less = []      
    greater = []   
    for i in range(1,length):     #分别将比基准元素小的和大的元素存储到less和greater中
        if arr[i]<=pivot:
            less.append(arr[i])
        else:
            greater.append(arr[i])
    return QuickSort(less)+[pivot]+QuickSort(greater)    #递归进行排序
