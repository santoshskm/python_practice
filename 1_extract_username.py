email=input("Enter your email id:")
li=list(email)
index_num=li.index("@")
print("Username:")
for i in range(0,index_num):
    if(li[i].isalpha()):
        print(str(li[i]),end="")

