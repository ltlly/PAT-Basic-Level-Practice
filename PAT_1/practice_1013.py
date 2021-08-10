"""1013 数素数 (20 分)
令 P
​i
​​  表示第 i 个素数。现任给两个正整数 M≤N≤10
​4
​​ ，请输出 P
​M
​​  到 P
​N
​​  的所有素数。

输入格式：
输入在一行中给出 M 和 N，其间以空格分隔。

输出格式：
输出从 P
​M
​​  到 P
​N
​​  的所有素数，每 10 个数字占 1 行，其间以空格分隔，但行末不得有多余空格。

输入样例：
5 27
输出样例：
11 13 17 19 23 29 31 37 41 43
47 53 59 61 67 71 73 79 83 89
97 101 103
"""


class Thired:
    def __init__(self):
        pass

    def biaoji(self, dic, N):
        for i in dic.copy():
            if dic[i] and self.is_sushu(i):
                for j in range(i, N + 1):
                    if i * j <= N:
                        dic[i * j] = False
                    elif i * j > N:
                        break

    def is_sushu(self, num):
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
                break
        else:
            return True

    def creat_dic(self, start, end, dic):
        for j in range(start, end + 1):
            dic[j] = True
        return dic

    def main(self, N, dic, sushus):
        self.biaoji(dic, N)
        for n in dic.copy():
            if not dic[n]:
                dic.pop(n)
        for sushu in dic:
            sushus.append(sushu)
        return (sushus)


if __name__ == '__main__':
    c = Thired()
    inp = list(map(int, input().split()))
    dic = {}
    sushus = []
    if inp[1] > 5000:
        N = 105000
    else:
        N = 500
    c.creat_dic(2, N, dic)
    couter = 0
    sushus = c.main(N, dic, sushus)
    while len(sushus) <= inp[1]:
        c.creat_dic(N, N + 500, dic)
        N = N + 500
        sushus = c.main(N, dic, sushus)
        sushus = list(set(sushus))
    sushus.sort()

    for result in sushus[inp[0] - 1:inp[1]]:
        couter = (couter + 1)
        if couter != 10 and result != sushus[inp[1] - 1]:
            print(result, end=" ")
            couter = couter % 10
        elif result == sushus[inp[1] - 1]:
            print(result)
        else:
            print(result, end="\n")
            couter = couter % 10
