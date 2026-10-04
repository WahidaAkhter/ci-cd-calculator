from calculator import add, subtract, multiply, divide, power


def main():
    print("=== Python Calculator Classroom ===")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Power\n6. Exit")

    while True:
        choice = input("\nSelect choice (1-6): ").strip()
        if choice == "6":
            print("Exiting...")
            break

        if choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice. Try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print(f"Result: {add(num1, num2)}")
            elif choice == "2":
                print(f"Result: {subtract(num1, num2)}")
            elif choice == "3":
                print(f"Result: {multiply(num1, num2)}")
            elif choice == "4":
                print(f"Result: {divide(num1, num2)}")
            elif choice == "5":
                print(f"Result: {power(num1, int(num2))}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()