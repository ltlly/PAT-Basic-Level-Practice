
"""
1030 完美数列 (25 分)
给定一个正整数数列，和正整数 p，设这个数列中的最大值是 M，最小值是 m，如果 M≤mp，则称这个数列是完美数列。

现在给定参数 p 和一些正整数，请你从中选择尽可能多的数构成一个完美数列。

输入格式：
输入第一行给出两个正整数 N 和 p，其中 N（≤10
5
 ）是输入的正整数的个数，p（≤10
9
 ）是给定的参数。第二行给出 N 个正整数，每个数不超过 10
9
 。

输出格式：
在一行中输出最多可以选择多少个数可以用它们组成一个完美数列。

输入样例：
10 8
2 3 20 4 5 1 6 7 8 9
结尾无空行
输出样例：
8
结尾无空行
"""
import sys
# sys.stdin.readline()和input()作用一样 但是快点
lennum, p = list(map(int, sys.stdin.readline().split()))

ori_num = sorted(list(map(int, sys.stdin.readline().split())))
maxlen = 0
for index in range(0, lennum):
    if index + maxlen > lennum:
        # 这时候即使后面全要 也不可能超过之前的maxlen了
        break
    counter = maxlen
    #从index+maxlen开始遍历 比如说 现在的maxlen是3 我要假设下一组的maxlen是4 如果不可行就直接跳过 (因为你判断出来下一组maxlen是1or2or3对结果也没影响
    for l in range(index+maxlen, lennum):
        if ori_num[l] > p * ori_num[index]:
            break
        counter += 1
    if counter > maxlen:
        maxlen = counter
print(maxlen)
