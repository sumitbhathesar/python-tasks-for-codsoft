def add(numbers):
    """Return the sum of the numbers"""
    return sum(numbers)

def subtract(numbers):
    """Return the difference of the numbers"""
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(numbers):
    """Return the product of the numbers"""
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    """Return the quotient of the numbers"""
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        result /= num
    return result

def calculator():
    result = 0.0
    while True:
        print("Simple Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice in ['1', '2', '3', '4']:
            numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
            if choice == '1':
                result = add(numbers)
                print(f"Result: {result}")

            elif choice == '2':
                result = subtract(numbers)
                print(f"Result: {result}")

            elif choice == '3':
                result = multiply(numbers)
                print(f"Result: {result}")

            elif choice == '4':
                try:
                    result = divide(numbers)
                    print(f"Result: {result}")
                except ZeroDivisionError as e:
                    print(str(e))
        elif choice == '5':
            print("Thank you for using the calculator!")
            break
        else:
            print("Invalid choice")

calculator()