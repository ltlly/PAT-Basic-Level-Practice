"""
1012 数字分类 (20 分)
给定一系列正整数，请按要求对数字进行分类，并输出以下 5 个数字：

A
​1
​​  = 能被 5 整除的数字中所有偶数的和；
A
​2
​​  = 将被 5 除后余 1 的数字按给出顺序进行交错求和，即计算 n
​1
​​ −n
​2
​​ +n
​3
​​ −n
​4
​​ ⋯；
A
​3
​​  = 被 5 除后余 2 的数字的个数；
A
​4
​​  = 被 5 除后余 3 的数字的平均数，精确到小数点后 1 位；
A
​5
​​  = 被 5 除后余 4 的数字中最大数字。
输入格式：
每个输入包含 1 个测试用例。每个测试用例先给出一个不超过 1000 的正整数 N，随后给出 N 个不超过 1000 的待分类的正整数。数字间以空格分隔。

输出格式：
对给定的 N 个正整数，按题目要求计算 A
​1
​​ ~A
​5
​​  并在一行中顺序输出。数字间以空格分隔，但行末不得有多余空格。

若其中某一类数字不存在，则在相应位置输出 N。

输入样例 1：
13 1 2 3 4 5 6 7 8 9 10 20 16 18
输出样例 1：
30 11 2 9.7 9
输入样例 2：
8 1 2 4 5 6 7 9 16
输出样例 2：
N 11 2 N 9
"""
data = list(map(int, input().split()))
B1 = []
B2 = []
B3 = []
B4 = []
B5 = []
result = []
for index in range(1, len(data)):
    if data[index] % 5 == 0:
        B1.append(data[index])
    elif data[index] % 5 == 1:
        B2.append(data[index])
    elif data[index] % 5 == 2:
        B3.append(data[index])
    elif data[index] % 5 == 3:
        B4.append(data[index])
    elif data[index] % 5 == 4:
        B5.append(data[index])
a1 = 0
if B1:

    for x in B1:
        if x % 2 == 0:
            a1 += x
    if a1 == 0:
        a1 = "N"
else:
    a1 = "N"

a2 = 0
if B2:
    for index in range(0, len(B2), 2):
        a2 = a2 + B2[index]
    if len(B2) >= 1:
        for index in range(1, len(B2), 2):
            a2 = a2 - B2[index]
else:
    a2 = "N"


if B3:
    a3 = len(B3)
else:
    a3 = "N"



if B4:
    a4 = round(sum(B4) / len(B4), 1)
else:
    a4 = "N"


if B5:
    a5 = max(B5)
else:
    a5 = "N"

result.append(a1)
result.append(a2)
result.append(a3)
result.append(a4)
result.append(a5)
result = " ".join(list(map(str, result)))
print(result)
