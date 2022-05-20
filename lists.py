#lists
words=["apples","love","people","!"]
print(words[0])
print(words[1])
print(words[3])

#lists can store any data type
numbers=[5,6,7,8]
print(numbers[2])
dat=['a',1,"foo",6,7,"Hey!"]
print(dat)

#nested lists
m=[
[5,7,8],
[3,2,1]]
print(m[1][2])
print(m)
#strings can also be indexed as lists
str= "Hello class"
print(str[5])
print(str[6])
print(str[7-3])

strg= ["Hello","class","123","51","abc","Hey",'b','a']
print(strg)
print(strg[5])
print(strg[6])
print(strg[7-3])
strg[0]=strg[7-2]
print(strg)
#strings cannot be readdressed
Subjects=["maths","scince","religious"]
Subjects[2]="mechanics"
print(Subjects)

