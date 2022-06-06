while (1):
    try:
        x=int(input('Enter first no:'))
        y=int(input('Enter second number:'))
        z=x/y
    except ZeroDivisionError:
        print("Cannot divide by 0!")
    except ValueError:
        print("Invalid input!")
        continue
    else:
        print(z)
        break
    finally:
        print('This program ends here')
        