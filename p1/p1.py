def primenumber(checkprime):
    count=0
    prime=bool()
    for i in range(1,checkprime+1):
        if checkprime%i==0:
            count+=1
        i+=1
    if count>2:
        prime=False
    elif count==2:
        prime=True
    return prime

inplist=list()
max_maqsom=int()
list_maqsom=list()
prime_maqsom=list()
count_maqsom=int()
maqsom_dict=dict()
#input number
for add in range(0,10):
    inplist.append(int(input()))
#find prime maqsom
for num in inplist:
    prime_maqsom=[]
    for maqsom in range(1,num+1):
        if num%maqsom==0:
            if primenumber(maqsom):
                prime_maqsom.append(maqsom)
    list_maqsom.append([num,len(prime_maqsom)])
#find bigger number
for x,y in list_maqsom:
    if y>count_maqsom:
        count_maqsom=y
        max_maqsom=x
    elif y==count_maqsom:
        if x>max_maqsom:
            max_maqsom=x        

#output
print(max_maqsom,count_maqsom)