#coding:utf-8
'''
BF算法
'''
def BF(input,target):
    location=[]
    target_length = len(target)
    input_length = len(input)
    for i in range(target_length-input_length+1):
        loc=i
        for j in range(input_length):
            if target[loc]==input[j]:
                loc=loc+1
            else:
                break
        if loc-i==input_length:
            location.append(loc)
    return location