"""1022 D进制的A+B (20 分)
输入两个非负 10 进制整数 A 和 B (≤2
​30
​​ −1)，输出 A+B 的 D (1<D≤10)进制数。

输入格式：
输入在一行中依次给出 3 个整数 A、B 和 D。

输出格式：
输出 A+B 的 D 进制数。

输入样例：
123 456 8
输出样例：
1103"""
inp=list(map(int,input().split()))
result_10=inp[0]+inp[1]
result_R=[]
while result_10!=0:
    result_R.insert(0,result_10%inp[2])
    result_10=result_10//inp[2]
result_R="".join(list(map(str,result_R)))
print(result_R if result_R!="" else "0")