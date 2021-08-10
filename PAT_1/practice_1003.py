"""得到“答案正确”的条件是：

字符串中必须仅有 P、 A、 T这三种字符，不可以包含其它字符；
任意形如 xPATx 的字符串都可以获得“答案正确”，其中 x 或者是空字符串，或者是仅由字母 A 组成的字符串；
如果 aPbTc 是正确的，那么 aPbATca 也是正确的，其中 a、 b、 c 均或者是空字符串，或者是仅由字母 A 组成的字符串。
现在就请你为 PAT 写一个自动裁判程序，判定哪些字符串是可以获得“答案正确”的。

输入格式：
每个测试输入包含 1 个测试用例。第 1 行给出一个正整数 n (<10)，是需要检测的字符串个数。接下来每个字符串占一行，字符串长度不超过 100，且不包含空格。

输出格式：
每个字符串的检测结果占一行，如果该字符串可以获得“答案正确”，则输出 YES，否则输出 NO。

输入样例：
9
PAT
PAAT
AAPATAA
AAPAATAAAA
xPATx
PT
Whatever
APAAATAA
APT
输出样例：
YES
YES
YES
YES
NO
NO
NO
NO
NO"""
strs_len = int(input())
strs = {}
for index in range(0, strs_len):
    strs[input()] = "NO"
for string in strs.keys():
    counter_left = 0
    counter_middle = 0
    counter_right = 0
    counter_P = 0
    counter_T = 0
    test = True
    for character in string:
        if character != "P" and character != "A" and character != "T":
            test = False
            break
        if character == "P":
            counter_P += 1
        elif character == "T":
            counter_T += 1
        if (counter_P == 0 or 1) and (counter_T == 0 or 1):
            if counter_P == 0 and character == "A":
                counter_left += 1
            elif counter_P == 1 and counter_T == 0 and character == "A":
                counter_middle += 1
            elif counter_P == 1 and counter_T == 1 and character == "A":
                counter_right += 1
    else:
        if counter_left * counter_middle == counter_right and counter_middle != 0 and test:
            strs[string] = "YES"
for answar in strs.values():
    print(answar)
