# for loops in python

mangoes="books"
for i in mangoes:
    print("taken one")
print("done")

#for loops with lists
words=["I","did","A"]
for word in words:
    print(word+"I")
names=["June","Jake"]
for name in names:
    print("Hi "+name)

str="Hello guys welcome back to my class"
count=0
for x in str:
    if(x=='l'):
        count+=1
print("The number of 0's is :",count)

str="Hello guys welcome back to my class"
for x in str:
    if(x=='l'):
        continue
    else:
        print(x)
        count+=1
print("The number of 0's is :",count)
    
