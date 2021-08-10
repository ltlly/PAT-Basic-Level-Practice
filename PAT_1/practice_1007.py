"""
1007 素数对猜想 (20 分)
让我们定义d
​n
​​ 为：d
​n
​​ =p
​n+1
​​ −p
​n
​​ ，其中p
​i
​​ 是第i个素数。显然有d
​1
​​ =1，且对于n>1有d
​n
​​ 是偶数。“素数对猜想”认为“存在无穷多对相邻且差为2的素数”。

现给定任意正整数N(<10
​5
​​ )，请计算不超过N的满足猜想的素数对的个数。

输入格式:
输入在一行给出正整数N。

输出格式:
在一行中输出不超过N的满足猜想的素数对的个数。

输入样例:
20
输出样例:
4
"""


class First1:
    def __init__(self):
        pass

    def is_sushu(self, num, dic):
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                break
        else:
            dic[num] = True

    def creat_dic(self, num, dic):
        for j in range(2, num + 1):
            dic[j] = False
        return dic

    def main(self):
        N = int(input())
        dic = {}
        result = 0
        self.creat_dic(N, dic)
        for num in range(3, N + 1, 2):
            self.is_sushu(num, dic)
        for num in range(3, N + 1, 2):
            if dic[num] and num + 2 <= N:
                if dic[num + 2]:
                    result += 1
        print(result)


class second:
    def main(self):
        sushus = [2, 3]
        N = int(input())
        result = 0
        for num in range(5, N + 1, 2):
            self.is_sushu(num, sushus)
        for sushu in sushus:
            if sushu + 2 in sushus:
                result += 1
        print(result)

    def is_sushu(self, num, sushus):
        for sushu in sushus:
            if num % sushu == 0:
                break
            elif sushu >= num ** 0.5 + 1:
                sushus.append(num)
                break
        else:
            sushus.append(num)


class Thired:
    def __init__(self):
        pass

    def biaoji(self, dic, N):
        for i in dic.copy():
            if dic[i] and self.is_sushu(i):
                for j in range(i, N + 1):
                    if i * j <= N :
                        dic[i * j] = False
                    elif i*j>N:
                        break

    def is_sushu(self, num):
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
                break
        else:
            return True

    def creat_dic(self, num, dic):
        for j in range(2, num + 1):
            dic[j] = True
        return dic

    def main(self):
        N = int(input())
        dic = {}
        result = 0
        self.creat_dic(N, dic)
        self.biaoji(dic, N)
        for n in dic:
            if dic[n] and n + 2 <= N and dic[n + 2]:
                result += 1
        print(result)


if __name__ == '__main__':
    # a=First1()
    # a.main()
    # b=second()
    # b.main()
    c = Thired()
    c.main()
# 方法一使用字典标记素数 并通过查字典验证素数对数 运行时间171ms
# 方法二将素数加入列表 用数字取余素数判断是否为素数 运行时间>200ms
