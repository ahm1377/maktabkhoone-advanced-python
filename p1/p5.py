word_list=list()
words=list()
count=2
text=input().split('.')
for part_text in text:
   words=part_text.split()[1:]
   for word in words:
       if word[0].strip(',').isupper():
           word_list.append([word , count])
       count+=1
   count+=1
if word_list==[]:
    print('None')
else:
    for i in range(len(word_list)):
        print(f"{word_list[i][1]}:{word_list[i][0]}")