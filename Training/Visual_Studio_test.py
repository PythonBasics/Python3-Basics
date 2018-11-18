try:
    number = int(input("Enter number: "))
    print (number)
except ZeroDivisionError:
    print("ZeroDivisionError")
except ValueError:
    print("invalid value")