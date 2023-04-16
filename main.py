value = 10/0
try:
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print("err")
except ValueError:
    print("Invalid Input")