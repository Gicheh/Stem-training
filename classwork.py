# def print_nums (n):
#     for num in range (n):
#         if num %3==0 and num %5 !=0:
#             print("foo")
#         if num %5==0 and num %3 !=0:
#             print("bar")
#         if num %3==0 and num %5==0:
#             print("foobar")
#         if num %3!=0 and num %5 !=0:
#             print (num)
# print_nums (10)

        
# def greater_than (n):
#     for num in range (n):
#         if num > 10:
#             print ("Greater than 10")
            
# greater_than(12)

def greater_than (a,b):
    for num in range (b):
        if num > a:
            print("Greater than",a)
        elif num ==a:
            print("Equal to",a)
        else:
            print("less than",a)

greater_than(6,10)    
        