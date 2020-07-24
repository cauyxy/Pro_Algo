def GetBC(pattern):
    # 预生成坏字符表
    BMBC = dict()
    for i in range(len(pattern) - 1):
        # 记录坏字符最右位置（不包括模式串最右侧字符）
        BMBC[pattern[i]] = i + 1
    return BMBC

def GetGS(pattern):
    # 预生成好后缀表
    BMGS = dict()

    # 无后缀仅根据坏字移位符规则
    BMGS[''] = 0

    for i in range(len(pattern)):

        # 好后缀
        GS = pattern[len(pattern) - i - 1:]

        for j in range(len(pattern) - i - 1):

            # 匹配部分
            NGS = pattern[j:j + i + 1]

            # 记录模式串中好后缀最靠右位置（除结尾处）
            if GS == NGS:
                BMGS[GS] = len(pattern) - j - i - 1
    return BMGS

def BM(input,target):
    """
    Boyer-Moore算法实现字符串查找
    """
    input_length = len(input)
    target_length = len(target)
    i = 0
    j = input_length
    loaction = []
    BMBC = GetBC(pattern=input)  # 坏字符表
    BMGS = GetGS(pattern=input)  # 好后缀表
    while i < target_length:
        while (j > 0):
            if i + j -1 >= target_length: # 当无法继续向下搜索就返回值
                return loaction

            # 主串判断匹配部分
            a = target[i + j - 1:i + input_length]

            # 模式串判断匹配部分
            b = input[j - 1:]

            # 当前位匹配成功则继续匹配
            if a == b:
                j = j - 1

            # 当前位匹配失败根据规则移位
            else:
                i = i + max(BMGS.setdefault(b[1:], input_length), j - BMBC.setdefault(target[i + j - 1], 0))
                j = input_length

            # 匹配成功返回匹配位置
            if j == 0:
                loaction.append(i)
                i += 1
                j = len(input)
