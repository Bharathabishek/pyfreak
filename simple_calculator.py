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

number1 = int(input("Enter 1st number: "))
number2 = int(input("Enter 2nd number: "))

if select == "+":
    print("\n{} + {} =".format(number1,number2),add(number1,number2))

elif select == "-":
    print("\n{} - {} =".format(number1,number2),subract(number1,number2))

elif select == "*":
    print("\n{} - {} =".format(number1,number2),multiply(number1,number2))

elif select == "/":
    print("\n{} - {} =".format(number1,number2),divide(number1,number2))

else:
    print("Please provide one of these signs ('+', '-', '*', '/')")
