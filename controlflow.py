#If statements
x=0
if x<=1:
    print("Hey, I am still here")
    x-=1
print("Done")
#Else statement
x=10
if x==10:
    print(x)
else:
    print("Not 10")
#elif to create grading system
grade=int(input("Write student score :"))
if grade >=80 and grade<101:
    print(" Student scored an A")
elif grade >=70 and grade <80:
    print("STudent scored a B")
elif grade >=60 and grade<70:
    print("Student scored a C")
elif grade >=50 and grade<60:
    print("Student scored a C")
elif grade >=40 and grade <50:
    print("Student scored a D")
elif grade >=30 and grade <40:
    print("Student scored an E")
elif grade 