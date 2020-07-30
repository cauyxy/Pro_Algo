# coding:utf-8

'''
Levenshtein算法
动态规划实现
'''


def Levenshtein(input, target):
    # 构建dp二维表
    input_length = len(input)
    target_length = len(target)
    dp = [[0] * (target_length + 1) for _ in range(input_length + 1)]
    # 二维表初始化
    # 第一列
    for i in range(1, input_length + 1):
        dp[i][0] = dp[i - 1][0] + 1
    # 第一行
    for j in range(1, target_length + 1):
        dp[0][j] = dp[0][j - 1] + 1

    for i in range(1, input_length + 1):
        for j in range(1, target_length + 1):
            if input[i - 1] == target[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
    # 返回编辑距离
    return dp[-1][-1]
