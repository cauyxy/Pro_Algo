# coding:utf-8
'''
BF算法
'''


def BF(input, target):
    location = []
    target_length = len(target)
    input_length = len(input)
    for i in range(target_length - input_length + 1):
        # 目标串移动循环
        loc = i
        for j in range(input_length):
            # 模式串与目标串部分匹配循环
            if target[loc] == input[j]:
                # 相等就继续下一个字符
                loc = loc + 1
            else:
                break
        if loc - i == input_length:
            # 全匹配完就返回匹配位置
            location.append(loc)
    return location
