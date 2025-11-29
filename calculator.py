def calculator():
    """Simple command-line calculator with error handling"""
    
    def add(x, y):
        return x + y
    
    def subtract(x, y):
        return x - y
    
    def multiply(x, y):
        return x * y
    
    def divide(x, y):
        if y == 0:
            return "Error: Cannot divide by zero"
        return x / y
    
    def power(x, y):
        try:
            return x ** y
        except OverflowError:
            return "Error: Result too large"
    
    print("\n===== Simple Calculator =====")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Quit")
    print("=" * 30)
    
    while True:
        choice = input("\nSelect operation (1-6): ").strip()
        
        if choice == '6':
            print("Thank you for using the calculator!")
            break
        
        if choice in ['1', '2', '3', '4', '5']:
            try:
                num1 = float(input("Enter first number: ").strip())
                num2 = float(input("Enter second number: ").strip())
                
                if choice == '1':
                    result = add(num1, num2)
                    print(f"{num1} + {num2} = {result}")
                elif choice == '2':
                    result = subtract(num1, num2)
                    print(f"{num1} - {num2} = {result}")
                elif choice == '3':
                    result = multiply(num1, num2)
                    print(f"{num1} * {num2} = {result}")
                elif choice == '4':
                    result = divide(num1, num2)
                    if isinstance(result, str):  # Error message
                        print(result)
                    else:
                        print(f"{num1} / {num2} = {result}")
                elif choice == '5':
                    result = power(num1, num2)
                    if isinstance(result, str):  # Error message
                        print(result)
                    else:
                        print(f"{num1} ^ {num2} = {result}")
                    
            except ValueError:
                print("Error: Please enter valid numbers")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Invalid choice. Please select 1-6")

if __name__ == "__main__":
    calculator()
