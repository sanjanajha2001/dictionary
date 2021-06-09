list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,] 
i=0
dic1={}
while i<len(list1):
    dic2={list1[i]:list2[i]}
    dic1.update(dic2)
    i=i+1
print(dic1) 


# c={}
# for i in range(len[list1]):
#     c[list1[n]]=list2[n]
# print(c)