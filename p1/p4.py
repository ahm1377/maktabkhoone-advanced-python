inp=int(input())
list_asami=list()
sort_list_asami=list()
for _ in range(0,inp):
    temp=[]
    temp=input().split('.')
    list_asami.append(temp)

for i in list_asami:
    temp=str()
    temp=i[1]
    temp=temp[:1].upper()+temp[1:].lower()
    i[1]=temp

sort_list_asami=sorted(list_asami , key=lambda x:(x[0],x[1]))

for outp in sort_list_asami:
    print(f"{outp[0]} {outp[1]} {outp[2]}")