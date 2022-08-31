from datetime import datetime
import time

N, M = map(int,input().split())

# date_string = '00:00:00'
# start_time = datetime.strptime(date_string, '%H:%M:%S')
# date_string = '16:10:00'
answer=0
cafe = []
cafe_sum = 0
# if start_time <out_time:
#     print(out_time)
input_list=[]
p=[]
for i in range(M):
    x = input().split()
    start_time = datetime.strptime(x[0], '%H:%M:%S')
    out_time = datetime.strptime(x[1], '%H:%M:%S')
    input_list.append([start_time,out_time])
    p.append(start_time)
input_list2=[]
list1 = sorted(range(len(p)), key=p.__getitem__)

for i in list1:
    input_list2.append(input_list[i])


for i in range(M):
    x=input_list2[i]
    if cafe_sum<N:
        cafe_sum+=1
        cafe.append(x[1])
        answer+=1
    else:
        cafe_min = datetime.strptime('23:59:59', '%H:%M:%S')
        k = -1
        for j in range(N):
            if cafe_min>cafe[j]:
                cafe_min = cafe[j]
                k=j
        start_time = x[0]
        if k!=-1:
            if start_time>cafe_min:
                cafe[k]=x[1]
                answer+=1
print(answer)
