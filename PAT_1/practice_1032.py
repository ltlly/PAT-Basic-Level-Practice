"""
1032 挖掘机技术哪家强 (20 分)
为了用事实说明挖掘机技术到底哪家强，PAT 组织了一场挖掘机技能大赛。现请你根据比赛结果统计出技术最强的那个学校。

输入格式：
输入在第 1 行给出不超过 10
5
  的正整数 N，即参赛人数。随后 N 行，每行给出一位参赛者的信息和成绩，包括其所代表的学校的编号（从 1 开始连续编号）、及其比赛成绩（百分制），中间以空格分隔。

输出格式：
在一行中给出总得分最高的学校的编号、及其总分，中间以空格分隔。题目保证答案唯一，没有并列。

输入样例：
6
3 65
2 80
1 100
2 70
3 40
3 0
输出样例：
2 150
鸣谢用户 米泰亚德 补充数据！
"""


import sys
#使用sys.stdin.readline()代替input()
manypeople=int(input())
#用数组下标表示学校编码,用一位数组代替字典或者二维数组 使查找操作耗时少
scores=[0]*(manypeople+1)
for index in range(1,manypeople+1):
    inp=list(map(int,sys.stdin.readline().split()))
    scores[inp[0]]+=inp[1]
tem=max(scores)
if tem==0:
    print("1 0")
else:
    print(scores.index(tem),tem)
