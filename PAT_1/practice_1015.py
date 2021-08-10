import sys
import time
start=time.time()
score_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
              '10': 10, '11': 11, '12': 12, '13': 13, '14': 14, '15': 15, '16': 16, '17': 17,
              '18': 18, '19': 19, '20': 20, '21': 21, '22': 22, '23': 23, '24': 24, '25': 25,
              '26': 26, '27': 27, '28': 28, '29': 29, '30': 30, '31': 31, '32': 32, '33': 33,
              '34': 34, '35': 35, '36': 36, '37': 37, '38': 38, '39': 39, '40': 40, '41': 41,
              '42': 42, '43': 43, '44': 44, '45': 45, '46': 46, '47': 47, '48': 48, '49': 49,
              '50': 50, '51': 51, '52': 52, '53': 53, '54': 54, '55': 55, '56': 56, '57': 57,
              '58': 58, '59': 59, '60': 60, '61': 61, '62': 62, '63': 63, '64': 64, '65': 65,
              '66': 66, '67': 67, '68': 68, '69': 69, '70': 70, '71': 71, '72': 72, '73': 73,
              '74': 74, '75': 75, '76': 76, '77': 77, '78': 78, '79': 79, '80': 80, '81': 81,
              '82': 82, '83': 83, '84': 84, '85': 85, '86': 86, '87': 87, '88': 88, '89': 89,
              '90': 90, '91': 91, '92': 92, '93': 93, '94': 94, '95': 95, '96': 96, '97': 97,
              '98': 98, '99': 99, '100': 100}
a = list(map(int, sys.stdin.readline().split()))
total_inform = {}
total_inform["参考总人数"] = a[0]
total_inform["录取最低分"] = a[1]
total_inform["优先录取线"] = a[2]

many=int(total_inform["参考总人数"])
stu_inform = [0]*many
a = [0] * many
for i in range(0, total_inform["参考总人数"]):
    a[i] = sys.stdin.readline().split()
    a[i][1] = score_dict[a[i][1]]
    a[i][2] = score_dict[a[i][2]]
    stu_inform[i]=({"id": a[i][0], "德分": a[i][1], "才分": a[i][2]})
while 0 in stu_inform:
    stu_inform.remove(0)
# 去除两科都不及格者
for stu in stu_inform.copy():
    if stu["德分"] < total_inform["录取最低分"] or stu["才分"] < total_inform["录取最低分"]:
        stu_inform.remove(stu)
# 找出两科都优秀者
# first_stus:一类
first_stus = [0] * many
for stu in stu_inform.copy():
    if stu["德分"] >= total_inform["优先录取线"] and stu["才分"] >= total_inform["优先录取线"]:
        for index in range(0, len(first_stus)):
            if first_stus[index] == 0:
                first_stus[index] = stu
                break
        stu_inform.remove(stu)
while 0 in first_stus:
    first_stus.remove(0)
first_stus = sorted(first_stus, key=lambda i: (-i["德分"] - i["才分"], -i["德分"], i["id"]), )

# 找出二类:德分优秀 才分一般
second_stus = [0] * many
for stu in stu_inform.copy():
    if stu["德分"] >= total_inform["优先录取线"] and stu["才分"] < total_inform["优先录取线"]:
        for index in range(0, len(second_stus)):
            if second_stus[index] == 0:
                second_stus[index] = stu
                break
        stu_inform.remove(stu)
while 0 in second_stus:
    second_stus.remove(0)
second_stus = sorted(second_stus, key=lambda i: (-i["德分"] - i["才分"], -i["德分"], i["id"]), )

# 三类:德分>=才分
thired_stus = [0] * many
for stu in stu_inform.copy():
    if stu["德分"] >= stu["才分"]:
        for index in range(0, len(second_stus)):
            if thired_stus[index] == 0:
                thired_stus[index] = stu
                break
        stu_inform.remove(stu)
while 0 in thired_stus:
    thired_stus.remove(0)
thired_stus = sorted(thired_stus, key=lambda i: (-i["德分"] - i["才分"], -i["德分"], i["id"]), )
# 剩下的是四类
fourth_stus = stu_inform
fourth_stus = sorted(fourth_stus, key=lambda i: (-i["德分"] - i["才分"], -i["德分"], i["id"]), )
sorted_list = first_stus + second_stus + thired_stus + fourth_stus
sys.stdout.write(f"{len(sorted_list)}\n")
for stu in sorted_list:
    sys.stdout.write(f'{stu["id"]} {stu["德分"]} {stu["才分"]}\n')
# print((time.time()-start)*1000)