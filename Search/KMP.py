#coding:utf-8
from CutWord import CutWord
'''
KMP算法
'''
def GetNext(str):
    n = len(str)
    next = [0, 0]
    j = 0
    for i in range(1, n):
        while j > 0 and str[i] != str[j]:
            j = next[j]
        if str[i] == str[j]:
            j += 1
        next.append(j)
    return next

def KMP(input, target):
    target_length = len(target)
    input_length = len(input)
    next = GetNext(input)
    location = []
    j = 0
    for i in range(target_length):
        while target[i] != input[j] and j > 0:
            j = next[j]

        if target[i] == input[j]:
            j += 1
            if j == input_length:
                location.append(i-input_length+1)
                j = next[j]
    return location
