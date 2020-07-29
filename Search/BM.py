# coding:utf-8
'''
BM算法
'''


def GetBC(pattern):
    # 坏字符字典
    BCDict = dict()
    for i in range(len(pattern) - 1):
        # 用字典记录坏字符位置
        BCDict[pattern[i]] = i + 1
    return BCDict


def GetGS(pattern):
    # 好后缀字典
    GSDict = dict()

    # 没有好后缀则不执行长距离滑动
    GSDict[''] = 0

    for i in range(len(pattern)):
        # 本质上在进行自身与自身的匹配寻找好后缀

        # 从右向左寻找好后缀
        GS = pattern[len(pattern) - i - 1:]

        for j in range(len(pattern) - i - 1):

            # 进行好后缀匹配寻找
            FindGS = pattern[j:j + i + 1]

            # 记录好后缀最靠右位置
            if GS == FindGS:
                GSDict[GS] = len(pattern) - j - i - 1
    return GSDict


def BM(input, target):
    input_length = len(input)
    target_length = len(target)
    i = 0
    j = input_length
    loaction = []
    BMBC = GetBC(pattern=input)  # 坏字符
    BMGS = GetGS(pattern=input)  # 好后缀
    while i < target_length:
        while (j > 0):
            if i + j - 1 >= target_length:  # 搜索完成返回结果位置
                return loaction

            # 目标串匹配
            target_match = target[i + j - 1:i + input_length]

            # 模式串匹配
            input_match = input[j - 1:]

            # 该字符匹配成功就继续
            if target_match == input_match:
                j = j - 1

            # 匹配失败就滑动
            else:
                # 寻找两个算法的滑动最大值
                i = i + max(BMGS.setdefault(input_match[1:], input_length), j - BMBC.setdefault(target[i + j - 1], 0))
                j = input_length

            # 匹配成功
            if j == 0:
                loaction.append(i)
                i += 1
                j = len(input)
    return loaction
