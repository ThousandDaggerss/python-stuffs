"""
Project: Calculator
"""

def calc_logo() -> None:
    """
    Print the calculator logo.
    """
    logo = """
   ██████╗  █████╗ ██╗      ██████╗ 
  ██╔════╝ ██╔══██╗██║     ██╔════╝ 
  ██║      ███████║██║     ██║
  ██║      ██╔══██║██║     ██║
  ╚██████╗ ██║  ██║███████╗╚██████╗
   ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝ 
"""
    print(logo)

def calculate() -> None:
    """
    Main calculator logic with stacking results.
    """
    result = None

    while True:
        try:
            # Determine first number (use result if continuing)
            if result is None:
                num1 = float(input("Type the first number: "))
            else:
                print(f"Current result: {result}")
                num1 = result

            # Operation input
            operation = input("Type the operation (+, -, *, /): ").strip()
            if operation not in ["+", "-", "*", "/"]:
                print("Invalid operation. Try again.")
                continue

            # Second number input
            num2 = float(input("Type the second number: "))

            # Perform calculation
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    print("Division by zero is not allowed.")
                    continue
                result = num1 / num2

            # Show result
            print(f"Result: {result}")

        except ValueError:
            print("Please enter valid numbers.")
            continue

        # Ask to continue or reset memory
        cont = input("Do you want to continue? (y/n/reset): ").strip().lower()
        if cont == "reset":
            print("Memory cleared. Starting fresh.")
            result = None
        elif cont != "y":
            print("See you later. Bye!")
            break

if __name__ == "__main__":
    calc_logo()
    calculate()
