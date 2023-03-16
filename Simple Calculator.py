# This asks the user to enter the first number
num1 = float(input("Enter the first number: "))

# This asks the user to enter the second number
num2 = float(input("Enter the second number: "))

# Ask the user to choose an operation
print("Choose an operation (+, -, *, /)")
operator = input()

# Perform the chosen operation on the two numbers
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
else:
    print("ERROR!!! - Invalid operator")

# Display the result to the user
print("Result: ", result)
