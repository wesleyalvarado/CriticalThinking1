# Get user input for the first number
num1 = float(input("Please enter a number: "))

# Get user input for the second number
num2 = float(input("Please enter a second number: "))

# Calculate the multiplication
multiplication_result = num1 * num2

# Check if num2 is not equal to 0 to avoid division by zero
if num2 != 0:
    division_result = num1 / num2
    print(f"Division result: {num1} / {num2} = {division_result}")
else:
    print("Error: Division by zero is undefined. Please enter a non-zero second number.")

# Display the multiplication result
print(f"Multiplication result: {num1} * {num2} = {multiplication_result}")