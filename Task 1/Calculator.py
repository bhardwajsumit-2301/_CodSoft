first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

print("\nChoose an operation:")
print("+ for Addition")
print("- for Subtraction")
print("* for Multiplication")
print("/ for Division")

operation = input("Enter your choice (+, -, *, /): ")

if operation == '+':
    result = first_number + second_number
    print(f"\nResult: {first_number} + {second_number} = {result}")
elif operation == '-':
    result = first_number - second_number
    print(f"\nResult: {first_number} - {second_number} = {result}")
elif operation == '*':
    result = first_number * second_number
    print(f"\nResult: {first_number} * {second_number} = {result}")
elif operation == '/':

    if second_number != 0:
        result = first_number / second_number
        print(f"\nResult: {first_number} / {second_number} = {result}")
    else:
        print("\nError: Cannot divide by zero!")
else:
    print("\nInvalid operation. Please choose +, -, *, or /.")


print("\nThank you for using the calculator!")
