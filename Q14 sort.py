my_dict={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
dict={}
for i in my_dict:
    print("key - ",i,":","value - ",my_dict[i])
    s=my_dict[i]
    for j in my_dict:
        a=my_dict[j]
        if s>a:
            dict[j]=a
print(dict)