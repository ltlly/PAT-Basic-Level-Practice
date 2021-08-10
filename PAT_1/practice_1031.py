import sys
weight = [7, 9, 10, 5, 8,4,2,1,6,3,7,9,10,5,8,4,2]
M=["1","0","X","9","8","7","6","5","4","3","2"]
many=int(sys.stdin.readline())
result=[]
for i in range(0,many):
    try:
        input_id=sys.stdin.readline()
        tem_id=[list(map(int,input_id[0:17])),input_id[17]]
        last=0
        for index in range(0,17):
            last=last+tem_id[0][index]*weight[index]
        last=last%11
        if M[last]==tem_id[1]:
            continue
        else:
            raise ValueError
    except(ValueError):
        result.append(input_id.rstrip())
if result:
    for x in result:
        print(x)
else:
    print("All passed")