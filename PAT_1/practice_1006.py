"""
1006 换个格式输出整数 (15 分)
让我们用字母 B 来表示“百”、字母 S 表示“十”，用 12...n 来表示不为零的个位数字 n（<10），换个格式来输出任一个不超过 3 位的正整数。例如 234 应该被输出为 BBSSS1234，因为它有 2 个“百”、3 个“十”、以及个位的 4。

输入格式：
每个测试输入包含 1 个测试用例，给出正整数 n（<1000）。

输出格式：
每个测试用例的输出占一行，用规定的格式输出 n。

输入样例 1：
234
输出样例 1：
BBSSS1234
输入样例 2：
23
输出样例 2：
SS123
"""
def get():
    num_str = input()
    result=""
    if len(num_str) == 3:
        result = "B" * int(num_str[0]) + "S" * int(num_str[1])
    elif len(num_str) == 2:
        result = "S" * int(num_str[0])
    for i in range(1, int(num_str[-1]) + 1):
        result = result + str(i)
    return result
if __name__ == '__main__':
    print(get())
    exit(0)

#注意个位数!