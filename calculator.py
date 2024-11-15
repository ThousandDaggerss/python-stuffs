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

    while True:
        try:
            # first number
            num1 = float(input("Type first number: "))

            # operation
            operation = input("Type the operation (+, -, *, /): ")
            if operation not in ["+", "-", "*", "/"]:
                print("Operação inválida. Tente novamente.")
                continue

            # second number
            num2 = float(input("Type second number: "))

            # calculation
            result = None
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    print("Divise for zero is not allowed.")
                    continue
                result = num1 / num2

            # result
            print(f"Result: {result}")

        except ValueError:
            print("please enter valid numbers.")
            continue

        # ask to continue
        cont = input("Do you want to continue? (y/n): ").strip().lower()
        if cont != "y":
            print("See you later. Bye!")
            break

if __name__ == "__main__":
    calc_logo()
    calculate()
