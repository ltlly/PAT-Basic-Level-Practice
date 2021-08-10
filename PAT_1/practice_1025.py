"""
00100 6 4
00000 4 99999
00100 1 12309
68237 6 -1
33218 3 00000
99999 5 68237
12309 2 33218
"""
import pprint
def main():
    a=input().split()
    startadd,howlong,reversnum=a
    ori_data=[0]*int(howlong)
    dic={}
    for index in range(len(ori_data)):
        ori_data[index]=input().split()
        dic[ori_data[index][0]]=ori_data[index][1:]#创建一个字典 建为地址 值为值和下一个地址
    line_data=[]
    line_data.append([[startadd]+dic[startadd]])
    pprint.pprint(line_data)
    pprint.pprint(dic)


def revers(line_data,sta,cell):
    # line_data[1:4] = line_data[3:0:-1]  # 将第二个与第三个翻转了 即1 与 2 index
    if sta==0:
        line_data[0:0+cell]=line_data[cell-1::-1]
    else:
        line_data[sta:sta+cell]=line_data[sta+cell-1:sta-1:-1]
if __name__ == '__main__':
    main()
