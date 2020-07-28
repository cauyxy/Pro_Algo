#coding:utf-8
'''
KMP算法
'''
def GetNext(input):
    #得到next数组
    n = len(input)
    next = [0, 0]
    j = 0
    for i in range(1, n):
        while j > 0 and input[i] != input[j]:
            #如果前后缀遇见不等就更新next，该长度为最长前后缀
            j = next[j]
        if input[i] == input[j]:
            #如果相等则继续累加
            j += 1
        next.append(j)
    return next

def KMP(input, target):
    #KMP算法实现
    target_length = len(target)
    input_length = len(input)
    next = GetNext(input)
    location = []
    j = 0
    for i in range(target_length):
        #如果不相等就向后滑动
        while target[i] != input[j] and j > 0:
            j = next[j]
        #如果相等就继续向后判断
        if target[i] == input[j]:
            j += 1
            #如果完全相等就记录位置
            if j == input_length:
                location.append(i-input_length+1)
                j = next[j]
    return location
