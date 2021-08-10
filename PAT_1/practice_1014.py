"""
1014 福尔摩斯的约会 (20 分)
大侦探福尔摩斯接到一张奇怪的字条：我们约会吧！ 3485djDkxh4hhGE 2984akDfkkkkggEdsb s&hgsfdk d&Hyscvnm。大侦探很快就明白了，字条上奇怪的乱码实际上就是约会的时间星期四 14:04，因为前面两字符串中第 1 对相同的大写英文字母（大小写有区分）是第 4 个字母 D，代表星期四；第 2 对相同的字符是 E ，那是第 5 个英文字母，代表一天里的第 14 个钟头（于是一天的 0 点到 23 点由数字 0 到 9、以及大写字母 A 到 N 表示）；后面两字符串第 1 对相同的英文字母 s 出现在第 4 个位置（从 0 开始计数）上，代表第 4 分钟。现给定两对字符串，请帮助福尔摩斯解码得到约会的时间。

输入格式：
输入在 4 行中分别给出 4 个非空、不包含空格、且长度不超过 60 的字符串。

输出格式：
在一行中输出约会的时间，格式为 DAY HH:MM，其中 DAY 是某星期的 3 字符缩写，即 MON 表示星期一，TUE 表示星期二，WED 表示星期三，THU 表示星期四，FRI 表示星期五，SAT 表示星期六，SUN 表示星期日。题目输入保证每个测试存在唯一解。

输入样例：
3485djDkxh4hhGE
2984akDfkkkkggEdsb
s&hgsfdk
d&Hyscvnm
输出样例：
THU 14:04
"""


def get_data():
    password = [0] * 4
    result_01 = []
    A_G = ["A", "B", "C", "D", "E", "F", "G"]
    A_N09 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "0", "1", "2", "3", "4", "5", "6",
             "7", "8", "9"]
    for index in range(0, 4):
        password[index] = input().strip()
    for index in range(0, len(password[0])):
        if password[0][index] == password[1][index]:
            # 第一对相同大写字母A-G(65-71)
            if password[0][index] in A_G and not result_01:
                result_01.append(password[0][index])
                continue
            # 第二对相同字符 0-9(48-57) A-N(65-78)
            if result_01 and password[0][index] in A_N09:
                result_01.append(password[0][index])
                break

    for index in range(0, len(password[2])):
        if password[2][index] == password[3][index] and str(password[2][index]).isalpha():
            result_01.append(index)
            break
    return result_01


def treat_data(result_01):
    # 星期部分
    week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    result_01[0] = week[int(ord(result_01[0])) - 65]
    # 小时部分
    try:
        result_01[1] = int(result_01[1])
    except(ValueError):
        result_01[1] = int(ord(result_01[1])) - 55
    return result_01


if __name__ == '__main__':
    result = treat_data(get_data())
    result[1] = str(result[1]).zfill(2)
    result[2] = str(result[2]).zfill(2)
    print(f"{result[0]} {result[1]}:{result[2]}")
