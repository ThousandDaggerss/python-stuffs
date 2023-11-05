"""
FizzBuzz Challenge
"""

def fizz_buzz(n):
    """
    Given an integer n, return "Fizz" if n is divisible by 3, "Buzz" if n
    is divisible by 5, and "FizzBuzz" if n is divisible by both 3 and 5.
    """
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


def main():
    """
    Main function to run tests
    """

    for i in range(1, 101):
        print(fizz_buzz(i))




if __name__ == "__main__":
    main()
