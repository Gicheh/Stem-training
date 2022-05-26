str="Hello guys welcome back to my class"
for x in str:
    if x!="l":
         print(x)

str="Hello guys welcome back to my class"
outstr=""
for x in str:
    if x !='l'and x!='e'and x!='u':
        outstr += x
print(outstr)

#range
for i in range(1,10,2):
    print(i)
