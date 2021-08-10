"""
1018 锤子剪刀布 (20 分)
大家应该都会玩“锤子剪刀布”的游戏：两人同时给出手势，胜负规则如图所示：

FigCJB.jpg

现给出两人的交锋记录，请统计双方的胜、平、负次数，并且给出双方分别出什么手势的胜算最大。

输入格式：
输入第 1 行给出正整数 N（≤10
​5
​​ ），即双方交锋的次数。随后 N 行，每行给出一次交锋的信息，即甲、乙双方同时给出的的手势。C 代表“锤子”、J 代表“剪刀”、B 代表“布”，第 1 个字母代表甲方，第 2 个代表乙方，中间有 1 个空格。

输出格式：
输出第 1、2 行分别给出甲、乙的胜、平、负次数，数字间以 1 个空格分隔。第 3 行给出两个字母，分别代表甲、乙获胜次数最多的手势，中间有 1 个空格。如果解不唯一，则输出按字母序最小的解。

输入样例：
10
C J
J B
C B
B B
B C
C C
C B
J B
B C
J J
输出样例：
5 3 2
2 3 5
B B
"""
#注意大数据超时问题 应该用count函数 少用自定义的计数器
#应该多互相定义 少用count 就少运行时间
n = int(input())
informs = [0] * n
for index in range(len(informs)):
    informs[index] = input()
a = [0] * 3
b = [0] * 3
a_win = ["C J", "J B", "B C"]
a_b = ["C C", "B B", "J J"]
b_win = ["J C", "B J", "C B"]

a_use = [0] * 3  # bcj
b_use = [0] * 3

use = ["B", "C", "J"]
a_use[0] = informs.count(a_win[2])
a_use[1] = informs.count(a_win[0])
a_use[2] = informs.count(a_win[1])

b_use[0] = informs.count(b_win[2])
b_use[1] = informs.count(b_win[0])
b_use[2] = informs.count(b_win[1])

a[0] = sum(a_use)
a[2] = sum(b_use)
a[1] = len(informs) - a[0] - a[2]

b = a[::-1]
print(" ".join(list(map(str, a))))
print(" ".join(list(map(str, b))))
print(use[a_use.index(max(a_use))], end=" ")
print(use[b_use.index(max(b_use))])
