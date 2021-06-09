# i=0
# dic1={}
# while i<3:
#     key=input("enter the key")
#     value=input("enter the key")
#     i=i+1
#     d={key:value}
#     dic1.update(d)
# print(dic1)



a={}
b=int(input("how much input ???"))
for i in range(b):
    s=input("enter the key")
    j=input("enter the values")
    a.update({s:j})
print(a)


