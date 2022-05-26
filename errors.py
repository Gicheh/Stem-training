try :
    Div=10/0
    value=int(input("enter a number :"))
    print(value)
except ValueError:
    print("Invalid number entered")
except ZeroDivisionError:
    print("Divided by zero")