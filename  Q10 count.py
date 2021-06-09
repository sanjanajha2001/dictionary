d={"Alex":["subj1","subj2","subj3"],"David":["subj1","subj2"]}
c=0
for x in d:
    if d[x]:
        c=c+len(d[x])
print(c)

