inp=int(input())
word_dict=dict()
for i in range(0,inp):
    temp=input().split()
    word_dict[temp[0]]=[temp[1],temp[2],temp[3]]
    temp=''
text_inp=input().strip('.,').split()
text_translate=str()
for word in text_inp:
    count=0
    for key , values in word_dict.items(): 
        count+=1
        if word in values:
            text_translate=text_translate + key + ' '
            break
        elif count>(inp-1):
            text_translate=text_translate + word + ' '
print(f"{text_translate}")