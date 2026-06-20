print("Calculator")
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
operator=input("Enter the operation +,-,*,/:")
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operator."

print("Result:", result)
