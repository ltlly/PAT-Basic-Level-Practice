"""1019 数字黑洞 (20 分)
给定任一个各位数字不完全相同的 4 位正整数，如果我们先把 4 个数字按非递增排序，再按非递减排序，然后用第 1 个数字减第 2 个数字，将得到一个新的数字。一直重复这样做，我们很快会停在有“数字黑洞”之称的 6174，这个神奇的数字也叫 Kaprekar 常数。

例如，我们从6767开始，将得到

7766 - 6677 = 1089
9810 - 0189 = 9621
9621 - 1269 = 8352
8532 - 2358 = 6174
7641 - 1467 = 6174
... ...
现给定任意 4 位正整数，请编写程序演示到达黑洞的过程。

输入格式：
输入给出一个 (0,10
​4
​​ ) 区间内的正整数 N。

输出格式：
如果 N 的 4 位数字全相等，则在一行内输出 N - N = 0000；否则将计算的每一步在一行内输出，直到 6174 作为差出现，输出格式见样例。注意每个数字按 4 位数格式输出。

输入样例 1：
6767
输出样例 1：
7766 - 6677 = 1089
9810 - 0189 = 9621
9621 - 1269 = 8352
8532 - 2358 = 6174
输入样例 2：
2222
输出样例 2：
2222 - 2222 = 0000"""
def is_equal(num):
    num = str(num).zfill(4)
    i = num[0]
    if num.count(i) == 4:
        return True
    else:
        return False


def get_max(num):  # 指从左到右 为从大到小
    num = str(num).zfill(4)
    _ = sorted(list(map(int, list(num))), reverse=True)
    _ = list(map(str, _))
    return int("".join(_))


def get_min(num):  # 指从左到右 为从小到大
    num = str(num).zfill(4)
    _ = sorted(list(map(int, list(num))))
    _ = list(map(str, _))
    return int("".join(_))


if __name__ == '__main__':
    n = int(input())
    if is_equal(n):
        print(f"{n} - {n} = 0000")
    else:
        while get_max(n) - get_min(n) != 6174:
            print(f"{str(get_max(n)).zfill(4)} - {str(get_min(n)).zfill(4)} = {str(get_max(n) - get_min(n)).zfill(4)}")
            n = get_max(n) - get_min(n)
        print(f"{str(get_max(n)).zfill(4)} - {str(get_min(n)).zfill(4)} = {str(get_max(n) - get_min(n)).zfill(4)}")
