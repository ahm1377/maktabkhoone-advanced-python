count=int(input())
likes=list()
janre_dict={'Horror':0, 'Romance':0, 'Comedy':0, 'History':0 , 'Adventure':0 , 'Action':0}
for _ in range(0,count):
    peapel_like=[]
    peapel_like=input().split()
    likes.append(peapel_like)
for _ in likes:
    for i in range(1,4):
        if _[i] in janre_dict:
            janre_dict[_[i]]+=1

out_list=sorted(janre_dict.items() , key=lambda x:(-x[1],x[0]))

for this_one in out_list:
    print(this_one[0],' : ',this_one[1])
