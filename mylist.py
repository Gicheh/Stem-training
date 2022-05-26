my_list=[2,3,4,5,6,7,10,8]
for x in my_list :
    print(x)
other_list=[]
for x in my_list:
    other_list.append(x)
    print(other_list)

my_list=[2,3,4,5,6,7,10,8]
other_list=[x for x in my_list]
print(other_list)

my_list=[2,3,4,5,6,7]
if x %2==0:
    other_list.append(x)
print(other_list)

my_list=[2,3,4,5,6,7,10,8]
other_list=[x for x in my_list if x %2==0]
print(other_list)
