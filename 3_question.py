list1=[1,13,7,5,9]
length=len(list1)
for i in list1:
    for j in list1:
        if(i!=j):
            if (i+j)==14:
             print(list1.index(i)," ",list1.index(j))

