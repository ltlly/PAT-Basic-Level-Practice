import math
import random
"""1010 一元多项式求导 (25 分)
设计函数求一元多项式的导数。（注：x
​n
​​ （n为整数）的一阶导数为nx
​n−1
​​ 。）

输入格式:
以指数递降方式输入多项式非零项系数和指数（绝对值均为不超过 1000 的整数）。数字间以空格分隔。

输出格式:
以与输入相同的格式输出导数多项式非零项的系数和指数。数字间以空格分隔，但结尾不能有多余空格。注意“零多项式”的指数和系数都是 0，但是表示为 0 0。

输入样例:
3 4 -5 2 6 1 -2 0
输出样例:
12 3 -10 1 6 0"""

def my(nums):
    nums = input().split()
    # nums =list(map(int, input().split()))
    results = []
    for index in range(0, len(nums), 2):
        xishu = int(nums[index]) * int(nums[index + 1])
        zhishu = int(nums[index + 1]) - 1
        if zhishu == -1:
            continue
        results.append(xishu)
        results.append(zhishu)
    if results:
        for index in range(0, len(results)):
            results[index] = str(results[index])
        return (" ".join(results).strip())

    else:
        return ("0 0")


def other(num_lst):
    # num=input().split()
    num_lst = num_lst.split(" ")
    n = len(num_lst)
    out_lst = []

    for i in range(0, n, 2):
        xishu = int(num_lst[i])
        zhishu = int(num_lst[i + 1])
        if zhishu == 0:
            continue
        out_lst.append(str(xishu * zhishu))
        out_lst.append(str(zhishu - 1))

    out_str = " ".join(out_lst)
    if out_str:
        return (out_str.strip())

    else:
        return ("0 0")


def test():
    # num=f"{random.randint(0,100)} {random.randint(0,100)} {random.randint(0,100)} {random.randint(0,100)}"
    num = "6 0 6 0"
    if my(num) == other(num):
        print(my(num))
    elif my(num) != other(num):
        print("输入的数组是", num)
        print("我的结果是", my(num))
        print("正确的结果是", other(num))
        print("*****************")


if __name__ == '__main__':
    # for n in range(0, 100):
    #     test()
    test()
    print("完成")
#split()是将多个空格作为一个