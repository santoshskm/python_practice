list1=['aa','abc','xyz','123','aba','121','131','12221']
count=0
length1=len(list1)
for i in range(0,length1):
    if list1[i][0]==list1[i][-1]:
        print(list1[i],end=" ")
        count=count+1
print()
print(count)