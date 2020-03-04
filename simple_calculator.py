def add(num1,num2):
    return num1 + num2

def subract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1 / num2

print("Please select an operation: \n" \
            "1.Add(+)\n" \
            "2.Subract(-)\n" \
            "3.Multipy(*)\n" \
            "4.Divide(/)\n")

# User input to deside the opertion
select = (input("Select an operation '+', '-', '*', '/' : "))

# User input to ask for numbers
number1 = int(input("Enter 1st number: "))
number2 = int(input("Enter 2nd number: "))

# Statements to decide the opertion based on user input
if select == "+":
    print("\n{} + {} =".format(number1,number2),add(number1,number2))

elif select == "-":
    print("\n{} - {} =".format(number1,number2),subract(number1,number2))

elif select == "*":
    print("\n{} * {} =".format(number1,number2),multiply(number1,number2))

elif select == "/":
    if number2 > 0:
        print("\n{} / {} =".format(number1,number2),divide(number1,number2))
    else:
        print("\nCan't divide anthing by zero")

else:
    print("Please provide one of these signs ('+', '-', '*', '/')")
