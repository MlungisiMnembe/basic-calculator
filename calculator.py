def calculate(num1, num2, operation):
    """Perform a calculation using two numbers."""

    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return num1 / num2
    else:
        raise ValueError("Invalid operation.")


def main():
    print("=" * 35)
    print("       BASIC PYTHON CALCULATOR")
    print("=" * 35)

    while True:
        try:
            num1 = float(input("\nEnter the first number: "))
            operation = input("Choose an operation (+, -, *, /): ").strip()
            num2 = float(input("Enter the second number: "))

            result = calculate(num1, num2, operation)

            print(f"\nResult: {num1} {operation} {num2} = {result}")

        except ValueError as error:
            print(f"\nError: {error}")

        again = input("\nWould you like another calculation? (y/n): ").lower()

        if again != "y":
            print("\nThank you for using the calculator!")
            break


if __name__ == "__main__":
    main()
